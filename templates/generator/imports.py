

from utils.lib import get_variable_name_in_camelcase

def create_imports(dependencies=[]):
    import_str=""
    for dependency in dependencies:
        if dependency=="dotenv":
            continue 
        var_name = get_variable_name_in_camelcase(dependency)
        import_str+=f"import {var_name} from '{dependency}';\n"

    return import_str

