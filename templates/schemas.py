
from utils.lib import get_js_var_dict


def generate_schemas_header(orm="mongoose",module="es5"):
    code= f"const {orm} = require('{orm}');"
    code+=f"\nconst {{Schema}} = mongoose;\n\n"; 
    return code 

def generate_schemas_footer(name,module="es5"):
    code=f"\nmodule.exports = {name}"
    return code 



def get_schema(schema):
    name = schema.get("name")
    type = schema.get("type")
    additional = schema.get("additional",{})
    schema_defs = {**additional,"type": type} 

    return f"""
        {name}: {{ 
                {get_js_var_dict(schema_defs)}}}
    """

def get_schema_string(fields,var_name="schema"):
    code=f"""const {var_name} = new Schema({{
        {','.join([get_schema(schema_str) for schema_str in fields])}
    }})""" 

    return code 

