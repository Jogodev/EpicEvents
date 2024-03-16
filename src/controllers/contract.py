"""Contract controllers"""

import datetime
from src.views.contract import ContractView, CrudContractView
from src.models.contract import Contract
from src.utils.utils import clear_screen
from src.helpers.check_collaborater import check_email
from config import db
from rich import print


class ContractController:
    """Menu controller"""

    @classmethod
    def menu_contract_controller(cls, payload: dict):
        """Menu"""
        print(f"[bold green] Bonjour {payload.name.upper()} [/bold green]")
        choice = ContractView.menu_contract_view()

        if choice == "1":
            return "create_contract", payload
        if choice == "2":
            return "get_contracts", payload
        if choice == "3":
            return "update_contract", payload
        if choice == "4":
            return "delete_contract", payload
        if choice == "b":
            return "main_menu", payload

        print("\nSaisie non valide\n")
        return "menu_contract", payload


class CrudContractController:
    """Crud contract"""

    @classmethod
    def create(cls, payload: dict):
        """Post"""
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

    @classmethod
    def list_all(cls, payload: dict):
        """All contracts"""
        clear_screen()

        contracts = db.query(Contract).all()
        choice = CrudContractView.list_all(contracts)
        if choice == "b":
            return "menu_contract", payload
        else:
            print("[bold red]Saisie non valide[/bold red]")
            return "menu_contract", payload

    @classmethod
    def update(cls, payload: dict):
        """Update"""
        contracts = db.query(Contract).all()
        contract_dict = CrudContractView.update(contracts)
        contract = db.query(Contract).get(contract_dict["contract_id"])
        if contract is None:
            print("[bold red]Aucun contract ne correspond à cet id[/bold red]")
            return "menu_contract", payload

        setattr(contract, contract_dict["key"], contract_dict["value"])
        db.commit()
        new_contract = db.query(Contract).get(contract_dict["contract_id"])
        print(f"[bold green]Contrat modifié avec succès {new_contract}[/bold green]")

        return "menu_contract", payload

    @classmethod
    def delete(cls, payload: dict):
        """Delete"""
        contracts = db.query(Contract).all()
        contract_dict = CrudContractView.delete(contracts)

        if contract_dict["choice"] == "y":
            contract = db.query(Contract).get(contract_dict["contract_id"])
            if contract is None:
                print("[bold red]Ce contrat n'existe pas[/bold red]")
                return "menu_contract", payload
            print(contract)
            db.delete(contract)
            db.commit()
            print(f"[bold green]{contract.name} supprimé[/bold green]")
            return "menu_contract", payload
        if contract_dict["choice"] == "n":
            return "menu_contract", payload
        print("[bold red]Saisie non valide[/bold red]")
        return "menu_contract", payload
