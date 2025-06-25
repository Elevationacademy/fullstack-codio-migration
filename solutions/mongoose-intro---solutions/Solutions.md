## Exercise 1
```
router.post('/person', function(req, res) {
	    let person = req.body
	    let p1 = new Person({
	        firstName: person.firstName,
	        lastName: person.lastName,
	        age: person.age
	    })
	    
	    p1.save()
	    res.end()
	})
```

## Exercise 2
```
router.put('/person/:id', function(req, res) {
	    let id = req.params.id
	    Person.findByIdAndUpdate(id, {age: 80}, function(err, person) {
	        res.end()
	    })
	})
```

## Exercise 3
```
router.delete('/apocalypse', function(req, res) {
	

	    Person.find({}, function(err, people) {
	        people.forEach(p => p.remove())
	    })
	

	    res.end()
	})
```
