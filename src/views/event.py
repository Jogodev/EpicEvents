from src.views.headers import Headers
from rich.table import Table
from rich.console import Console


class EventView:
    def menu_event_view():
        """Menu evenT"""
        Headers.menu_title("event")
        txt = """
                [1] - Ajouter un evennement
                [2] - Liste de tous les evennements
                [3] - Modifier un evennement
                [4] - Supprimer un evennement
                [b] - retour
                """
        print(txt)

        choice = input("Faites votre choix : ")
        return choice


class CrudEventView:
    """Crud event"""

    def create():

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

        support_email = input(
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
            "support_email": support_email,
            "attendees": attendees,
            "location": location,
            "description": description,
        }

    def list_all(events):
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
        table.add_column("Début", justify="left", style="")
        for event in events:
            table.add_row(
                str(event.id),
                event.name,
                event.contract_id,
                event.customer_email,
                event.support_email,
                event.location,
                event.attendees,
                event.start_date,
                event.end_date,
                event.start_date,
            )

        Console().print(table)
        choice = input(
            """
            [b] retour
            --> """
        )
        return choice
