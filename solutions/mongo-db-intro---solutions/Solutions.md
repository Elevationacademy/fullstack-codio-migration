## Exercise 1
```
db.linkedon.count({salary: {$gt: 25000}})
```

## Exercise 2
```
db.linkedon.find({}, {firstName: 1, salary: 1, _id: 0}).sort({salary: -1}).limit(3)
```

## Exercise 3
```
db.linkedon.count({$and: [{salary: {$gte: 7000}}, {"currentCompany.name": "Walmart"}]})
```

## Exercise 4
```
db.linkedon.find({$or: [{"currentCompany.industry": "Sales"}, {"currentCompany.industry": "Retail"}]}, {firstName: 1, lastName: 1, "currentCompany.name": 1, salary: 1, _id: 0}).sort({salary: -1}).limit(1)
```

## Exercise 5
```
db.linkedon.count({$or: [{"currentCompany.name": "Apple"}, {previousCompanies: {$elemMatch: {name: "Apple"}}}]})
```

## Extension 1
```
db.linkedon.aggregate([{$match: {"currentCompany.name": "Apple"}},{$group: {_id: "$currentCompany.industry", count: {$sum: 1}}}])

```

## Extension 2
```
db.linkedon.aggregate([{$match: {currentPosition: "Analyst"}},{$group: {_id: "$currentCompany.name", averageSalary: {$avg: "$salary"}}}])
```

## Extension 3
```
db.linkedon.aggregate([{$match: {$and: [{"currentCompany.industry": "Tech"}, {$or: [{"currentCompany.name": "Apple"}, {"currentCompany.name": "Google"}]}]}},{$group: {_id: "$lastName", averageSalary: {$avg: "$salary"}}}, {$sort: {averageSalary: -1}}])

```