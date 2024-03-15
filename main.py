"""Main"""

from src.controllers.main import main_menu_controller
from src.controllers.collaborater import (
    CollaboraterController,
    CrudCollaboraterController,
)
from src.controllers.customer import CustomerController, CrudCustomerController
from src.controllers.contract import ContractController, CrudContractController
from src.controllers.event import EventController, CrudEventController
from src.controllers.auth import auth_controller

controller_dict = {
    # Main
    "main_menu": main_menu_controller,
    # Authentication
    "auth_controller": auth_controller,
    # Collaborater
    "menu_collaborater": CollaboraterController.menu_collaborater_controller,
    "create_collaborater": CrudCollaboraterController.create,
    "get_collaborators": CrudCollaboraterController.list_all,
    "update_collaborater": CrudCollaboraterController.update,
    "delete_collaborater": CrudCollaboraterController.delete,
    # Customer
    "menu_customer": CustomerController.menu_customer_controller,
    "create_customer": CrudCustomerController.create,
    "get_customers": CrudCustomerController.list_all,
    "update_customer": CrudCustomerController.update,
    "delete_customer": CrudCustomerController.delete,
    # Contracts
    "menu_contract": ContractController.menu_contract_controller,
    "create_contract": CrudContractController.create,
    "get_contracts": CrudContractController.list_all,
    "update_contract": CrudContractController.update,
    "delete_contract": CrudContractController.delete,
    # Events
    "menu_event": EventController.menu_event_controller,
    "create_event": CrudEventController.create,
    "get_events": CrudEventController.list_all,
    "update_event": CrudEventController.update,
    "delete_event": CrudEventController.delete,
}


def main():
    """Program start"""
    payload = {}
    string_controller, payload = auth_controller(payload)

    while True:
        controller = controller_dict[string_controller]
        string_controller, payload = controller(payload)


if __name__ == "__main__":
    main()
