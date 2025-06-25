Now when we want to access a specific route with a param.

Let's say like 
```js
http://localhost:3001/wiki/charms/Accio
```

we want to extract the string 'Accio'.
so we will `useParams` hook to help us.

`useParams` is a hook provided by the React Router library, which allows you to access the dynamic pieces of the URL in a React component.

In a React application that uses React Router, when a user navigates to a specific route with dynamic parameters (e.g. `/users/:userId`), the value of the dynamic parameter (e.g. the userId) can be accessed within the corresponding React component using the `useParams` hook.

The `useParams` hook returns an object that contains key-value pairs of the dynamic parameters defined in the URL. For example, in the case of `/users/:userId`, `useParams` would return an object with a `userId` property whose value is the actual value of the dynamic parameter in the URL.

Here's an example usage of `useParams`:

```js
import { useParams } from 'react-router-dom';

function UserProfile() {
  const { userId } = useParams();

  // use the userId variable in your component logic
  return (
    <div>
      User profile for user with ID: {userId}
    </div>
  );
}
```

So when you create a Route like this:
```js
 <Route path="/users/:userId" element={<UserProfile />} />

```

