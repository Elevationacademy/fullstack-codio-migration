
Create a route called ``/details` that extracts the optional parameters `zipcode`, `city`, and `middleName`. Once you get the details, console log the `city` in the server, then send a response with all the params.

  

Ultimately, when you go to your route, you should receive an object that looks like this:

  
```
{
  zipcode: "6863155",
  city: "Ankh Morpork",
  middleName: "Wilfred"
}
```
  

The route should look like [this](https://codepen.io/ElevationPen/pen/qzmarZ?editors=0010).

  

The request (in the browser):
<details><summary>
  Click here to reveal the answer.
</summary>

http://localhost:3000/details/?zipcode=6863155&city=Ankh Morpork&middleName=Wilfred


</details>

</br>
  

Result:

  

![](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/express-routes-many-optional-params.PNG)

Plus a console log of `Ankh Morpork` in the _server_