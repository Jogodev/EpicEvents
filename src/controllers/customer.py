"""Customer controllers"""

import datetime
from src.views.customer import CustomerView, CrudCustomerView
from src.models.customer import Customer
from src.utils.utils import clear_screen
from src.helpers.check_collaborater import check_email
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
    def create(cls, payload: dict):
        """Post"""
        clear_screen()
        customer_dict = CrudCustomerView.create()
        if not check_email(customer_dict["email"]):
            print("[bold red]Email invalide[/bold red]")
            return "create_customer", payload
        new_customer = Customer(
            name=customer_dict["name"],
            email=customer_dict["email"],
            phone=customer_dict["phone"],
            company=customer_dict["company"],
            created_at=datetime.datetime.now().strftime("%d-%m-%Y"),
        )
        db.add(new_customer)
        db.commit()
        print(f"[bold green]Nouveau client {new_customer.name}[/bold green]")
        return "menu_customer", payload

    @classmethod
    def list_all(cls, payload: dict):
        """All customers"""
        clear_screen()
        customers = db.query(Customer).all()
        choice = CrudCustomerView.list_all(customers)
        if choice == "b":
            return "menu_customer", payload
        print("[bold red]Saisie non valide[/bold red]")
        return "menu_customer", payload

    @classmethod
    def update(cls, payload: dict):
        """Update"""
        customers = db.query(Customer).all()
        customer_dict = CrudCustomerView.update(customers)
        customer = db.query(Customer).get(customer_dict["customer_id"])
        if customer is None:
            print("[bold red]Aucun client ne correspond à cet id[/bold red]")
            return "menu_customer", payload

        setattr(customer, customer_dict["key"], customer_dict["value"])
        db.commit()
        new_customer = db.query(Customer).get(customer_dict["customer_id"])
        print(f"[bold green]Client modifié avec succès {new_customer}[/bold green]")

        return "menu_customer", payload

    @classmethod
    def delete(cls, payload: dict):
        """Delete"""
        customers = db.query(Customer).all()
        customer_dict = CrudCustomerView.delete(customers)

        if customer_dict["choice"] == "y":
            customer = db.query(Customer).get(customer_dict["customer_id"])
            if customer is None:
                print("[bold red]Ce contrat n'existe pas[/bold red]")
                return "menu_customer", payload
            print(customer)
            db.delete(customer)
            db.commit()
            print(f"[bold green]{customer.name} supprimé[/bold green]")
            return "menu_customer", payload
        if customer_dict["choice"] == "n":
            return "menu_customer", payload
        print("[bold red]Saisie non valide[/bold red]")
        return "menu_customer", payload
