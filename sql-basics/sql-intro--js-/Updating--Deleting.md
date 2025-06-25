
Of course our DB will likely be dynamic, things change and _Things Fall Apart_ all the time, so we need to know how to handle that too. Honestly, SQL syntax is pretty friendly so you can probably figure this out just by looking at it:

  

  

**Updating**

```
UPDATE TABLE_NAME
SET colum1_name = new_value, columX_name = new_value, ...
WHERE SOME_CONDITION;
```
  

The `WHERE` condition is **very** important because otherwise you'll update _everything_!

**Deleting**

```
DELETE FROM TABLE_NAME
WHERE SOME_CONDITION;
```
  

The condition here is even **more** important - you understand why.