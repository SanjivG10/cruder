from .constants import SUPPORTS
from .lib import check_value_array
from .error import generate_error_string


def validate_route_to_schema(schema,schemas):
    for sch in schemas:
        for k,_ in sch.items():
            if k==schema:
                return True 
    return False 


def validate_user_input(data):
    name = data.get("name")
    port= data.get("port")
    output_folder = data.get("output")
    entry = data.get("entry")
    auth = data.get("auth",False)

    if auth: 
        raise Exception("auth is not supported currently")

    schemas = data.get("schemas",[])
    routes = data.get("routes",[])


    for route in routes:
        if not all([validate_route_to_schema(route.get("schema"),schemas)  for route in routes]):
            raise Exception(f"{route.get('path')} doesn't match schema")


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
