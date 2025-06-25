## Exercise 1
```
router.get('/sanity', function(req, res) {
	    res.send("Server up and running")
	})
```

## Exercise 2
```
const wordCounter = {}
router.get('/word/:word', function(req, res) {
	    if(wordCounter[req.params.word]) {
	        res.send({count: wordCounter[req.params.word]})
	    } else {
	        res.send({count: 0})
	    }
	

	})
```

## Exercise 3
```
router.post('/word/:word', function(req, res) {
	    
	    if(wordCounter[req.params.word]) {
	        wordCounter[req.params.word]++
	    } else {
	        wordCounter[req.params.word] = 1
	    }
	

	    res.send({text: `Added ${req.params.word}`, currentCount: wordCounter[req.params.word]})
	})
```

## Exercise 4
```
router.post('/words/:sentence', function(req, res) {
	    
	    let words = req.params.sentence.split(" ")
	    let numNewWords = 0
	    let numOldWords = 0
	

	    for(let word of words) {
	        if(wordCounter[word]) {
	            wordCounter[word]++
	            numOldWords++
	        } else {
	            wordCounter[word] = 1
	            numNewWords++
	        }
	    }
	

	    res.send({text: `Added ${numNewWords} words, ${numOldWords} already existed.`, currentCount: -1})
	})
```

## Exercise 5
```
router.get('/total', function(req, res) {
	    const words = Object.keys(wordCounter)
	    let sum = 0
	    
	    for(let word of words) {
	        sum += wordCounter[word]
	    }
	

	    res.send({text: "Total count", count: sum})
	})
```

## Extension 1
No Solution

## Extension 2
No Solution

## Extension 3
No Solution
