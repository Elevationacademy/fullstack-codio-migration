# Solutions

## Exercise 1

```
  const emailCompany = users.map(u => {return {email: u.email, companyName: u.company.name}})
```


## Exercise 2

```
const zipCodeFive = users.filter(u => u.address.zipcode[0] === "5")
```


## Exercise 3

```
const zipCodeFiveId = users.filter(u => u.address.zipcode[0] === "5")
	    .map(u => u.id)
```


## Exercise 4

```
const names = users.map(u => u.name)
	    .filter(n => n[0].toLowerCase() === "c")
```


## Exercise 5

```
const doesAllLiveSC = users.every(u => u.address.city === "South Christy")
```


## Exercise 6

```
const findUser = suite => console.log(users.find(u => u.address.suite === suite).company.name)
```


## Exercise 7

```
const printInfo = user => console.log(`${user.name} lives in ${user.address.city}, and owns the company ${user.company.name}`) users.forEach(printInfo)
```