import json 
from utils.file import file_exists,create_folder
from utils.validation import validate_user_input
from utils.json import sanitize_data

FILE_NAME = "cruder.json"

def read_json():
    if not file_exists(FILE_NAME):
        raise Exception(f"{FILE_NAME} file not found")
    
    with open(FILE_NAME,"r") as f:
        data = json.load(f)
        data = sanitize_data(data) 

        validate_user_input(data);         

        output = data.get("output")

        create_folder(output)
        entry = data.get("entry")
        create_folder(output+"/"+entry)

        with open(output+"/"+entry+"/"+"index.js","w"):
            pass 


read_json()

