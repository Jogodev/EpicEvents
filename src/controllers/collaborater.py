from src.views.collaborater import CollaboraterView, CrudCollaboraterView
from src.helpers.check import check_email, check_password
from rich import print
from config import db
from src.utils.utils import clear_screen
from src.models.collaborater import Collaborater
import logging


class CollaboraterController:

    def menu_collaborater_controller(payload: dict):

        clear_screen()
        choice = CollaboraterView.menu_collaborater_view()
        if choice == "1":
            return "create_collaborater", payload
        elif choice == "b":
            return "main_menu", payload
        else:
            print("\nSaisie non valide\n")
            return "menu_collaborater", payload


class CrudCollaboraterController:

    def create(payload):
        
        clear_screen()
        collaborater_dict = CrudCollaboraterView.create()
        if not check_email(collaborater_dict["email"]):
            print(
                "[bold red]Email invalide[/bold red]"
            )
            return "create_collaborater", payload
        elif not check_password(collaborater_dict["password"]):
            print(
                "[bold red]Mot de passe invalide[/bold red]"
            )
            return "create_collaborater", payload
        elif collaborater_dict["role"] == "1":
            collaborater_dict["role"] = "gestion"
        elif collaborater_dict["role"] == "2":
            collaborater_dict["role"] = "commercial"
        elif collaborater_dict["role"] == "3":
            collaborater_dict["role"] = "support"
        elif collaborater_dict["role"] != ['1', '2', '3']: 
            print(
                "[bold red]Choisissez entre les 3 groupes[/bold red]"
            )
            return "create_collaborater", payload
        new_collab = Collaborater(
            email=collaborater_dict["email"],
            password=collaborater_dict["password"],
            role=collaborater_dict["role"],
            name=collaborater_dict["name"],
        )

        db.add(new_collab)
        db.commit()
        print(
                f"[bold green]{new_collab.name} ajouté au collaborateur dans le groupe {new_collab.role}[/bold green]"
            )
        return "main_menu", payload
