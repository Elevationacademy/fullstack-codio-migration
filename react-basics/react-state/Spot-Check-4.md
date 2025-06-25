
Create the following two functional components:

-   `Hot`
    -   A Component that contains the a div that has the following text `"I'm feeling too hot! "`
-   `Cold`
    -   A Component that contains the a div that has the following text `"It's too cold in here!"`

  

Create a button which toggles between the two components (switches between them).
  


At first, you should see `Hot`. Then, when you press the button, you should see `Cold`. If you press it again, you should see `Hot` again - go back and forth on each button press.






----

You can check the solution below

<details>
  <summary>
     Solution
  </summary>

      function App() {
        const [temperature, setTemperature] = useState("hot")
        const toggleTemperature = () => {
            setTemperature(temperature === "hot" ? "cold" : "hot");
        }
        return (
            <div className="App">
              {temperature == "hot"  ? <Hot/> : <Cold/>}
              <button onClick={toggleTemperature}>Change Temp!</button>
            </div>
        );
      }

      export default App;



</details>