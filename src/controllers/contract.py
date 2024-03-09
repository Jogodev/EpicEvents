from src.views.contract import ContractView, CrudContractView
from src.models.contract import Contract
from src.utils.utils import clear_screen
from src.helpers.check import check_email
from rich import print
from config import db
import datetime


class ContractController:

    def menu_contract_controller(payload):
        """Menu"""

        choice = ContractView.menu_contract_view()

        if choice == "1":
            return "create_contract", payload
        if choice == "2":
            return "get_contracts", payload
        elif choice == "b":
            return "main_menu", payload
        else:
            print("\nSaisie non valide\n")
            return "menu_contract", payload


class CrudContractController:
    """Crud contract"""

    def create(payload):

        clear_screen()
        contract = CrudContractView.create()
        if contract["status"] == "n":
            contract["status"] = False
        elif contract["status"] == "y":
            contract["status"] = True
        elif contract["status"] not in ["y", "n"]:
            print("[bold red]Saisie invalide du status (y/n)[/bold red]")
            return "create_contract", payload
        elif not check_email(contract["email"]):
            print("[bold red]Email invalide[/bold red]")
            return "create_contract", payload

        new_contract = Contract(
            customer_email=contract["customer_email"],
            contract_price=contract["contract_price"],
            left_to_pay=contract["left_to_pay"],
            status=contract["status"],
            created_at=datetime.datetime.now().strftime("%d-%m-%Y"),
        )
        db.add(new_contract)
        db.commit()
        print(f"[bold green]Nouveau contrat n° {new_contract.id}[/bold green]")
        return "menu_contract", payload

    def list_all(payload):

        clear_screen()

        contracts = db.query(Contract).all()
        choice = CrudContractView.list_all(contracts)
        if choice == "b":
            return "menu_contract", payload
        else:
            print("[bold red]Saisie non valide[/bold red]")
            return "menu_contract", payload
