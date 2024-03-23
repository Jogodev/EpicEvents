"""Collaborater views"""

from rich.table import Table
from rich.console import Console
from src.views.headers import Headers


class CollaboraterView:
    """Menu"""

    @classmethod
    def menu_collaborater_view(cls):
        """Menu collaborater"""
        Headers.menu_title("collaborater")

        txt = """
        [1] - Ajouter un collaborateur
        [2] - Liste de tous les collaborateurs
        [3] - Modifier un collaborateur
        [4] - Supprimer un collaborateur
        [b] - retour au menu principal
        """
        print(txt)

        choice = input("Faites votre choix : ")
        return choice


class CrudCollaboraterView:
    """Collaborators views"""

    @staticmethod
    def create():
        """Post"""
        Headers.create_title("collaborater")

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

        role = input(
            """
        Ajouter à un groupe

        [1] - Gestion
        [2] - Commercial
        [3] - Support
        --> """
        )

        password = input(
            """
        Au moins 6 caractères et un chiffre
        Mot de passe
        --> """
        )

        return {
            "email": email,
            "name": name.capitalize(),
            "password": password,
            "role": role,
        }

    @staticmethod
    def list_all(collaborators):
        """All collaborators"""
        Headers.list_title("collaborater")
        table = Table(title="Collaborateur(s)")
        table.add_column("Id")
        table.add_column("Nom")
        table.add_column("email")
        table.add_column("Groupe")
        table.add_column("mdb")
        for collaborater in collaborators:
            table.add_row(
                str(collaborater.id),
                collaborater.name,
                collaborater.email,
                collaborater.role,
                collaborater.password,
            )

        Console().print(table)

        choice = input(
            """
        [b] retour
        --> """
        )
        return choice

    @staticmethod
    def update(collaborators) -> dict:
        """Update"""
        Headers.update_title("collaborater")
        table = Table(title="Collaborateurs")
        table.add_column("Id")
        table.add_column("Nom(name)")
        table.add_column("Email")
        table.add_column("Groupe")
        table.add_column("mdp")
        for collaborater in collaborators:
            table.add_row(
                str(collaborater.id),
                collaborater.name,
                collaborater.email,
                collaborater.role,
                collaborater.password,
            )

        Console().print(table)

        collaborater_id = input(
            """
        Id du collaborateur à modifier
        --> """
        )

        field_to_change = input(
            """
        Quel champ voulez vous modifier ?

        [1] Email
        [2] Name
        [3] Groupe
        [4] Mot de passe (seulement si vous êtes le collaborateur en question)

        --> """
        )

        value = input(
            """
        Nouvelle valeur
        --> """
        )

        return {
            "collaborater_id": collaborater_id,
            "field_to_change": field_to_change.lower(),
            "value": value,
        }

    @staticmethod
    def delete(collaborators):
        """Delete one collaboratoer"""
        Headers.delete_title("collaborater")
        table = Table(title="Collaborateurs")
        table.add_column("Id")
        table.add_column("Nom")
        table.add_column("email")
        table.add_column("Groupe")
        for collaborater in collaborators:
            table.add_row(
                str(collaborater.id),
                collaborater.name,
                collaborater.email,
                collaborater.role,
            )

        Console().print(table)

        collaborater_id = input(
            """
        Id du collaborateur à supprimer
        --> """
        )

        choice = input(
            """
        Cette action est irréversible êtes vous sûr ?

        [y] oui [n] annuler
            --> """
        )
        return {"choice": choice, "collaborater_id": collaborater_id}
