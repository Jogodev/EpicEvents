from src.views.headers import Headers
import logging


class CustomerView:

    def menu_customer_view():
        """Menu player"""
        Headers.menu_title("cusomer")
        txt = """
                        [1] - Ajouter un client
                        [2] - Modifier un client
                        [3] - Supprimer un client
                        [4] - Liste de tous les clients
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
