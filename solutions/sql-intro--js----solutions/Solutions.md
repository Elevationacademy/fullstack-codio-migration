## Exercise 1

```
use sql_intro;
create table Dolphin (
    name VARCHAR(30) NOT NULL PRIMARY KEY, 
    color VARCHAR(30),
    height INT(10),
    healthy BIT NOT NULL DEFAULT 1
);


INSERT INTO Dolphin (name, color, height)
VALUES("Daron", "gray", 5);


INSERT INTO Dolphin (name, color, height)
VALUES("Harry", "yellow", 1);


INSERT INTO Dolphin (name, color, height)
VALUES("Dan", "blue", 1);


INSERT INTO Dolphin (name, color, height)
VALUES("Yuval", "red", 3);


INSERT INTO Dolphin (name, color, height)
VALUES("Dorit", "green", 3);
select * from Dolphin WHERE height > 2;
```

## Exercise 2

```
SELECT *
FROM Dolphin 
WHERE name LIKE '%on%';
```

## Exercise 3

```
delete from Dolphin
where height < 2 and color = 'blue';
```

## Exercise 4

```
UPDATE Dolphin 
SET height = 6
WHERE name = 'Daron';
```

## Exercise 5

```
UPDATE Dolphin
set healthy = 0
WHERE color = 'green' or color = 'brown';
```
