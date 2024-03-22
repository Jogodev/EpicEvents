"""Customer controllers"""

import datetime
from src.views.customer import CustomerView, CrudCustomerView
from src.models.customer import Customer
from src.utils.utils import clear_screen
from src.helpers.check_customer import check_field_to_update, has_customer
from src.helpers.check_common import check_email, check_phone
from src.helpers.permissions import is_sale
from rich import print
from config import db


class CustomerController:
    """Menu customer"""

    @classmethod
    def menu_customer_controller(cls, payload: dict):
        """Menu customer"""
        choice = CustomerView.menu_customer_view()
        if choice == "1":
            return "create_customer", payload
        if choice == "2":
            return "get_customers", payload
        if choice == "3":
            return "update_customer", payload
        if choice == "4":
            return "delete_customer", payload
        if choice == "b":
            return "main_menu", payload

        print("\nSaisie non valide\n")
        return "menu_customer", payload


class CrudCustomerController:
    """Crud customer controller"""

    @classmethod
    def create(cls, current_collaborater: dict):
        """Post"""
        if not is_sale(current_collaborater.role):
            print("[bold red]Vous n'êtes pas autorisé à ajouter des clients[/bold red]")
            return "menu_customer", current_collaborater
        customer_dict = CrudCustomerView.create()
        if not check_email(customer_dict["email"]):
            print("[bold red]Email invalide[/bold red]")
            return "menu_customer", current_collaborater
        if not check_phone(customer_dict["phone"]):
            print("[bold red]Telephone invalide[/bold red]")
            return "menu_customer", current_collaborater
        new_customer = Customer(
            name=customer_dict["name"],
            email=customer_dict["email"],
            phone=customer_dict["phone"],
            company=customer_dict["company"],
            created_at=datetime.datetime.now().strftime("%d-%m-%Y"),
            collaborater_id=current_collaborater.id,
        )
        db.add(new_customer)
        db.commit()
        print(f"[bold green]Nouveau client {new_customer.name}[/bold green]")
        return "menu_customer", current_collaborater

    @classmethod
    def list_all(cls, current_collaborater: dict):
        """All customers"""
        clear_screen()
        customers = db.query(Customer).all()
        choice = CrudCustomerView.list_all(customers)
        if choice == "b":
            return "menu_customer", current_collaborater
        print("[bold red]Saisie non valide[/bold red]")
        return "menu_customer", current_collaborater

    @classmethod
    def update(cls, current_collaborater: dict):
        """Update"""

        if not is_sale(current_collaborater.role):
            print(
                "[bold red]Vous n'êtes pas autorisé à modifier des clients[/bold red]"
            )
            return "menu_customer", current_collaborater
        customers = db.query(Customer).all()
        customer_dict = CrudCustomerView.update(customers)
        customer = db.query(Customer).get(customer_dict["customer_id"])
        if customer is None:
            print("[bold red]Aucun client ne correspond à cet id[/bold red]")
            return "menu_customer", current_collaborater
        if customer_dict["field_to_update"] == "2":
            if not check_email(customer_dict["value"]):
                print("[bold red]Email invalide[/bold red]")
                return "menu_customer", current_collaborater
        if customer_dict["field_to_update"] == "3":
            if not check_phone(customer_dict["value"]):
                print("[bold red]Téléphone invalide[/bold red]")
                return "menu_customer", current_collaborater
        setattr(
            customer,
            check_field_to_update(customer_dict["field_to_update"]),
            (customer_dict["value"]),
        )
        db.query(Customer).filter(Customer.id == customer_dict["customer_id"]).update(
            {Customer.updated_at: datetime.datetime.now().strftime("%d-%m-%Y")}
        )
        db.commit()
        new_customer = db.query(Customer).get(customer_dict["customer_id"])
        print(f"[bold green]Client modifié avec succès {new_customer}[/bold green]")

        return "menu_customer", current_collaborater

    @classmethod
    def delete(cls, current_collaborater: dict):
        """Delete"""
        if not is_sale(current_collaborater.role):
            print(
                "[bold red]Vous n'êtes pas autorisé à supprimer des clients[/bold red]"
            )
            return "menu_customer", current_collaborater
        customers = db.query(Customer).all()
        customer_dict = CrudCustomerView.delete(customers)

        if customer_dict["choice"] == "y":
            customer = db.query(Customer).get(customer_dict["customer_id"])
            if customer is None:
                print("[bold red]Ce contrat n'existe pas[/bold red]")
                return "menu_customer", current_collaborater
            print(customer)
            db.delete(customer)
            db.commit()
            print(f"[bold green]{customer.name} supprimé[/bold green]")
            return "menu_customer", current_collaborater
        if customer_dict["choice"] == "n":
            return "menu_customer", current_collaborater
        print("[bold red]Saisie non valide[/bold red]")
        return "menu_customer", current_collaborater
