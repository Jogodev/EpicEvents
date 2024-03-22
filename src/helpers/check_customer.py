"""Check inputs customers"""

from src.helpers.check_common import check_email, check_phone


def has_customer(customer):
    bool(customer is not None)


def check_field_to_update(field_to_update):
    if field_to_update == "1":
        field_to_update = "name"
    elif field_to_update == "2":
        field_to_update = "email"
    elif field_to_update == "3":
        field_to_update = "phone"
    elif field_to_update == "4":
        field_to_update = "company"
    return field_to_update


# if customer_dict["field_to_update"] == "3":
#         if check_phone(customer_dict["value"]):
#             print("[bold red]Telephone invalide[/bold red]")
#     if customer_dict["field_to_update"] == "2":
#         if not check_email(customer_dict["value"]):
#             print("[bold red]Email invalide[/bold red]")
#     if customer_dict["field_to_update"] not in ["1", "2", "3", "4"]:
#         print("[bold red]Le champ choisie n'existe pas[/bold red]")
