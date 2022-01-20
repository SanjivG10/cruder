def get_database_string():
    return  """\n \n(async () => {
    try {
        await mongoose.connect(process.env.MONGODB_URL)
        console.log("Connection with database success")
    }
    catch (err) {
        console.log("Connection with mongoose failed")
    }
})()"""