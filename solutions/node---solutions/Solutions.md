## Exercise 1
No Solution

## Exercise 2
consts.js:
```
const FINANCE = "finance"
	const WEATHER = "weather"
	const EMOTIONS = "emotions"
	

	module.exports.complaints = {
	    FINANCE,
	    WEATHER,
	    EMOTIONS
	}
```
complaintsHandler.js:
```
const c = require("./consts")
	

	const handleComplaints = function(complaint) {
	    if(complaint.type === c.complaints.FINANCE) {
	        return console.log("Money doesn't grow on trees, you know.")
	    } else if (complaint.type === c.complaints.WEATHER) {
	        return console.log("It is the way of nature. Not much to be done.")
	    } else if (complaint.type === c.complaints.EMOTIONS) {
	        return console.log("It'll pass, as all things do, with time.")
	    }
	

	}
	

	module.exports.handleComplaint = handleComplaints
```
complaints.js:
```
const c = require("./consts")
	

	let complaint1 = {
	    text: "I'm not getting enough money",
	    type: c.complaints.FINANCE
	}
	

	let complaint2 = {
	    text: "My salary hasn't come in yet",
	    type: c.complaints.FINANCE
	}
	

	let complaint3 = {
	    text: "I'm always full of energy",
	    type: c.complaints.EMOTIONS
	}
	

	const ch = require("./complaintsHandler")
	

	ch.handleComplaint(complaint1) //should print "Money doesn't grow on trees, you know."
	ch.handleComplaint(complaint2) //should print "Money doesn't grow on trees, you know."
	ch.handleComplaint(complaint3) //should print "It'll pass, as all things do, with time."
```