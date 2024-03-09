"""Event controllers"""

from src.views.event import EventView, CrudEventView
from src.models.event import Event
from src.utils.utils import clear_screen
from src.helpers.check import check_email
import datetime
from config import db
from rich import print


class EventController:
    """Event controller"""

    @classmethod
    def menu_event_controller(cls, payload):
        """Menu"""
        choice = EventView.menu_event_view()

        if choice == "1":
            return "create_event", payload
        if choice == "2":
            return "get_events", payload
        if choice == "4":
            return "delete_event", payload
        if choice == "b":
            return "main_menu", payload
        else:
            print("\nSaisie non valide\n")
            return "menu_event", payload


class CrudControllerEvent:
    """Crud controller"""

    @classmethod
    def create(cls, payload):
        """Post"""
        event = CrudEventView.create()
        if not check_email(event["customer_email"]):
            print("\n[bold red]Email du client invalide[/bold red]")
            return "create_event", payload
        if not check_email(event["support_contact"]):
            print("\n[bold red]Email de l'équipe support invalide[/bold red]")
            return "create_event", payload
        new_event = Event(
            name=event["name"],
            start_date=event["start_date"],
            end_date=event["end_date"],
            location=event["location"],
            attendees=event["attendees"],
            notes=event["description"],
            customer_email=event["customer_email"],
            support_contact=event["support_contact"],
            contract_id=event["contract_id"],
        )
        db.add(new_event)
        db.commit()

        print(f"[bold green]Evènement n° {new_event.id} créé[/bold green]")
        return "menu_customer", payload

    @classmethod
    def list_all(cls, payload: dict):
        """Get"""
        clear_screen()
        events = db.query(Event).all()
        choice = CrudEventView.list_all(events)
        if choice == "b":
            return "menu_event", payload

        print("[bold red]Saisie non valide[/bold red]")
        return "menu_event", payload

    @classmethod
    def delete(cls, payload: dict):
        """Delete"""

        events = db.query(Event).all()
        event_dict = CrudEventView.delete(events)

        if event_dict["choice"] == "y":
            event = db.query(Event).get(event_dict["event_id"])
            if event is None:
                print("[bold red]Ce contrat n'existe pas[/bold red]")
                return "menu_event", payload
            print(event)
            db.delete(event)
            db.commit()
            print(f"[bold green]Evènement n° {event.id} supprimé[/bold green]")
            return "menu_event", payload
        if event_dict["choice"] == "n":
            return "delete_event", payload
        print("[bold red]Saisie non valide[/bold red]")
        return "menu_event", payload
