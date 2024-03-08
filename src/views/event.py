from src.views.headers import Headers
from rich.table import Table
from rich.console import Console

class EventView:
    def menu_event_view():
        """Menu evenT"""
        title = "\n-----------------------MENU EVENNEMENTS---------------------------"
        txt = """
                [1] - Ajouter un evennement
                [2] - Liste de tous les evennements
                [3] - Modifier un evennement
                [4] - Supprimer un evennement
                [b] - retour
                """
        print(title)
        print(txt)

        choice = input("Faites votre choix : ")
        return choice
