from src.views.headers import Headers
from rich.table import Table
from rich.console import Console


class CollaboraterView:

    def menu_collaborater_view():
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

    def create():
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

        return {"email": email, "name": name, "password": password, "role": role}

    def get(collaborators):
        Headers.list_title("collaborater")
        table = Table(title="Collaborateur(s)")
        table.add_column("Id")
        table.add_column("Nom")
        table.add_column("email")
        table.add_column("Groupe")
        for collaborater in collaborators:            
            table.add_row(str(collaborater.id),collaborater.name, collaborater.email, collaborater.role)


        Console().print(table)
        choice = input(
            """
        [b] retour
        --> """
        )
        return choice
    
    def update(collaborators):
        Headers.list_title("collaborater")
        table = Table(title="Collaborateur(s)")
        table.add_column("Id")
        table.add_column("Nom")
        table.add_column("Email")
        table.add_column("Groupe")
        for collaborater in collaborators:            
            table.add_row(str(collaborater.id),collaborater.name, collaborater.email, collaborater.role)


        Console().print(table)

        choice = input(
            """
        [1] Modifier un collaborateur
        --> """
        )

        choice = input(
            """
        [b] retour
        --> """
        )
        return choice
    
    def delete(collaborators):
        Headers.list_title("collaborater")
        table = Table(title="Collaborateurs")
        table.add_column("Id")
        table.add_column("Nom")
        table.add_column("email")
        table.add_column("Groupe")
        for collaborater in collaborators:            
            table.add_row(str(collaborater.id),collaborater.name, collaborater.email, collaborater.role)


        Console().print(table)

        choice = input(
            """
        [1] Supprimer un un collaborateur
        --> """
        )

        choice = input(
            """
        [b] retour
        --> """
        )
        return choice
