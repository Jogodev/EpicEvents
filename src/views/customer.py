from src.views.headers import Headers
from rich.table import Table
from rich.console import Console
import logging


class CustomerView:

    def menu_customer_view():
        """Menu player"""
        Headers.menu_title("cusomer")
        txt = """
                        [1] - Ajouter un client
                        [2] - Liste de tous les clients
                        [3] - Modifier un client
                        [4] - Supprimer un client
                        [b] - retour au menu principal
                        """
        print(txt)

        choice = input("")
        return choice


class CrudCustomerView:

    def create():
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

    def get(customers):
        Headers.list_title("customer")
        table = Table(title="Collaborateur(s)")
        table.add_column("Id")
        table.add_column("Nom")
        table.add_column("Email")
        table.add_column("Télephone")
        table.add_column("Entreprise")
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
