from src.utils.utils import clear_screen
from src.views.main import main_menu_view


def main_menu_controller(payload):

    clear_screen()
    choice = main_menu_view()

    if choice == "1":
        return "menu_collaborater", payload
    elif choice == "2":
        return "menu_customer", payload
    elif choice == "3":
        return "menu_contract", payload
    elif choice == "4":
        return "menu_event", payload
    else:
        print("\nSaisie non valide\n")
        return "main_menu", payload
