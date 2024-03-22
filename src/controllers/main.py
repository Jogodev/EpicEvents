"""Main menu controller"""

from rich import print
from src.utils.utils import clear_screen
from src.views.main import main_menu_view


def main_menu_controller(current_collaborater):
    """Main menu"""
    clear_screen()
    print(f"[bold green] Bonjour {current_collaborater.name.upper()} [/bold green]")
    choice = main_menu_view()

    if choice == "1":
        return "menu_collaborater", current_collaborater
    elif choice == "2":
        return "menu_customer", current_collaborater
    elif choice == "3":
        return "menu_contract", current_collaborater
    elif choice == "4":
        return "menu_event", current_collaborater
    else:
        print("\nSaisie non valide\n")
        return "main_menu", current_collaborater
