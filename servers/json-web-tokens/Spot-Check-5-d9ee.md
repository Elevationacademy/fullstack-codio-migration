Now that we are on a new page (our animal sound App) we want to make requests with `token`'s in the client.
We have not yet implemented a **JWT** authentication system yet in the backend (some sort of **middleware** that verifies we are who we say we are) it will be our next step.


Let's look at the code in the `animal.js`:

```js
$(document).ready(function() {
    $('.getFavAnimal').on('click', function() {
      $.ajax({
        url: `/favorites/animals`,
        method: 'GET',
        headers: {
          Authorization: `Bearer ${localStorage.getItem('token')}`
        },
        success: function(response) {
          $(".animal").append(`<h2>${response.animal}!</h2>`)
        },
        error: function(res, status, error) {
          location.href = "/"
        }
      });
      
    });
  });
```

This is the current code in `animal.js` it makes a request to a certain **API** endpoint in our server.
we want to include the current token we have with this request.

**Edit this code to include our token in the method we mentioned before**



<details>
  <summary>
     Solution
  </summary>

```js
$(document).ready(function() {
    $('.animal button').on('click', function() {
      var animal = $(this).siblings('img').attr('alt').toLowerCase();
      
      $.ajax({
        url: `/sounds/animals/${animal}`,
        method: 'GET',
        headers: {
          Authorization: `Bearer ${localStorage.getItem('token')}`
        },
        success: function(response) {
          alert(response);
        },
        error: function(res, status, error) {
          alert(res.responseText);
          location.href = "/"
        }
      });
      
    });
  });
```


</details>