"""Main"""

from src.controllers.main import main_menu_controller
from src.controllers.collaborater import (
    CollaboraterController,
    CrudCollaboraterController,
)
from src.controllers.customer import CustomerController, CrudCustomercontroller
from src.controllers.contract import ContractController, CrudContractController
from src.controllers.event import EventController, CrudControllerEvent

controller_dict = {
    # Main
    "main_menu": main_menu_controller,
    # Collaborater
    "menu_collaborater": CollaboraterController.menu_collaborater_controller,
    "create_collaborater": CrudCollaboraterController.create,
    "get_collaborators": CrudCollaboraterController.list_all,
    "update_collaborater": CrudCollaboraterController.update,
    "delete_collaborater": CrudCollaboraterController.delete,
    # Customer
    "menu_customer": CustomerController.menu_customer_controller,
    "create_customer": CrudCustomercontroller.create,
    "get_customers": CrudCustomercontroller.list_all,
    "delete_customer": CrudCustomercontroller.delete,
    # Contracts
    "menu_contract": ContractController.menu_contract_controller,
    "create_contract": CrudContractController.create,
    "get_contracts": CrudContractController.list_all,
    "delete_contract": CrudContractController.delete,
    # Events
    "menu_event": EventController.menu_event_controller,
    "create_event": CrudControllerEvent.create,
    "get_events": CrudControllerEvent.list_all,
    "delete_event": CrudControllerEvent.delete,
}


def main():
    """Program start"""
    payload = {}
    string_controller, payload = main_menu_controller(payload)

    while True:
        controller = controller_dict[string_controller]
        string_controller, payload = controller(payload)


if __name__ == "__main__":
    main()
