const express = require('express')
const app = express()
const port = 80
const fs = require('fs')
app.get('/', (req, res) => {
    const f = JSON.parse(fs.readFileSync("puppy.json", {
        encoding: "utf8"
    }))
    const puppy = {
        "species": f.species
    }
    res.send(puppy)
})

app.listen(port, () => {
    console.log(`http://127.0.0.1:${port}`)
})