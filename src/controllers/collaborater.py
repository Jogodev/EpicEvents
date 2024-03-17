"""Collaborater controllers"""

from rich import print
from src.views.collaborater import CollaboraterView, CrudCollaboraterView
from src.models.collaborater import Collaborater
from src.helpers.check_common import check_email
from src.helpers.permissions import is_management
from src.helpers.check_collaborater import (
    check_password,
    hash_password,
    can_update_collaborater,
    check_field_to_update,
)
from src.utils.utils import clear_screen
from config import db


class CollaboraterController:
    """Menu"""

    @classmethod
    def menu_collaborater_controller(cls, payload: dict):
        """Menu"""

        choice = CollaboraterView.menu_collaborater_view()
        if choice == "1":
            return "create_collaborater", payload
        if choice == "2":
            return "get_collaborators", payload
        if choice == "3":
            return "update_collaborater", payload
        if choice == "4":
            return "delete_collaborater", payload
        if choice == "b":
            return "main_menu", payload

        print("\nSaisie non valide\n")
        return "menu_collaborater", payload


class CrudCollaboraterController:
    """Crud collaborater"""

    @classmethod
    def create(cls, current_collaborater: dict):
        """Post"""

        if is_management(current_collaborater.role) != "management":
            print(
                "[bold red]Vous n'êtes pas autorisé à ajouter des collaborateurs[/bold red]"
            )
            return "menu_collaborater", current_collaborater
        collaborater_dict = CrudCollaboraterView.create()
        if not check_email(collaborater_dict["email"]):
            print("[bold red]Email invalide[/bold red]")
            return "create_collaborater", current_collaborater
        if not check_password(collaborater_dict["password"]):
            print("[bold red]Mot de passe invalide[/bold red]")
            return "create_collaborater", current_collaborater
        if collaborater_dict["role"] == "1":
            collaborater_dict["role"] = "management"
        elif collaborater_dict["role"] == "2":
            collaborater_dict["role"] = "sale"
        elif collaborater_dict["role"] == "3":
            collaborater_dict["role"] = "support"
        elif collaborater_dict["role"] not in ["1", "2", "3"]:
            print("[bold red]Choisissez entre les 3 groupes[/bold red]")
            return "create_collaborater", current_collaborater

        new_collab = Collaborater(
            email=collaborater_dict["email"],
            password=hash_password(collaborater_dict["password"]),
            role=collaborater_dict["role"],
            name=collaborater_dict["name"],
        )

        db.add(new_collab)
        db.commit()
        print(
            f"[bold green]{new_collab.name} ajouté dans le groupe {new_collab.role}[/bold green]"
        )
        return "menu_collaborater", current_collaborater

    @classmethod
    def list_all(cls, current_collaborater):
        """all collaborators"""
        clear_screen()

        collaborators = db.query(Collaborater).all()
        choice = CrudCollaboraterView.list_all(collaborators)
        if choice == "b":
            return "menu_collaborater", current_collaborater
        print("[bold red]Saisie non valide[/bold red]")
        return "menu_collaborater", current_collaborater

    @classmethod
    def update(cls, current_collaborater: dict):
        """Update"""

        collaborators = db.query(Collaborater).all()
        collaborater_dict = CrudCollaboraterView.update(collaborators)
        collaborater = db.query(Collaborater).get(collaborater_dict["collaborater_id"])
        if can_update_collaborater(
            collaborater, collaborater_dict, current_collaborater
        ):
            if collaborater_dict["field_to_change"] == "4":
                setattr(
                    collaborater,
                    check_field_to_update(collaborater_dict["field_to_change"]),
                    hash_password(collaborater_dict["value"]),
                )
            else:
                setattr(
                    collaborater,
                    check_field_to_update(collaborater_dict["field_to_change"]),
                    collaborater_dict["value"],
                )
            db.commit()
            print("[bold green]Collaborateur modifié[/bold green]")
            return "menu_collaborater", current_collaborater

        return "menu_collaborater", current_collaborater

    @classmethod
    def delete(cls, current_collaborater: dict):
        """Delete"""

        if is_management(current_collaborater.role) != "management":
            print(
                "[bold red]Vous n'êtes pas autorisé à ajouter des collaborateurs[/bold red]"
            )
            return "menu_collaborater", current_collaborater
        collaborators = db.query(Collaborater).all()
        collaborater_dict = CrudCollaboraterView.delete(collaborators)

        if collaborater_dict["choice"] == "y":
            collaborater = db.query(Collaborater).get(
                collaborater_dict["collaborater_id"]
            )
            if collaborater is None:
                print("[bold red]Ce contrat n'existe pas[/bold red]")
                return "menu_collaborater", current_collaborater
            db.delete(collaborater)
            db.commit()
            print(f"[bold green]{collaborater.name} supprimé[/bold green]")
            return "menu_collaborater", current_collaborater
        if collaborater_dict["choice"] == "n":
            return "menu_collaborater", current_collaborater
        print("[bold red]Saisie non valide[/bold red]")
        return "menu_collaborater", current_collaborater
