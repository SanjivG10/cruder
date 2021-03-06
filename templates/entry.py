from templates.generator.database import get_database_string
from .generator import imports
import os 

def create_entry_file(filename,data,ext=".js",dependencies=[]): 
    code = ""
    import_string = imports.create_imports(dependencies)
    route_path = os.path.join(data.get("entry"),data.get("route_folder"))
    port = data.get("port")

    file_name = filename + ext
    code +=import_string

    code+="\nimport dotenv from 'dotenv';\n"
    code+="dotenv.config()\n"

    route_variable_name = "api"
    code+=f"\nimport {route_variable_name} from './{route_path}';"
    code+="\nconst app = express();"
    code+="\napp.use(bodyParser.json());"
    code+=f"\n\napp.use('/',{route_variable_name});"
    code+=f"\nconst port = process.env.PORT || {port};"
    code+= get_database_string(data.get("db_url"))
    code+= f"""\n\napp.listen(port, () => {{ 
        console.log('App listening at http://localhost:{port}')
}})
    """

    with open(file_name,"w") as f:
        f.write(code)

