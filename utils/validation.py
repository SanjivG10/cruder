from .constants import SUPPORTS
from .lib import check_value_array
from .error import generate_error_string


def validate_user_input(data):
    name = data.get("name")
    port= data.get("port")
    output_folder = data.get("output")
    entry = data.get("entry")

    if not isinstance(port, int):
        raise Exception("port number is not a number")

    if not name.isalnum():
        raise Exception("Bad project name. Make sure it is alphanumeric")

    output_folder_check = output_folder.isalnum()
    if not output_folder_check:
        raise Exception("Bad output file name. Make sure it is alphanumeric")

    entry= entry.isalnum()
    if not entry:
        raise Exception("Bad entry file name. Make sure it is alphanumeric")

    keys = list(SUPPORTS.keys())

    for key in keys:
        is_key_valid = check_value_array(data.get(key),SUPPORTS.get(key))
        if not is_key_valid:
            error = generate_error_string(key)
            raise Exception(error)
