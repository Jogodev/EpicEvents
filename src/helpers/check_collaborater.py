"""Checks for inputs"""

import re
import bcrypt
from src.utils.utils import regex_mail, regex_mdp, regex_phone
from rich import print


def check_password(password):
    return bool(re.fullmatch(regex_mdp, password))


def check_phone(phone):
    return bool(re.fullmatch(regex_phone, phone))


# Hash password
def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def check_hash_password(password, hashed_password):
    hashed_password = hash_password(password)
    return bool(bcrypt.checkpw(password.encode(), hashed_password))


# Collaborators update
def can_update_collaborater(
    collaborater: dict, collaborater_dict: dict, current_collaborater: dict
) -> bool:
    if collaborater is None:
        print("[bold red]Aucun collaborateur ne correspond à cet id[/bold red]")
        return "menu_collaborater", current_collaborater
    if (collaborater.id != current_collaborater.id) and (
        collaborater_dict["field_to_change"] == "4"
    ):
        print(
            "[bold red]Vous ne pouvez pas modifier le mot de passe d'un autre collaborater[/bold red]"
        )
        return "menu_collaborater", current_collaborater
    if current_collaborater.role != "gestion" and (
        collaborater_dict["field_to_change"] in ["1", "2", "3"]
    ):
        print("[bold red]Vous ne faites pas parti de l'equipe de gestion[/bold red]")
        return "menu_collaborater", current_collaborater

    if current_collaborater.role == "gestion" and (
        collaborater_dict["field_to_change"] in ["1", "2", "3"]
    ):
        return True
    if (collaborater.id == current_collaborater.id) and (
        collaborater_dict["field_to_change"] == "4"
    ):
        return True


def check_field_to_update(field_to_update):
    if field_to_update == "1":
        field_to_update = "email"
    elif field_to_update == "2":
        field_to_update = "name"
    elif field_to_update == "3":
        field_to_update = "role"
    elif field_to_update == "4":
        field_to_update = "password"
    return field_to_update
