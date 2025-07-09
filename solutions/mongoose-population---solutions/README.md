# Solutions

## Exercise 1
```
const solarSystemSchema = new Schema({
	    planets: [{type: Schema.Types.ObjectId, ref: 'Planet'}],
	    starName: String
	})
	

	const planetSchema = new Schema({
	    name: String,
	    system: {type: Schema.Types.ObjectId, ref: 'SolarSystem'},
	    visitors: [{type: Schema.Types.ObjectId, ref: 'Visitor'}]
	})
	

	const visitorSchema = new Schema({
	    name: String,
	    homePlanet: {type: Schema.Types.ObjectId, ref: 'Planet'},
	    visitedPlanets: [{type: Schema.Types.ObjectId, ref: 'Planet'}]
	})
	

	const SolarSystem = mongoose.model("SolarSystem", solarSystemSchema)
	const Planet = mongoose.model("Planet", planetSchema)
	const Visitor = mongoose.model("Visitor", visitorSchema)
	

	let ss = new SolarSystem({
	    planets: [],
	    starName: "Soya Way"
	})
	

	let p1 = new Planet({
	    name: "Earthy",
	    system: ss,
	    visitors: []
	})
	

	let p2 = new Planet({
	    name: "Marsy",
	    system: ss,
	    visitors: []
	})
	

	let p3 = new Planet({
	    name: "Uranusy",
	    system: ss,
	    visitors: []
	})
	

	let v1 = new Visitor({
	    name: "Mr mars",
	    homePlanet: p2,
	    visitedPlanets: []
	})
	

	let v2 = new Visitor({
	    name: "Mr Uranus",
	    homePlanet: p3,
	    visitedPlanets: []
	})
	

	/* ss.planets.push(p1)
	ss.planets.push(p2)
	ss.planets.push(p3)
	
	v1.visitedPlanets.push(p3)
	v1.visitedPlanets.push(p1)
	
	p1.visitors.push(v1)
	p3.visitors.push(v1)
	
	v2.visitedPlanets.push(p1)
	p1.visitors.push(v2)
	
	ss.save()
	
	p1.save()
	p2.save()
	p3.save()
	
	v1.save()
	v2.save() */
	

	//Find a visitor's list of visited planets
	/* Visitor.findOne({}).populate("visitedPlanets").exec(function(err, visitor) {
	    visitor.visitedPlanets.forEach(vp => console.log(vp.name))
	}) */
	

	

	//Find all the visitors on a planet
	/* Planet.findOne({}).populate("visitors").exec(function(err, planet) {
	    planet.visitors.forEach(v => console.log(v.name))
	}) */
	

	//Find all the visitors in a system (subdocuments!)
	/* SolarSystem.findOne({}).populate({
	        path: "planets",
	        populate: {
	            path: "visitors"
	        }
	    }).exec(function (err, solarSystem){
	        
	        for(planet of solarSystem.planets) {
	            planet.visitors.forEach(v => console.log(v.name))
	        }
	    }) */
	

	

	//Find the name of the star in the system of a visitor's home planet
	/* Visitor.findOne({}).populate({
	    path: "homePlanet",
	    populate: {
	        path: "system",
	    }
	}).exec(function(err, visitor) {
	    console.log(visitor.homePlanet.system.starName)
	}) */
	

	//Find a planet's system's star name as well as its visitors
	

	/* Planet.findOne({}).populate("system visitors").exec(function(err, planet) {
	    console.log(planet.system.starName)
	    planet.visitors.forEach(v => console.log(v.name))
	}) */
	

	Planet.findOne({}).populate({
	    path: "system visitors",
	    populate: {
	        path: "homePlanet"
	    }
	}).exec(function(err, planet) {
	    planet.visitors.forEach(v => console.log(v.homePlanet.name))
	})
```