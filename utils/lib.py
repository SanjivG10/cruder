def check_value_array(value,array):
    return value in array

def get_variable_name_in_camelcase(val):
    output = ''.join([x.title() for x in val.split("-")])
    return (output[0].lower() + output[1:])

def get_js_boolean(val):
    if val==True:
        return "true"
    elif val==False:
        return "false"

    return val 

def get_js_var_dict(v):
    str=""
    for key,value in v.items():
        str+= f"{key}:{get_js_boolean(value)},\n\t\t"

    return str 
