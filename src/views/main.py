"""Main menu view"""

from src.views.headers import Headers


def main_menu_view():
    """Main menu"""

    Headers.main_title()
    txt = """
         [1] - Collaborateur
         [2] - Clients
         [3] - Contrats
         [4] - Evènements
        """
    print(txt)
    choice = input("Faites votre choix : ")
    return choice
