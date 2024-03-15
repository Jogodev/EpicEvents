"""Authentication views"""

from rich.table import Table
from rich.console import Console
from src.views.headers import Headers


def auth_view(collaborators):
    """Menu authentication"""
    Headers.menu_title("auth")
    table = Table(title="Collaborateur(s)")
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

    email = input(
        """
    Email
    --> """
    )

    password = input(
        """
    Mot de passe
    --> """
    )

    return {"email": email, "password": password}
