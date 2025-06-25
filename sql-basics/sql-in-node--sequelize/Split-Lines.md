
Since some queries can get quite large, we recommend taking advantage of the backtick ` `` ` syntax to split your strings. For instance:

  
```
sequelize.query(`
                UPDATE company 
                SET name='Twitter'WHERE name='Apple'`, 
                function (result) {
                        console.log(result)
                }) 
```
  

The above is a perfectly valid `UPDATE` operation (please ignore the odd coloring; the callback function is separate from the query).