"""Auth controller"""

from rich import print
from src.views.auth import auth_view
from src.models.collaborater import Collaborater
from src.utils.utils import clear_screen
from src.helpers.check import check_hash_password
from config import db


def auth_controller(payload: dict):
    """Menu"""

    collaborators = db.query(Collaborater).all()
    credential = auth_view(collaborators)
    collaborater_find = (
        db.query(Collaborater).filter_by(email=credential["email"]).first()
    )
    if not collaborater_find:
        print("[bold red] Email ou mot de passe invalide 1[/bold red]")
        return "auth_controller", payload
    collaborater = db.query(Collaborater).get(collaborater_find.id)
    print(collaborater.password)
    if check_hash_password(credential["password"], collaborater.password):
        payload = collaborater
        return "main_menu", payload
    print("[bold red] Email ou mot de passe invalide 2[/bold red]")
    return "auth_controller", payload
