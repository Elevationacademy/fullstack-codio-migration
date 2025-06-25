
## Exercise 1 - setup
    
Sequelize has its own set of syntax you can use to avoid using raw SQL commands on node, and generally this is the preferred way of working.
    

However, because many companies still use raw SQL a lot, we prefer that you hone this skill some more instead of learning another separate tool.
    
      
----------
    
**Exercise Brief**
    
**PokeCorp** is a company that tracks pokemon and their trainers around the world.
    
      
Until this day, they've been storing all their data together, in a [single JSON file](https://github.com/Elevationacademy/raw-pokemon-trainer-json/blob/master/poke_data.json) that looks like this:
    
      
```
[{
        "id": <pokemon_id>,
        "name": <pokemon_name>,
        "type": <pokemon_type>,
        "height": <pokemon_height>,
        "weight": <pokemon_weight>,
        "ownedBy": [
          {name: <trainer_name>, town: <trainer_town>},
          ...
        ]
    },
    ...
]
```    
      
The file has 151 pokemon in it. Each pokemon has some data, as well as an `ownedBy` field.
    
The `ownedBy` field is an array of objects, where each object represents a trainer that owns this pokemon - note that this array might be empty.
    
      
You don't know exactly how many there are, but you know there are fewer than 50 trainers. Of course, each trainer can own more than one pokemon.
    
      
Likewise, you don't know how many pokemon types there are, but you know it is fewer than 151.
    
      
**PokeCorp** has hired you and a Senior Database Administrator (DBA) to **migrate their data to an SQL database**.
    
      
The DBA is very busy, and she left you with pretty much the entire task, and the following notes:
    
      
Create the following tables:
    
-   `pokemon` - the `PRIMARY KEY` for this should be the pokemon's ID
-   `pokemon_type`
-   `trainer`
-   `town`
-   `pokemon_trainer` - this should be a **join table** of only pokemon and trainer IDs
    
      
Each table, except the `pokemon_trainer` table should have a unique ID that is its `PRIMARY_KEY`
    
----------
    
      
You should create the tables using plain SQL (in some `.sql` file), and then do all the `INSERT`s in node using the `sequelize` package.
    
      
Once you're done, write functions for the following queries.
    
      
    
----------
    
      
For the following queries, **the query itself should be in SQL**, but the wrapping function in node. Obviously, use `sequelize`
    

## Exercise 2
    
Write a function that returns the heaviest pokemon (the one with the biggest `weight` property) - the [MAX command](https://dev.mysql.com/doc/refman/8.0/en/example-maximum-column.html) will help you here. You should find that `Snorlax` is the heaviest.
    

## Exercise 3

Write a function that receives a pokemon type, and returns all of the pokemon names with that type.
    
      
    
For instance, `findByType("grass")` should return `["bulbasaur", "ivysaur", "venusaur", "oddish", ...]`
    

## Exercise 4
    
    
Write a function that receives the name of a pokemon, and returns the names of all the trainers that own it, or an empty array if no one owns it.
    
          
For instance, `findOwners("gengar")` should return `["Misty", "Wallace", "Gary", "Plumeria"]`
    

## Exercise 5
    
Write a function that receives the name of a trainer, and returns the names of all the pokemon he or she owns.
    
          
For instance, `findRoster("Loga")` should return `["metapod", "raticate", "spearow", "pikachu", "machoke", "machamp", "weepinbell", "cloyster", "kabuto"]`
    

    
## Exercise 6 - Extension


Write a function that finds the most owned pokemon. If many have the same count, return them all.