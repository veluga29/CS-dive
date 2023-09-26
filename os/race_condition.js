const path = require('path');
const pt = path.join(__dirname, 'shared.json');

let ret = JSON.parse(fs.readFileSync(pt))
ret.num -= 1000
setTimeout(() => {
    fs.writeFileSync(pt, JSON.stringify(ret))
}, 3000)