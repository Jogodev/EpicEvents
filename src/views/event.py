"""Event views"""

from rich.table import Table
from rich.console import Console
from src.views.headers import Headers


class EventView:
    """Event view menu"""

    @staticmethod
    def menu_event_view():
        """Menu event"""
        Headers.menu_title("event")
        txt = """
                [1] - Ajouter un evennement
                [2] - Liste de tous les évènements
                [3] - Modifier un évènnement
                [4] - Supprimer un évènnement
                [b] - retour
                """
        print(txt)

        choice = input("Faites votre choix : ")
        return choice


class CrudEventView:
    """Crud event"""

    @staticmethod
    def create():
        """Post"""

        name = input(
            """
        Nom de l'évènement
        --> """
        )

        contract_id = input(
            """
        Id du contrat
        --> """
        )

        start_date = input(
            """
        Date de début
        --> """
        )

        end_date = input(
            """
        Date de fin
        --> """
        )

        customer_email = input(
            """
        Email du client
        --> """
        )

        support_contact = input(
            """
        Email equipe support
        --> """
        )

        attendees = input(
            """
        Nombre de personnes
        --> """
        )

        location = input(
            """
        Lieu de l'evennement
        --> """
        )

        description = input(
            """
        Description
        --> """
        )

        return {
            "name": name,
            "contract_id": contract_id,
            "start_date": start_date,
            "end_date": end_date,
            "customer_email": customer_email,
            "support_contact": support_contact,
            "attendees": attendees,
            "location": location,
            "description": description,
        }

    @staticmethod
    def list_all(events):
        """All events"""
        Headers.list_title("event")
        table = Table(title="Evènements")
        table.add_column("Id", justify="left", style="bold")
        table.add_column("Nom", justify="left", style="")
        table.add_column("Contrat n°", justify="left", style="")
        table.add_column("Client", justify="left", style="")
        table.add_column("Support", justify="left", style="")
        table.add_column("Lieu", justify="left", style="")
        table.add_column("Pax", justify="left", style="")
        table.add_column("Début", justify="left", style="")
        table.add_column("Fin", justify="left", style="")
        for event in events:
            table.add_row(
                str(event.id),
                event.name,
                str(event.contract_id),
                event.customer_email,
                event.support_contact,
                event.location,
                event.Attendees,
                str(event.start_date),
                str(event.end_date),
            )

        Console().print(table)
        choice = input(
            """
            [b] retour
            --> """
        )
        return choice

    @staticmethod
    def update(events):
        """All events"""
        Headers.update_title("event")
        table = Table(title="Evènements")
        table.add_column("Id", justify="left", style="bold")
        table.add_column("Nom", justify="left", style="")
        table.add_column("Contrat n°", justify="left", style="")
        table.add_column("Client", justify="left", style="")
        table.add_column("Support", justify="left", style="")
        table.add_column("Lieu", justify="left", style="")
        table.add_column("Pax", justify="left", style="")
        table.add_column("Début", justify="left", style="")
        table.add_column("Fin", justify="left", style="")
        for event in events:
            table.add_row(
                str(event.id),
                event.name,
                str(event.contract_id),
                event.customer_email,
                event.support_contact,
                event.location,
                event.Attendees,
                str(event.start_date),
                str(event.end_date),
            )

        Console().print(table)

        event_id = input(
            """
        Id de l'évènement à modifier
        --> """
        )

        key = input(
            """
        Champ à modifier
        --> """
        )

        value = input(
            """
        Nouvelle valeur
        --> """
        )

        return {"event_id": event_id, "key": key.lower(), "value": value}

    @staticmethod
    def delete(events):
        """Delete owned event"""
        Headers.delete_title("event")
        table = Table(title="Evènements")
        table.add_column("Id", justify="left", style="bold")
        table.add_column("Nom", justify="left", style="")
        table.add_column("Contrat n°", justify="left", style="")
        table.add_column("Client", justify="left", style="")
        table.add_column("Support", justify="left", style="")
        table.add_column("Lieu", justify="left", style="")
        table.add_column("Pax", justify="left", style="")
        table.add_column("Début", justify="left", style="")
        table.add_column("Fin", justify="left", style="")
        for event in events:
            table.add_row(
                str(event.id),
                event.name,
                str(event.contract_id),
                event.customer_email,
                event.support_contact,
                event.location,
                event.attendees,
                str(event.start_date),
                str(event.end_date),
            )

        Console().print(table)

        event_id = input(
            """
        Id de l'évènement à supprimer
        --> """
        )

        choice = input(
            """
        Cette action est irréversible êtes vous sûr ?

        [y] oui [n] annuler
            --> """
        )
        return {"choice": choice, "event_id": event_id}
