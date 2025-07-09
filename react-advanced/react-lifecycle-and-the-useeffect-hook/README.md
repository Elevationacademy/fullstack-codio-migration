# Cleanup

We have learned how to use the `useEffect` hook, but we still did not cover a very important issue that might cause bugs.

Let's dive in into the cleanup option:

<div style="position: relative; padding-bottom: 56.074766355140184%; height: 0;"><iframe src="https://www.loom.com/embed/370747823c9e42daaeaaeae5b2df32b4" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

Here is the App code:
```
function App() {
  const [shouldRemove, setShouldRemove] = useState(false)

  const clickHandler = () => {
    setShouldRemove(true)
  }

  return (
    <div>
      <button onClick={clickHandler}>Remove</button>
      {shouldRemove ? null : <ClickReminder />}
    </div>
  );
}
```

and the ClickReminder code:
```
function ClickReminder() {
  const [timeoutId, setTimeoutId] = useState(null)

  const clickHandler = () => {
    console.log('clearing timeout');
    clearTimeout(timeoutId)
  }

  useEffect(() => {
    let timeoutId = setTimeout(()=>{alert("remember to click")}, 2000)
    setTimeoutId(timeoutId)
    
    return () => {
      clearTimeout(timeoutId)
    }
  }, [])

  return (
    <div>
      <button onClick={clickHandler}>Click</button>
    </div>
  );
}
```

This is good to know. It brings us to explore another option. Watch this video where we investigate another case of using cleanups:

<div style="position: relative; padding-bottom: 56.074766355140184%; height: 0;"><iframe src="https://www.loom.com/embed/0474f3a7a7524221bd803d000e308a3d" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

Here is the code:
```
function FriendStatus(props) {
  const [isOnline, setIsOnline] = useState(null);

  useEffect(() => {
    function handleStatusChange(status) {
      setIsOnline(status.isOnline);
    }
    ChatAPI.subscribeToFriendStatus(props.friend.id, handleStatusChange);
    
    return function cleanup() {
      ChatAPI.unsubscribeFromFriendStatus(props.friend.id, handleStatusChange);
    };
  });

  if (isOnline === null) {
    return 'Loading...';
  }
  return <div>
    Frind with id {props.friend.id} is {isOnline ? 'Online' : 'Offline'}
  </div>
}
```

One last thing that we can add is an optimization. We do want the cleanup function running if the props change, but only if the friend's id has changed. 
At the moment the cleanup function will run on every update.
To avoid that we can add the id to the dependencies array like that:

```
  useEffect(() => {
    function handleStatusChange(status) {
      setIsOnline(status.isOnline);
    }
    ChatAPI.subscribeToFriendStatus(props.friend.id, handleStatusChange);
    
    return function cleanup() {
      ChatAPI.unsubscribeFromFriendStatus(props.friend.id, handleStatusChange);
    };
  }, [props.friend.id]);
```

Now the cleanup will run only if the id of the friend has changed.