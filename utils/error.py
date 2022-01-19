from .constants import SUPPORTS

def generate_error_string(name):
    return f"{name} not supported. Make sure you supplied one of [{(',').join(SUPPORTS.get(name))}]"