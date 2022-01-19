def sanitize_data(data):

    framework = data.get("framework","express")
    output = data.get("output","build")
    entry= data.get("entry","src")
    database = data.get("database","mongo")
    orm = data.get("orm","mongoose")
    language = data.get("language","js")

    optional_data = {
        **data,
        "framework":framework,
        "output":output,
        "entry":entry,
        "database":database,
        "orm":orm,
        "language":language
    }

    return  optional_data