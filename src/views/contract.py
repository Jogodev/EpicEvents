from src.views.headers import Headers
from rich.table import Table
from rich.console import Console


class ContractView:

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

    def create():

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

    def list_all(contracts):
        Headers.list_title("contract")
        table = Table(title="Contrats")
        table.add_column("Id", justify="left", style="bold")
        table.add_column("Client", justify="left", style="bold")
        table.add_column("Montant", justify="left", style="bold")
        table.add_column("Reste à payer", justify="left", style="bold")
        table.add_column("Statut", justify="left", style="bold")
        for contract in contracts:
            if contract.status == False:
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
