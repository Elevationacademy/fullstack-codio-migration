Here is a simple app. A server for NBA players data.

Here is the server configuration file:
```js
const express = require('express')
const path = require('path')
const api = require('./api')
const app = express()

app.use(express.static(path.join(__dirname, 'dist')))
app.use(express.static(path.join(__dirname, 'node_modules')))
app.use(express.json());

app.use('/', api)



const port = 3006
app.listen(port, function () {
    console.log(`Running server on port ${port}`)
})
```

and the routes:

```js
const express = require('express')
const router = express.Router()
const players = require('./players.json')


const teamToIDs = {
    "lakers": "1610612747",
    "warriors": "1610612744",
    "heat": "1610612748",
    "suns": "1610612756"
}

router.get(`/players`, (req, res) => {
    let teamID = teamToIDs[req.params.teamName]
    
    let team = players
        .filter(d => d.teamId === teamID)
        .map(d => { return { firstName: d.firstName, lastName: d.lastName } })
    console.log(team)
    res.send(team) 
})


router.get(`/teams/:teamName`, (req, res) => {
    if (!teamToIDs[req.params.teamName]){
        console.log("id not found")
    }
    res.send(teamToIDs[req.params.teamName]) 
})

router.post('/teams', (req, res) => {
    let teamName = req.body.teamName
    teamToIDs[teamName] = req.body.teamId
    res.status(201).send(teamToIDs)
})


module.exports = router
```

You will need the players data.
You can take it from [this players json](https://github.com/bttmly/nba/blob/master/data/players.json)