def sanitize_data(data):

    name = data.get("name","app")
    port= data.get("port",8000)
    framework = data.get("framework","express")
    output = data.get("output","build")
    entry= data.get("entry","src")
    database = data.get("database","mongo")
    orm = data.get("orm","mongoose")
    language = data.get("language","js")
    entry_file = data.get("entry_file","index")
    module = data.get("module","es5")
    env= data.get("env",".env")
    db_url= data.get("db_url",f"mongodb://localhost:27017/{name}")
    route_folder = data.get("route_folder","routes")
    schema_folder= data.get("schema_folder","schemas")
    schemas = data.get("schemas",[]) 


    sanitized_data = {
        **data,
        "framework":framework,
        "output":output,
        "entry":entry,
        "database":database,
        "orm":orm,
        "language":language,
        "entry_file":entry_file,
        "module": module,
        "env":env,
        "db_url": db_url,
        "route_folder": route_folder,
        "schema_folder":schema_folder,
        "schemas": schemas,
        "port":port
    }

    return  sanitized_data