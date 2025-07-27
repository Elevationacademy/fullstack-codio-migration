Now let's just adjust our code in `app.js`, we want to save our `token` in the **Local Storage**.


<details>
  <summary>
     Solution
  </summary>

The adjusted AJAX request in `app.js`.

```js
  $.ajax({
    url: '/login',method: 'POST',
    dataType: 'json',contentType: 'application/json',
    data: JSON.stringify({ username, password }),
    success: function(data) {
      localStorage.setItem('token', data.accessToken);
      window.location.href = '/fav_animals/animals.html';

    },
    error: function(error, textStatus, errorThrown) {
      if (error.status === 401) {
        console.log('Unauthorized error:', errorThrown);
      } else {
        console.log('Request failed:', errorThrown);
      }
    }
  });
});
```


</details>

<br/>
Now we are ready to do **Step 4!**


|||important
## Relocation

Note that once we authenticate and return a token from the server, our client will relocate to a different page.
|||