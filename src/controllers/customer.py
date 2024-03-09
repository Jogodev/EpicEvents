from src.views.customer import CustomerView, CrudCustomerView
from src.models.customer import Customer
from src.utils.utils import clear_screen
from src.helpers.check import check_email
from rich import print
from config import db
import datetime


class CustomerController:
    def menu_customer_controller(payload):

        choice = CustomerView.menu_customer_view()
        if choice == "1":
            return "create_customer", payload
        elif choice == "2":
            return "get_customers", payload
        elif choice == "b":
            return "main_menu", payload
        else:
            print("\nSaisie non valide\n")
            return "menu_customer", payload


class CrudCustomercontroller:

    def create(payload):

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

    def list_all(payload):

        clear_screen()

        customers = db.query(Customer).all()
        choice = CrudCustomerView.list_all(customers)
        if choice == "b":
            return "menu_customer", payload
        else:
            print("[bold red]Saisie non valide[/bold red]")
            return "menu_customer", payload
