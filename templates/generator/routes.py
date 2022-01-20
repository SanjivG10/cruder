
from templates.routes import generate_delete_route, generate_get_route, generate_index_route, generate_post_route, generate_put_route, generate_route_header
from utils.constants import ALL_ROUTES

def create_routes(data,ext=".js"):

    # generate index file 

    routes = data.get("routes")
    for route in routes:
        path = route.get("path")
        auth = route.get("auth",False)
        crud = route.get("crud",ALL_ROUTES)
        schema = route.get("schema")
        if crud=="all":
            crud = ALL_ROUTES 

        code = generate_route_header(route,data)

        required_schema = {}
        for user_schemas in data.get("schemas"):
            for name,_ in user_schemas.items():
                if name==schema:
                    required_schema =user_schemas 
                    break 

        for each_crud in crud:
            each_crud = each_crud.upper()
            
            if each_crud=="GET":
                code+=generate_get_route(auth)
            if each_crud=="POST":
                code+=generate_post_route(required_schema,auth)
            if each_crud=="DELETE":
                code+= generate_delete_route(auth)
            if each_crud=="PUT":
                code+=generate_put_route(required_schema,auth)

        

        code+="module.exports = router"

        with open(schema+ext,"w") as f:
            f.write(code) 

    
    with open("index"+ext,"w") as f:
        index_route = generate_index_route(routes)
        f.write(index_route)

