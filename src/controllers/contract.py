"""Contract controllers"""

import datetime
from src.views.contract import ContractView, CrudContractView
from src.models.contract import Contract
from src.models.customer import Customer
from src.models.collaborater import Collaborater
from src.helpers.check_contract import check_field_to_update, status_value
from src.utils.utils import clear_screen
from src.helpers.permissions import is_management
from src.helpers.check_common import check_email, is_email_exist
from config import db
from rich import print


class ContractController:
    """Menu controller"""

    @classmethod
    def menu_contract_controller(cls, current_collaborater: dict):
        """Menu"""

        choice = ContractView.menu_contract_view()

        if choice == "1":
            return "create_contract", current_collaborater
        if choice == "2":
            return "get_contracts", current_collaborater
        if choice == "3":
            return "update_contract", current_collaborater
        if choice == "4":
            return "delete_contract", current_collaborater
        if choice == "b":
            return "main_menu", current_collaborater

        print("\nSaisie non valide\n")
        return "menu_contract", current_collaborater


class CrudContractController:
    """Crud contract"""

    @classmethod
    def create(cls, current_collaborater: dict):
        """Post"""
        clear_screen()
        if not is_management(current_collaborater.role):
            print("[bold red]Vous n'êtes pas autorisé à créer des contrats[/bold red]")
            return "menu_contract", current_collaborater
        customers = db.query(Customer).all()
        contract = CrudContractView.create(customers)
        if not is_email_exist(contract["customer_email"], Customer):
            print("[bold red]Ce client n'existe pas[/bold red]")
            return "menu_contract", current_collaborater
        if contract["status"] == "n":
            contract["status"] = False
        elif contract["status"] == "y":
            contract["status"] = True
        elif contract["status"] not in ["y", "n"]:
            print("[bold red]Saisie invalide du status (y/n)[/bold red]")
            return "create_contract", current_collaborater
        elif not check_email(contract["email"]):
            print("[bold red]Email invalide[/bold red]")
            return "create_contract", current_collaborater
        customer = (
            db.query(Customer).filter_by(email=contract["customer_email"]).first()
        )
        collaborater = db.query(Collaborater).get(customer.collaborater_id)
        new_contract = Contract(
            customer_email=contract["customer_email"],
            contract_price=contract["contract_price"],
            left_to_pay=contract["left_to_pay"],
            status=contract["status"],
            collaborater_email=collaborater.email,
            created_at=datetime.datetime.now().strftime("%d-%m-%Y"),
        )
        db.add(new_contract)
        db.commit()
        print(f"[bold green]Nouveau contrat n° {new_contract.id}[/bold green]")
        return "menu_contract", current_collaborater

    @classmethod
    def list_all(cls, current_collaborater: dict):
        """All contracts"""
        clear_screen()

        contracts = db.query(Contract).all()
        choice = CrudContractView.list_all(contracts)
        if choice == "b":
            return "menu_contract", current_collaborater

        print("[bold red]Saisie non valide[/bold red]")
        return "menu_contract", current_collaborater

    @classmethod
    def update(cls, current_collaborater: dict):
        """Update"""
        contracts = db.query(Contract).all()
        contract_dict = CrudContractView.update(contracts)
        contract = db.query(Contract).get(contract_dict["contract_id"])
        if contract is None:
            print("[bold red]Aucun contract ne correspond à cet id[/bold red]")
            return "menu_contract", current_collaborater
        if contract_dict["field_to_update"] == "3":
            if contract_dict["value"] not in ["1", "2"]:
                print("[bold red]Saisie non valide du statut(1, 2)[/bold red]")
                return "menu_contract", current_collaborater

            setattr(
                contract,
                check_field_to_update(contract_dict["field_to_update"]),
                status_value(contract_dict["value"]),
            )
        db.commit()
        new_contract = db.query(Contract).get(contract_dict["contract_id"])
        print(f"[bold green]Contrat modifié avec succès {new_contract}[/bold green]")

        return "menu_contract", current_collaborater

    @classmethod
    def delete(cls, current_collaborater: dict):
        """Delete"""
        if not is_management(current_collaborater.role):
            print(
                "[bold red]Vous n'êtes pas autorisé à supprimer des contrats[/bold red]"
            )
            return "menu_contract", current_collaborater
        contracts = db.query(Contract).all()
        contract_dict = CrudContractView.delete(contracts)

        if contract_dict["choice"] == "y":
            contract = db.query(Contract).get(contract_dict["contract_id"])
            if contract is None:
                print("[bold red]Ce contrat n'existe pas[/bold red]")
                return "menu_contract", current_collaborater
            print(contract)
            db.delete(contract)
            db.commit()
            print(f"[bold green]{contract.name} supprimé[/bold green]")
            return "menu_contract", current_collaborater
        if contract_dict["choice"] == "n":
            return "menu_contract", current_collaborater
        print("[bold red]Saisie non valide[/bold red]")
        return "menu_contract", current_collaborater
