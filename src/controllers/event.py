from src.views.event import EventView, CrudEventView
from src.models.event import Event
from src.utils.utils import clear_screen
from src.helpers.check import check_email
from rich import print
from config import db
import datetime

class EventController():
    def menu_event_controller(payload):
        
        choice = EventView.menu_event_view()
        
        if choice == "1":
            return "create_event", payload
        elif choice == "2":
            return "get_events", payload
        elif choice == "b":
            return "main_menu", payload
        else:
            print("\nSaisie non valide\n")
            return "menu_event", payload

class CrudControllerEvent:
    """Crud controller"""

    def create(payload):

        clear_screen()
        event = CrudEventView.create()
        if not check_email(event["customer_email"]):
            print("[bold red]Email du client invalide[/bold red]")
            return "create_event", payload
        elif not check_email(event["support_email"]):
            print("[bold red]Email de l'équipe support invalide[/bold red]")
            return "create_event", payload
        new_event = Event(name=event["name"], start_date=event["start_date"], end_date=event["end_date"], location=event["location"], attendees=event["attendees"], notes=event["description"], customer_email=event["customer_email"], support_email=event["support_email"], contract_id=event["contract_id"])
        db.add(new_event)
        db.commit()

        print(f"[bold green]Evènement n° {new_event.id} créé[/bold green]")
        return "menu_customer", payload
    
    def list_all(payload):

        clear_screen()

        events = db.query(Event).all()
        choice = CrudEventView.list_all(events)
        if choice == "b":
            return "menu_event", payload
        else:
            print("[bold red]Saisie non valide[/bold red]")
            return "menu_event", payload

