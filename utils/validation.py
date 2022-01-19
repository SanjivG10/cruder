from .constants import SUPPORTS
from .lib import check_value_array
from .error import generate_error_string


def validate_user_input(data):

    output_folder = data.get("output")
    entry = data.get("entry")

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
