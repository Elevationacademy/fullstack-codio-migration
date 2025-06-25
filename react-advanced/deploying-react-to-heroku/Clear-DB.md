
Until now, we had the database installed locally in our machine. When deploying our application to heroku we need to expose the server to external DB.

  

----------

  

We will use a service called ClearDB.

Go to [this link](https://dashboard.heroku.com/provision-addon?addonServiceId=2a4094b5-8880-4130-8449-b4fd14e795e0&planId=119215f7-7a6a-4cc5-8c2c-910eb5111916) and search your app you want to add ClearDB to it.

  

Then, press the `submit order form` it will show you a red alert. In the alert, click the verfy link and add your credit card. Don't worry they will not charge you if you chose the free plan.

Now, go back and press the `submit order form`.

This will add a `CLEARDB_DATABASE_URL` key to the `config` variables.

  

Finally, go to your code and change it to be:

```
const sequelize = new Sequelize(process.env.CLEARDB_DATABASE_URL);
```