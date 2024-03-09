"""Contract views"""

from rich.table import Table
from rich.console import Console
from src.views.headers import Headers

class ContractView:
    """Menu view"""
    @staticmethod
    def menu_contract_view():
        """Menu contract"""

        Headers.menu_title("contract")
        txt = """
                        [1] - Ajouter un contrat
                        [2] - Liste de tous les contrats
                        [3] - Modifier un contrat
                        [4] - Supprimer un contrat
                        [b] - retour
                        """
        print(txt)

        choice = input("Faites votre choix : ")
        return choice


class CrudContractView:
    """Crud contract"""

    @staticmethod
    def create():
        """Post"""
        Headers.create_title("contract")

        customer_email = input(
            """
        Email du client
        --> """
        )

        contract_price = input(
            """
        Montant total
        --> """
        )

        left_to_pay = input(
            """
        Reste à payer
        --> """
        )

        status = input(
            """
        Signé ? y/n
        --> """
        )

        return {
            "customer_email": customer_email,
            "contract_price": contract_price,
            "left_to_pay": left_to_pay,
            "status": status,
        }

    @staticmethod
    def list_all(contracts):
        """All contracts"""
        Headers.list_title("contract")
        table = Table(title="Contrats")
        table.add_column("Id", justify="left", style="bold")
        table.add_column("Client", justify="left", style="bold")
        table.add_column("Montant", justify="left", style="bold")
        table.add_column("Reste à payer", justify="left", style="bold")
        table.add_column("Statut", justify="left", style="bold")
        for contract in contracts:
            if contract.status is False:
                contract.status = "En attente de signature"
            else:
                contract.status = "Signé"
            table.add_row(
                str(contract.id),
                contract.customer_email,
                contract.contract_price,
                contract.left_to_pay,
                contract.status,
            )

        Console().print(table)
        choice = input(
            """
        [b] retour
        --> """
        )
        return choice

    @staticmethod
    def delete(contracts):
        """Delete"""
        Headers.delete_title("contract")
        table = Table(title="Contrats")
        table.add_column("Id", justify="left", style="bold")
        table.add_column("Client", justify="left", style="bold")
        table.add_column("Montant", justify="left", style="bold")
        table.add_column("Reste à payer", justify="left", style="bold")
        table.add_column("Statut", justify="left", style="bold")
        for contract in contracts:
            if contract.status is False:
                contract.status = "En attente de signature"
            else:
                contract.status = "Signé"
            table.add_row(
                str(contract.id),
                contract.customer_email,
                contract.contract_price,
                contract.left_to_pay,
                contract.status,
            )

        Console().print(table)

        contract_id = input(
            """
        Id du contrat à supprimer
        --> """
        )

        choice = input(
            """
        Cette action est irréversible êtes vous sûr ?

        [y] oui [n] annuler
            --> """
        )
        return {"choice": choice, "contract_id": contract_id}
