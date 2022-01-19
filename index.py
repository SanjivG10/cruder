import json 
from utils.file import file_exists,create_folder,create_file
from utils.validation import validate_user_input
from utils.json import sanitize_data
import os 
from templates.env import create_env_str

FILE_NAME = "cruder.json"

def read_json():
    if not file_exists(FILE_NAME):
        raise Exception(f"{FILE_NAME} file not found")
    
    with open(FILE_NAME,"r") as f:
        data = json.load(f)
        data = sanitize_data(data) 

        validate_user_input(data)

        output = data.get("output")
        create_folder(output)

        # create .env file
        env_file = data.get("env")
        with open(output+"/"+".env","w") as f:
            db_url = data.get("db_url")
            port = data.get("port")
            env_str = create_env_str(db_url,port)
            f.write(env_str)

        entry_file = data.get("entry_file")
        entry_file_name  = os.path.join(output,entry_file)+".js"

        entry = data.get("entry")
        entry_folder = os.path.join(output,entry)
        create_folder(entry_folder)

        create_file(entry_file_name)


read_json()

