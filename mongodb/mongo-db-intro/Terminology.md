
In Mongo, a **database** is the place where _all_ our data is stored. Usually each _project_ or _app_ will have its own DB.

  

In any Mongo DB we can have one or more **collections**. A collection is effectively a _list_ of similar items. These items might be "users", "products", "books", etc.

  

The technical term for these items is **document** - documents in Mongo DB work nearly identically to plain JSON: key-value pairs, no trailing commas, etc.

  

So in sum: any app we create will likely have **one DB** that has **one or more collections**, each of which likely has **many documents** inside of it.
