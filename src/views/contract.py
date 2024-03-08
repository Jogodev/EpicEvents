from src.views.headers import Headers
from rich.table import Table
from rich.console import Console

class ContractView:

    def menu_contract_view():
        """Menu contract"""

        title = "\n-----------------------MENU CONTRATS---------------------------"
        txt = """
                        [1] - Ajouter un contrat
                        [2] - Liste de tous les contrats
                        [3] - Modifier un contrat
                        [4] - Supprimer un contrat
                        [b] - retour
                        """
        print(title)
        print(txt)

        choice = input("Faites votre choix : ")
        return choice
