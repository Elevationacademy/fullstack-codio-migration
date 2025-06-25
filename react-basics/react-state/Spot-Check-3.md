
Complete the  `Calendar`  and  `Register`  code from earlier, then install the  [React Extension](https://chrome.google.com/webstore/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi?hl=en) and change `state` manually to watch it work.

  

Specifically:

-   `App` should render an instance of both `Calendar` and `Register`
  -   The reservations data should be passed from `state` to both instances using the key `reservations`
-   The  `Calendar`    component should render "NAME has a reservation on DAY @ TIME" for each item in the reservations data received from `props`
-   The `Register` component (in the `components` folder) should render "DAY @ TIME" for each item in the reservations data received from `props`

  


<details>
  <summary>
     Here is our solution 
  </summary>

```js
function App() {
  const [reservations, setReservations] = useState([
    { day: "Monday", time: 2000, name: "Earl" },
    { day: "Monday", time: 1845, name: "Ella" },
    { day: "Tuesday", time: 1930, name: "Linda" },
    { day: "Wednesday", time: 2015, name: "Anni" }
  ]);

  return (
      <div className="ex-space">
        <h4 className="ex-title">Spotcheck 5</h4>
        <div className="exercise" id="spotcheck-5">
          <div>
            <Calendar reservations={reservations} />
            <Register reservations={reservations} />
          </div>
        </div>
      </div>
  )
}

function Register({reservations}) {

  return (<div id="register">
      <h4>You cannot reserve during these times:</h4>
      {reservations.map(r => {
        return <div key={r.name}>{r.day} @ {r.time}</div>
      })}
  </div>)
}

function Calendar(props) {
  return (
    <div id="calendar">
        <h4>Calendar</h4>
        {props.reservations.map(r => {
          return <div key={r.name}>{r.name} has a reservation on {r.day} @ {r.time}</div>
        })}
    </div>
  )
}
```
</details>