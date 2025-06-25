
Another cool thing SQL knows to do for us is order our results. Say we want to see our deities in the order by which they were created. You can probably guess the syntax at this point:

  
```
SELECT * FROM Deity ORDER BY creation_date
```
  

  

Check out the result for yourself. Note that by default SQL will order it from lowest to highest, known as **Ascending** order. To go the other way, you can add `DESC`, short for **Descending**, to the _end_ of the query.

  

Heck, you can even `ORDER BY` _multiple_ columns. All you have to do is comma separate: `ORDER BY creation_date, coolness` - and you can even add `ASC` or `DESC` separately to each field.