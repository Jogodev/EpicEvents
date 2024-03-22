"""Check inputs for contracts"""


def check_field_to_update(field_to_update):
    if field_to_update == "1":
        field_to_update = "contract_price"
    elif field_to_update == "2":
        field_to_update = "left_to_pay"
    elif field_to_update == "3":
        field_to_update = "status"
    return field_to_update


def status_value(value):
    return bool(value == 1)
