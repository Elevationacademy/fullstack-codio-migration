# Solutions

## Exercise 1

```
CREATE TABLE pokemon_type(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(25)
);


CREATE TABLE town(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(25)
);


CREATE TABLE trainer(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(25),
    town INT,


    FOREIGN KEY(town) REFERENCES town(id)
);


CREATE TABLE pokemon(
    id INT PRIMARY KEY,
    name VARCHAR(25),
    type INT,
    height SMALLINT,
    weight SMALLINT,


    FOREIGN KEY(type) REFERENCES pokemon_type(id)
);


CREATE TABLE pokemon_trainer(
    p_id INT,
    t_id INT,


    FOREIGN KEY(p_id) REFERENCES pokemon(id),
    FOREIGN KEY(t_id) REFERENCES trainer(id)
);
```

## Exercise 2

```
const getHeaviestPokemon = async function () {
    let results = await sequelize.query("SELECT name, weight FROM pokemon WHERE weight=(SELECT MAX(weight) FROM pokemon)")
    
    return results[0][0]
}
```

## Exercise 3

```
const getPokemonByType = async function(type) {
    let results = await sequelize
                            .query(`SELECT name FROM pokemon 
                                    WHERE type=(SELECT id FROM pokemon_type WHERE name = "${type}") `)


    return results[0]                                
}
```


## Exercise 5

```
const findRoster = async function(trainerName) {
    let results = await sequelize
                            .query(`SELECT p.name FROM pokemon AS p, trainer AS t, pokemon_trainer AS pt
                                    WHERE t.name = "${trainerName}"
                                    AND t.id = pt.t_id
                                    AND p.id = pt.p_id`)


    return results[0]
}
```

## Exercise 6 - Extension

```
const getMostOwnedPokemon = async function() {
    let [mostOwned] = await sequelize
                            .query(`SELECT p.name, COUNT(pt.t_id) AS owner_count FROM pokemon AS p, pokemon_trainer AS pt, trainer AS t
                                    WHERE  pt.p_id = p.id AND t.id = pt.t_id
                                    GROUP BY p.name`)


    mostOwned.sort((a, b) => b.owner_count - a.owner_count)
    let maxOwners = mostOwned[0].owner_count


    let indexNotMax = mostOwned.findIndex(mo => mo.owner_count !== maxOwners)
    mostOwned[0].splice(indexNotMax)


    let namesMostOwned = []
    mostOwned.forEach(mo => namesMostOwned.push(mo.name))
                                    
    return namesMostOwned
}
```