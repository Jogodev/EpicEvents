"""Collaborater controllers"""

from rich import print
from src.views.collaborater import CollaboraterView, CrudCollaboraterView
from src.models.collaborater import Collaborater
from src.helpers.check import check_email, check_password, hash_password
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
    def create(cls, payload: dict):
        """Post"""

        collaborater_dict = CrudCollaboraterView.create()
        if not check_email(collaborater_dict["email"]):
            print("[bold red]Email invalide[/bold red]")
            return "create_collaborater", payload
        if not check_password(collaborater_dict["password"]):
            print("[bold red]Mot de passe invalide[/bold red]")
            return "create_collaborater", payload
        if collaborater_dict["role"] == "1":
            collaborater_dict["role"] = "gestion"
        elif collaborater_dict["role"] == "2":
            collaborater_dict["role"] = "commercial"
        elif collaborater_dict["role"] == "3":
            collaborater_dict["role"] = "support"
        elif collaborater_dict["role"] not in ["1", "2", "3"]:
            print("[bold red]Choisissez entre les 3 groupes[/bold red]")
            return "create_collaborater", payload

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
        return "menu_collaborater", payload

    @classmethod
    def list_all(cls, payload):
        """all collaborators"""
        clear_screen()

        collaborators = db.query(Collaborater).all()
        choice = CrudCollaboraterView.list_all(collaborators)
        if choice == "b":
            return "menu_collaborater", payload
        else:
            print("[bold red]Saisie non valide[/bold red]")
            return "menu_collaborater", payload

    @classmethod
    def update(cls, payload: dict):
        """Update"""
        collaborators = db.query(Collaborater).all()
        collaborater_dict = CrudCollaboraterView.update(collaborators)
        collaborater = db.query(Collaborater).get(collaborater_dict["collaborater_id"])
        if collaborater is None:
            print("[bold red]Aucun collaborateur ne correspond à cet id[/bold red]")
            return "menu_collaborater", payload

        setattr(collaborater, collaborater_dict["key"], collaborater_dict["value"])
        db.commit()
        new_collaborater = db.query(Collaborater).get(
            collaborater_dict["collaborater_id"]
        )
        print(
            f"[bold green]Collaborateur modifié avec succès {new_collaborater}[/bold green]"
        )

        return "menu_collaborater", payload

    @classmethod
    def delete(cls, payload: dict):
        """Delete"""
        collaborators = db.query(Collaborater).all()
        collaborater_dict = CrudCollaboraterView.delete(collaborators)

        if collaborater_dict["choice"] == "y":
            collaborater = db.query(Collaborater).get(
                collaborater_dict["collaborater_id"]
            )
            if collaborater is None:
                print("[bold red]Ce contrat n'existe pas[/bold red]")
                return "menu_collaborater", payload
            print(collaborater)
            db.delete(collaborater)
            db.commit()
            print(f"[bold green]{collaborater.name} supprimé[/bold green]")
            return "menu_collaborater", payload
        if collaborater_dict["choice"] == "n":
            return "menu_collaborater", payload
        print("[bold red]Saisie non valide[/bold red]")
        return "menu_collaborater", payload
