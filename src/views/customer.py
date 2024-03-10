"""Customer views"""

from rich.table import Table
from rich.console import Console
from src.views.headers import Headers


class CustomerView:
    """Menu customer"""

    @classmethod
    def menu_customer_view(cls):
        """Menu customer"""
        Headers.menu_title("cusomer")
        txt = """
                        [1] - Ajouter un client
                        [2] - Liste de tous les clients
                        [3] - Modifier un client
                        [4] - Supprimer un client
                        [b] - retour au menu principal
                        """
        print(txt)

        choice = input(
            """
        [b] retour
        --> """
        )
        return choice


class CrudCustomerView:
    """Crud customer view"""

    @staticmethod
    def create():
        """Post"""
        Headers.create_title("customer")

        email = input(
            """
        Email 
        --> """
        )

        name = input(
            """
        Nom 
        --> """
        )

        phone = input(
            """
        Numero de téléphone 
        --> """
        )

        company = input(
            """
        Entreprise 
        --> """
        )

        return {
            "email": email,
            "name": name,
            "phone": phone,
            "company": company,
        }

    @staticmethod
    def list_all(customers):
        """All customers"""
        Headers.list_title("customer")
        table = Table(title="Clients")
        table.add_column("Id", justify="left", style="bold")
        table.add_column("Nom", justify="left", style="")
        table.add_column("Email", justify="left", style="")
        table.add_column("Télephone", justify="left", style="")
        table.add_column("Entreprise", justify="left", style="")
        for customer in customers:
            table.add_row(
                str(customer.id),
                customer.name,
                customer.email,
                customer.phone,
                customer.company,
            )

        Console().print(table)
        choice = input(
            """
        [b] retour
        --> """
        )
        return choice

    @staticmethod
    def update(customers):
        """All customers"""
        Headers.update_title("customer")
        table = Table(title="Clients")
        table.add_column("Id", justify="left", style="bold")
        table.add_column("Nom", justify="left", style="")
        table.add_column("Email", justify="left", style="")
        table.add_column("Télephone", justify="left", style="")
        table.add_column("Entreprise", justify="left", style="")
        for customer in customers:
            table.add_row(
                str(customer.id),
                customer.name,
                customer.email,
                customer.phone,
                customer.company,
            )

        Console().print(table)

        customer_id = input(
            """
        Id du customer à modifier
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

        return {"customer_id": customer_id, "key": key.lower(), "value": value}

    @staticmethod
    def delete(customers):
        """Delete"""
        Headers.delete_title("customer")
        table = Table(title="Clients")
        table.add_column("Id", justify="left", style="bold")
        table.add_column("Nom", justify="left", style="")
        table.add_column("Email", justify="left", style="")
        table.add_column("Télephone", justify="left", style="")
        table.add_column("Entreprise", justify="left", style="")
        for customer in customers:
            table.add_row(
                str(customer.id),
                customer.name,
                customer.email,
                customer.phone,
                customer.company,
            )

        Console().print(table)
        customer_id = input(
            """
        Id du client à supprimer
        --> """
        )

        choice = input(
            """
        Cette action est irréversible êtes vous sûr ?

        [y] oui [n] annuler
            --> """
        )
        return {"choice": choice, "customer_id": customer_id}
