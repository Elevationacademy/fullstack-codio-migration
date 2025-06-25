For this Spotcheck, please create a Like counter.

create a `Like button` which increases the number of likes on a `counter` that is displayed on the screen.



----

You can check the solution below


<details>
  <summary>
     Solution
  </summary>

    function App() {
        const [likes, setLikes] = useState(0)
        const increaseLike = () => {
          setLikes(likes+1);
        }
        return (
          <div className="App">
            <div>{likes}</div>
            <button onClick={increaseLike}>Like! 👍</button>
          </div>
        );
      }

    export default App;

</details>