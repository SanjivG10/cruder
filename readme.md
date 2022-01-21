- [Introduction](#introduction)
- [Pre-Requisite](#pre-requisite)
- [Features](#features)
- [TODO](#todo)
- [Options](#options)



# Introduction 
🔥CRUDer🔥 is a simple application written in Python that generates simple CRUD (Create, Read, Update, Delete) routes for NodeJS. 

                      💲 PR's are absolutely welcome 💲


# Pre-Requisite 
 - ❗ Python (I mean you are running python app)
 - ❗ NodeJS (inorder to run the generated application)
 - ❗ MongoDB (create mongodb and database name)
 - ❗ NPM (Install npm packages)

# Features 

1.  🔴 Supports CRUD with mongo database (mongoose), express router and es6 syntax 
2.  🔴 Folder structure options with installation of dependencies.  
3.  🔴 Easy to understand code.
4.  🔴 No use of external libraries (might need some on future enhancements)
5.  🔴 Easy to run 
6.  🔴 Settings are passed through .json file. 
7.  🔴 Manchester United 


# TODO
- Create curder.json with required [options](#options)
- > python3 index.py 
- > node --es-module-specifier-resolution=node build/index.js  # need this option to make sure importing could be done without babel


# Options

``` 

    "name": Your project name

    "install": Install required dependencies after creation

    "framework": "express" (supported right now)

    "database": "mongo" (supported right now)

    "orm": "mongoose" (supported right now)

    "output": output folder name 

    "entry": folder name for main application (eg: "src")

    "language": "js" (supported right now)

    "module": "es6" (supported right now) 

    "env": env file name 

    "db_url": MongoDB URL with your database name 

    "port" : Port where you run your server 

    "entry_file":  main file name that sits on the top (index.js)

    "route_folder": folder name for your routes 

    "schema_folder": folder name for your schemas 

    "schema": schema definition. [<name>: <fields>]
        name: name of your schema 
        fields: {   
            "name": name of the field 
            "type": type of the field
            "additional": every other field requirements 
        }

        ⚠️ eg: schemas : [{
            "account": [
                {
                    "name": "password",
                    "type": "String",
                    "additional": {
                        "unique": true,
                        "trim": true
                    }
                }
            ]}]

    "routes": route information [<field>:<field>]
        field: {
            "path": route path. Must start with /
            "auth": false. (adding auth middleware option is limited as of now)
            "crud": "all" or any of ["GET","POST","DELETE","PUT"],
            "schema": which schema to use from above settings. 
        }

        ⚠️ eg: "routes": [{
            
            "path": "/account",
            "crud": "all",
            "schema": "account
            },
            {
    
            "path": "/token",
            "crud": [
                "GET",
                "DELETE"
            ],
            "schema": "token"
            }]

    
    

```

