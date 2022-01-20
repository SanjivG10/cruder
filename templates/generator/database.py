def get_database_string(db_url):
    return  f"""\n \n(async () => {{
    try {{
        await mongoose.connect(process.env.MONGODB_URL||'{db_url}')
        console.log("Connection with database success")
    }}
    catch (err) {{
        console.log("Connection with mongoose failed")
    }}
    }})()"""