
Before we dive into the exercises, make sure you `mongod` is running.

  

Next, fork & clone [this repository](https://github.com/Elevationacademy/linkedon-data). Navigate to the directory where the `generator.js` file is, and run the following command (run `npm install` first):

  
```js
node generator.js
```
  

This file should be run **once** - it will load some data into your DB, inside a new collection called `linkedon`

  

----------

  

The data you've loaded is from the popular site LinkedOn - it's a rival of LinkedIn. Same concept, less popular.

  

Each document contains data about one person and their current/historical professional info. Specifically, which job they're currently in (company and industry), and which jobs they've had in the past. **Explore this dataset before you begin the following exercises.**

  

If you have a JSON viewer installed in your browser, you can take a look at the data [here](https://raw.githubusercontent.com/Elevationacademy/linkedon-data/master/people.json?token=ALULtc6hWWL--avn4R9ieh7adfgg7n0Kks5csY1VwA%3D%3D).

  

----------

####   

With all that setup, you're ready to start querying. Remember, since we're querying the `linkedon` collection, and we've already run the `use test-db` command, we can use the following to execute commands on our new collection:

  
```js
db.linkedon.find({}) //or whichever operation
```
