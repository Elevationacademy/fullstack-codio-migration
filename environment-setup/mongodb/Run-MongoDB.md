
Open up a new terminal and run the following command:

---

**Windows:**
```bash
mongod
```
  

This splurts out a lot of text but at the end of the day starts a server running on your computer. You should see something like this:

  

```bash
...
2019-04-06T09:13:55.130+0300 I FTDC     [initandlisten] Initializing full-time diagnostic data capture with directory '/data/db/diagnostic.data'
2019-04-06T09:13:55.132+0300 I NETWORK  [initandlisten] waiting for connections on port 27017
```
  

This means our MongoDB is up and running, and waiting for us to connect to it.

To connect and start writing DB operations, open a **new** terminal (or new tab), and **run the following command:**

  


```bash
mongo
```
  

You should now be in the mongo shell, and see something like this:

  

```bash
---

> 
```
  

Here we can write Mongo commands.

---

**Mac:**

Working with mongoDB in mac is abit different than windows, so make sure to keep track of the different usage during the course.

```bash
brew services start mongodb-community@4.0
```

**to stop the service you simply replace the start with stop**

This splurts out a lot of text but at the end of the day starts a server running on your computer. You should see something like this:

  

```bash
Successfully started `mongodb-community@4.0` (label:homebrew.mxcl.mongodb-c
```
  

This means our MongoDB is up and running, and waiting for us to connect to it.

To connect and start writing DB operations, **run the following command:**

```bash
mongo
```
  

You should now be in the mongo shell, and see something like this:

  

```bash
---

> 
```
  

Here we can write Mongo commands.

