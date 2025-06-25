
#### **1. Edit Request Paths on The Client**

  

If you interacted with your server hosted on a local environment, you need to edit your request paths to be hosted in the same location as your server.

  

For example: `axios.get(https://localhost:8080/items)`

  

will have to change to

  

`axios.get(/items)`

  

since our client and server will be hosted in the same place.

  

You'll need to update this for all requests on your client. Your server paths should still work fine.

----------

  

#### **2. Serve the Build**

  

Heroku runs a build and heroku-postbuild script automatically during deployment if they are specified in the package.json of your app.

  

Create-react-app declares the "`build`" script automatically to create a production build of your project. This script will create a build directory in your project which contains your compiled (or minified/uglyfied) react files.

  

So, all you need to do is _serve_ the build directory on your server. This way, once the build is done running when you deploy, your server knows to use it for your app.

  

So **in your** **`server.js`** **file add in the following line to your server, before any routes**:

  

```
app.use(express.static(path.join(__dirname, 'build')));
```
  

Your server is now serving a production build of your app!

----------

  

#### **3. Add in a Catch-all Handler**

  

At the **bottom** of your `server.js` file, above your `app.listen`, add in the following line:

  
```
app.get('*', function (req, res) {
    res.sendFile(path.join(__dirname, 'build', 'index.html'));
});
```
  

This is a "catch-all" route handler, essentially saying that if your server did not register any of the other routes, it will send the `index.html` file from your `build`. That's why it's **essential that this line comes after all of your other routes!**

  

Note, some people also use this catch-all route as a fallback to return an error (or 404) html.

  

----------

  

Heroku also runs the "`start`" script if it is specified in your `package.json`.

**Remember, you have to change your "`start`" script in your `package.json` to be "`node server.js`" instead of "`react-scripts-start`"** (when deploying any app to heroku).