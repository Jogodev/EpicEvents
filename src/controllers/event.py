"""Event controllers"""

from src.views.event import EventView, CrudEventView
from src.models.event import Event
from src.models.contract import Contract
from src.models.customer import Customer
from src.utils.utils import clear_screen
from src.helpers.permissions import is_support, is_management, is_sale
from src.helpers.check_common import check_email, is_email_exist
import datetime
from config import db
from rich import print


class EventController:
    """Event controller"""

    @classmethod
    def menu_event_controller(cls, current_collaborater):
        """Menu"""
        choice = EventView.menu_event_view()

        if choice == "1":
            return "create_event", current_collaborater
        if choice == "2":
            return "get_events", current_collaborater
        if choice == "3":
            return "update_event", current_collaborater
        if choice == "4":
            return "delete_event", current_collaborater
        if choice == "b":
            return "main_menu", current_collaborater
        else:
            print("\nSaisie non valide\n")
            return "menu_event", current_collaborater


class CrudEventController:
    """Crud controller"""

    @classmethod
    def create(cls, current_collaborater):
        """Post"""
        if not is_sale(current_collaborater.role):
            print(
                "[bold red]Vous n'êtes pas autorisé à créer des évènements[/bold red]"
            )
            return "menu_event", current_collaborater
        customers = (
            db.query(Customer).join(Contract).filter(Contract.status == True).all()
        )

        event = CrudEventView.create(customers)
        if not is_email_exist(event["customer_email"], Customer):
            print("[bold red]Aucun client ne correspond à cet email[/bold red]")
            return "create_event", current_collaborater
        new_event = Event(
            name=event["name"],
            start_date=event["start_date"],
            end_date=event["end_date"],
            location=event["location"],
            attendees=event["attendees"],
            notes=event["description"],
            customer_email=event["customer_email"],
            contract_id=event["contract_id"],
        )
        db.add(new_event)
        db.commit()

        print(f"[bold green]Evènement n° {new_event.id} créé[/bold green]")
        return "menu_event", current_collaborater

    @classmethod
    def list_all(cls, current_collaborater: dict):
        """Get"""
        clear_screen()
        events = db.query(Event).all()
        choice = CrudEventView.list_all(events)
        if choice == "b":
            return "menu_event", current_collaborater

        print("[bold red]Saisie non valide[/bold red]")
        return "menu_event", current_collaborater

    @classmethod
    def update(cls, current_collaborater: dict):
        """Update"""

        if not is_management(current_collaborater.role) or not is_support(
            current_collaborater.role
        ):
            print(
                "[bold red]Vous n'êtes pas autorisé à modifier des évènements[/bold red]"
            )
            return "menu_event", current_collaborater
        events = db.query(Event).all()
        event_dict = CrudEventView.update(events)
        event = db.query(Event).get(event_dict["event_id"])
        event_contract = db.query(Contract).get(event_dict["event_id"])
        if event is None:
            print("[bold red]Aucun évènement ne correspond à cet id[/bold red]")
            return "menu_event", current_collaborater

        setattr(event, event_dict["key"], event_dict["value"])
        db.commit()
        new_event = db.query(Event).get(event_dict["event_id"])
        print(f"[bold green]Evènement modifié avec succès {new_event}[/bold green]")

        return "menu_event", current_collaborater

    @classmethod
    def delete(cls, current_collaborater: dict):
        """Delete"""

        events = db.query(Event).all()
        event_dict = CrudEventView.delete(events)

        if event_dict["choice"] == "y":
            event = db.query(Event).get(event_dict["event_id"])
            if event is None:
                print("[bold red]Cet évènement n'existe pas[/bold red]")
                return "menu_event", current_collaborater
            print(event)
            db.delete(event)
            db.commit()
            print(f"[bold green]Evènement n° {event.id} supprimé[/bold green]")
            return "menu_event", current_collaborater
        if event_dict["choice"] == "n":
            return "delete_event", current_collaborater
        print("[bold red]Saisie non valide[/bold red]")
        return "menu_event", current_collaborater
