STRING = f"""
const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require("body-parser");
const apiRoutes = require("./src/routes");

require('dotenv').config()

const app = express();
app.use(bodyParser.json());

app.use("/", apiRoutes)

const port = process.env.PORT || 8000;

(async () => {
    try {
        await mongoose.connect(process.env.MONGODB_URL)
        console.log("Connection with DB success")
    }
    catch (err) {
        console.log("Connection with mongoose failed")
    }
})()


app.listen(port, () => {
    console.log(`App listening at http://localhost:${port}`)
})
"""