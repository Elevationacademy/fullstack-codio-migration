// Do not modidy these lines of code -->
const turnToKing = function(name, money){
    name = name.toUpperCase()
    money = increaseByNameLength(money, name)
    name = makeRegal(name)

    return(name + " has " + money + " gold coins")
}
// --<

// Write your code here -->


const makeRegal = (name) => "His Royal Highness, " + name

	
const increaseByNameLength = (money, name) => name.length * money



