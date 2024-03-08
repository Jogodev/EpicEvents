"""Main"""

from src.controllers.main import main_menu_controller
from src.controllers.collaborater import (
    CollaboraterController,
    CrudCollaboraterController,
)
from src.controllers.customer import CustomerController, CrudCustomercontroller
from src.controllers.contract import ContractController
from src.controllers.event import EventController

controller_dict = {
    # Main
    "main_menu": main_menu_controller,
    # Collaborater
    "menu_collaborater": CollaboraterController.menu_collaborater_controller,
    "create_collaborater": CrudCollaboraterController.create,
    "get_collaborater": CrudCollaboraterController.get,
    # Customer
    "menu_customer": CustomerController.menu_customer_controller,
    "create_customer": CrudCustomercontroller.create,
    "get_customer": CrudCustomercontroller.get,
    # Contracts
    "menu_contract": ContractController.menu_contract_controller,
    # Events
    "menu_event": EventController.menu_event_controller,
}


def main():
    """Program start"""
    payload = dict()
    string_controller, payload = main_menu_controller(payload)

    while True:
        controller = controller_dict[string_controller]
        string_controller, payload = controller(payload)


if __name__ == "__main__":
    main()
