
def generate_route_header(route,data):

    schema_folder = data.get("schema_folder")
    schema = route.get("schema")

    code="const router = require('express').Router()\n"
    code+= f"const model = require('./../{schema_folder}/{schema}')\n \n"

    return code

def generate_get_route(auth=False):
    code=f"""\nrouter.get("/",[{'auth' if auth else ""}],async(req,res)=>{{
        try{{
            const data = await model.find();
            return res.send({{data}}) 
        }}
        catch(err){{
            return res.status(400).send({{err: err.message}})
        }}
    }})\n\n\n
    """

    return code 


def generate_post_route(schema,auth=False):
    field_names= []
    schema_name = "data" 
    for name,schema_props in schema.items():
        schema_name = name
        field_names = [schema_prop.get("name") for schema_prop in schema_props]

    code=f"""\nrouter.post("/",[{'auth' if auth else ""}],async(req,res)=>{{
        try {{
            const {{ {' ,'.join(field_names)} }} = req.body;  // this is for future usages 
            const {schema_name}Model = new model(req.body);
            const new{schema_name.title()} = await {schema_name}.save();

            return res.send({{data: new{schema_name.title()}}}); 
        }}
        catch(err){{
            return res.status(400).send({{
                err: err.message
            }})
            
        }}
    }})\n\n\n
    """

    return code 

def generate_put_route(schema,auth=False):
    field_names= []
    schema_name = "data" 
    for name,schema_props in schema.items():
        schema_name = name
        field_names = [schema_prop.get("name") for schema_prop in schema_props]

    code=f"""\nrouter.put("/:id",[{'auth' if auth else ""}],async(req,res)=>{{
    try {{
        const {{id}} = req.params; 
        const {{ {" ,".join(field_names)} }} = req.body;
        const updated{schema_name.title()} = await model.findOneAndUpdate({ "id"}, req.body, {{
            new: true
        }})

        return res.send({{ data: updated{schema_name.title()} }})
    }}  

    catch(err) {{
        return res.status(400).send({{
            err: err.message
        }})

    }}  
    }})\n\n\n
    """
    return code 

def generate_delete_route(auth=False):

    code=f"""\nrouter.delete("/:id",[{'auth' if auth else ""}],async(req,res)=>{{
    try {{
        const {{id}} = req.params; 
        const del = await model.findOneAndDelete({{{"id"}}});

        if (!del) {{
            return res.status(400).send({{ data: "Something went wrong while deleting" }})
        }}

        return res.send({{ data: 'deleted' }});
    }}  

    catch(err) {{
        return res.status(400).send({{
            err: err.message
        }})

    }}  
    }})\n\n\n
    """
    return code 


def generate_index_route(routes):

    code = "const router = require('express').Router();\n\n"
    for route in routes:
        name= route.get("schema")
        code+=f"const {name} = require('./{name}')\n"

    code +="\n"*3
    for route in routes:
        code+=f"router.use('{route.get('path')}',{route.get('schema')})\n"

    code+="\n\nmodule.exports = router"

    return code 
     


# router.use("/accounts", account);
# router.use("/wallet-address", walletAddress);
# router.use("/token", token);
# router.use("/transaction", transaction);
# router.use("/blacklist", auth, blacklist);
# router.use("/site-settings", auth, siteSettings);
# router.use("/create-token", jwtToken);

# module.exports = router; 
