# Solutions

## Exercise 1

```
       get restPopulation() {
	        let totalPeople = 0
	        this.reservations.forEach(r => {
	            if(!r.completed && r.seated) {
	                totalPeople += parseInt(r.numPeople)
	            }
	        })
	        return totalPeople
	    }
	    get completedTables() {
	        let totalTables = 0
	        this.reservations.forEach(r => r.completed ? totalTables+= 1 : null)
	        return totalTables
	    }
	    addRes = (name, numPeople) => {
	        this.reservations.push(new Reservation(name, numPeople))
	    }
	    completeRes = (id) => {
	        this.reservations.find(r => r.id === id).completed = true
	    }

```


## Exercise 2

```
export class RestaurantStore {
    
    get totalReservations() { //automatically calculates the total reservationsreturn this.reservations.length
    }
    get openTables() { //automatically caluclates the number of tables avalible, only when the state is affectedlet counter = 0this.reservations.forEach(r => r.seated ? counter ++: null)return (this.numTables - counter)
    }
    get restPopulation() {
        let totalPeople = 0this.reservations.forEach(r => {
            if(!r.completed && r.seated) {
                totalPeople += parseInt(r.numPeople)
            }
        })
        return totalPeople
    }


    get completedTables() {
        let counter = 0this.reservations.forEach(r => r.completed ? counter ++: null)
        return counter


    }
    addRes = (name, numPeople) => {
        this.reservations.push(new Reservation(name, numPeople))
    }
    seatRes = (id) => {
        const reservation = this.reservations.find(r => r.id === id)
        reservation.seated = true
    }
    completeRes = (id) => {
        const reservation = this.reservations.find(r => r.id === id)
        reservation.completed = true
    }
}
```

```
class Restaurant extends Component{
    addRes = () => {
        let name = this.props.GeneralStore.name
        let num = this.props.GeneralStore.numPeople
        this.props.RestaurantStore.addRes(name, num)
    }
    render () {
        return (
            <div><span>You have {this.props.RestaurantStore.openTables} open tables</span><div>There are <span id="restPop">{this.props.RestaurantStore.restPopulation}</span> people in the restaurant</div><div><span id="completedTables">{this.props.RestaurantStore.completedTables}</span> tables have been served today</div><ResInput/><button id="addRes" onClick={this.addRes}>Add Reservation</button> 
                <div className = "reservations">
                    {this.props.RestaurantStore.reservations.map((r, i) => <Reservation res = {r} key={i}/>)}
                </div></div>
        )
    }
}
```

```
class Reservation extends Component {
    completeRes = (e) => {
        this.props.RestaurantStore.completeRes(e.target.id)
    }


    seatRes = (e) => {
        this.props.RestaurantStore.seatRes(e.target.id)
    }
    render() {
        let res = this.props.res
        return (
            <div>
                {res.name} : {res.numPeople}
                <button className="completeRes"
                    id={res.id}
                    onClick={this.completeRes}>
                    Complete Reservation </button>
                <button
                    id={res.id}
                    onClick={this.seatRes}>
                    Seat Reservation </button>
            </div>
        )
    }
}
```


## Exercise 3

```
render() {
        let res = this.props.res
        return (
            <div
                className={res.completed ? "conditional" : null}>
                {res.name} : {res.numPeople}
                <button className="completeRes"
                    id={res.id}
                    onClick={this.completeRes}>
                    Complete Reservation </button>
                <button
                    id={res.id}
                    onClick={this.seatRes}>
                    Seat Reservation </button>
            </div>
        )
}
```