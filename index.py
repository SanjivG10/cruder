import json
from templates.generator.schemas import create_schemas
from templates.generator.routes import create_routes
from utils.file import file_exists,create_folder
from utils.validation import validate_user_input
from utils.json import sanitize_data
import os 
from templates.env import create_env_str
from utils.constants import DEPENDENCIES 
from templates.entry import create_entry_file


FILE_NAME = "cruder.json"

def create_crud():
    if not file_exists(FILE_NAME):
        raise Exception(f"{FILE_NAME} file not found")

    
    with open(FILE_NAME,"r") as f:
        data = json.load(f)
        data = sanitize_data(data) 

        ext ="."+ data.get("language")

        validate_user_input(data)

        output = data.get("output")  #/build 
        create_folder(output)
        os.chdir(output)


        env_file = data.get("env")
        with open(env_file,"w") as f:
            db_url = data.get("db_url")
            port = data.get("port")
            env_str = create_env_str(db_url,port)
            f.write(env_str)

        entry_file = data.get("entry_file")
        create_entry_file(entry_file,data,dependencies=DEPENDENCIES) 

        entry = data.get("entry")
        create_folder(entry)

        os.chdir(entry)

        route_folder = data.get("route_folder")
        create_folder(route_folder)

        schema_folder = data.get("schema_folder")
        create_folder(schema_folder)
        os.chdir(schema_folder)
        create_schemas(data.get("schemas"))
        
        os.chdir(".."+"/"+route_folder)
        create_routes(data)

        # lets create package.json folder

        os.chdir("../../")
        os.system(f"npm init -y")

        package = {}
        with open("package.json","r") as f:
            package = json.load(f)
            package["name"] = data.get("name")
            package["main"] = data.get("entry_file")+ext
        
        with open("package.json","w") as f:
            json.dump(package,f)

        if data.get("install"):
            os.system(f"npm install {' '.join(DEPENDENCIES)}")


create_crud()

