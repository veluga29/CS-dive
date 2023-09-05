const express = require('express');
const app = express();
const path = require('path');
const pt = path.join(__dirname, 'data.json');
const fs = require('fs');
app.get("/", (req, res) => {
    const ret = fs.readFileSync(pt)
    res.json(JSON.parse(ret))
})
app.listen(3000, () => {
    console.log("Server is running on port 3000");
})