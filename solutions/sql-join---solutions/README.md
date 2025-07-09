# Solutions

## Exercise 1

```
USE sql_intro;
CREATE TABLE ethnicity
(
    id INT NOT NULL PRIMARY KEY,
    name VARCHAR(20)
);


CREATE TABLE gender
(
    id INT NOT NULL PRIMARY KEY,
    name VARCHAR(20)
);


CREATE TABLE symptoms
(
    family INT NOT NULL PRIMARY KEY,
    fever BIT,
    blue_whelts BIT,
    low_bp BIT
    );


CREATE TABLE disease
(
    name VARCHAR(20) NOT NULL PRIMARY KEY,
    survival_rate FLOAT
);


CREATE TABLE patient
(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    ethnicity INT,
    gender INT,
    symptoms_family INT,
    disease VARCHAR(20),
    FOREIGN KEY(ethnicity) REFERENCES ethnicity(id),
    FOREIGN KEY(gender) REFERENCES gender(id),
    FOREIGN KEY(symptoms_family) REFERENCES symptoms(family),
    FOREIGN KEY(disease) REFERENCES disease(name)
);
```



## Exercise 2

```
SELECT COUNT (*) from patient
WHERE disease IS NOT NULL;
```



## Exercise 3

```
SELECT COUNT (*) from patient
WHERE disease = 'cabbage disease';
```

## Exercise 4

```
SELECT id, survival_rate from patient, disease
WHERE patient.disease = disease.name
ORDER BY id;
```


## Exercise 5

```
SELECT symptoms_family, COUNT(*) FROM patient p
WHERE disease = 'cabbage disease'
GROUP BY symptoms_family
ORDER BY symptoms_family;
```


## Exercise 6

```
SELECT name, COUNT(*) FROM patient p, ethnicity e
WHERE p.ethnicity = e.id 
AND p.disease = 'lettuce disease'
GROUP BY p.ethnicity
ORDER BY p.ethnicity;
```