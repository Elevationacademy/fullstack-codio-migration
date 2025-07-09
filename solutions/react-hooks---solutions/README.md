# Solutions

## Exercise 1

```
export default function Exercise1() {
  const countries = ['united states', 'china', 'united kingdom', 'australia']
  const [name, setName] = useState('')
  const [city, setCity] = useState('')
  const [country, setCountry] = useState('')


  return (
    <div className="ex-space">
      <h4 className="ex-title">Exercise 1</h4>
      <div className="exercise" id="ex-1">
        <input type="text" name="name" onChange={e => setName(e.target.value)} placeholder="name" value={name}/>
        <input type="text" name="city" onChange={e => setCity(e.target.value)} placeholder="city" value={city}/>
        <select name="" id="" onChange={e => setCountry(e.target.value)}>
          {countries.map(c => <option key={c} value={c}>{c}</option>)}
        </select>
      </div>
    </div>
  )
}
```

## Exercise 2

```
export default function Exercise2() {
  const [users, setUsers] = useState([])
  useEffect(() => {
    (async () => {
      const users = await axios.get('https://randomuser.me/api/?results=5')
      console.log(users.data.results);
      setUsers(users.data.results)
    })()


  }, [])
  return (
    <div className="ex-space">
      <h4 className="ex-title">Exercise 2</h4>
      <div className="exercise" id="ex-2">
        {users.map((u, i) => {
          return (
            <div key={i}>
              <span>{u.name.first}</span>
              <span>{u.name.last}</span>
              <img src={u.picture.thumbnail} alt="" />
            </div>
          )
        })}
      </div>
    </div>
  )
}
```

## Exercise 3

```
export default function Exercise3() {
  const [month, setMonth] = useState(0)
  const [expenses, setExpenses] = useState([])
  const months = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
  ]


  useEffect(() => {
    (async () => {
      const expenses = await fetchExpenses(month)
      setExpenses(expenses)
      console.log(expenses)
    })()
  }, [month])


  return (
    <div className="ex-space">
      <h4 className="ex-title">Exercise 3</h4>
      <div className="exercise" id="ex-3">
        <select name="" id="" onChange={e => setMonth(e.target.value)}>
          {months.map((m, i) => <option key={i} value={i}>{m}</option>)}
        </select>
        {expenses.map((e, i) => {
          return (
            <div key={i}>
              <span>{e.item}</span>
              <span>{e.date}</span>
              <span>{e.amount}</span>
            </div>
          )
        })}
      </div>
    </div>
  )
}
```