
To build this project you will need to do the following:

  

The main component is the `App` component, it should have **at least** the following properties and methods:

The state will have:

-   `minutes` - the minutes of the timer, should be initialized to `'25'`
-   `seconds` - the seconds of the timer, should be initialized to `'00'`
-   `timer` - will contain the interval (that will count the timer down)
-   `isWorkMode` - boolean that represents if the user is in work or break mode, should be initialized to `true`
-   `isActive` - boolean that represents if the timer is running or not (play/pause), should be initialized to `false`

  

The methods will be:

-   `start` - starts the timer by setting an interval, and calling the `tick` method
-   `pause` - will clear the `interval` and stop the timer
-   `reset` - will pause the `timer`, and reset the state `minutes`/`seconds` (according to the `isWorkMode` property)
-   `finished` - stops the timer and resets the time to the next mode (will be called when the time is equal to 0)
-   `changeMode` - receives a parameter (`'break'` or `'work'` mode) and updates the state properties to the relevant mode, also invokes the reset method
-   `tick` - the logical method that will be called every second. This method should check if the timer ended (as to not to run time negatively) and format the minutes and seconds (the format should be 04:03 or 21:09, not 4:3 or 21:9).

  

  

----------

  

**NavBar**

  

This component should receive one function as props:

-   `changeMode`

  

The component will have two buttons:

-   `Work mode`
-   `Break mode`

  

Both will invoke the `changeMode` method with a relevant argument (`'work'` or `'break'`)

  

----------

  

**Clock**

  

This component should receive two props: `minutes` and `seconds`, and display them on the screen (remember, when they change the clock changes).

  

----------

  

**ActionRow**

  

The component will receive the following props:

-   `activateAction` - the method that will invoke the start or pause methods, depending on the value of the `isActive` property (in the state)
-   `resetClicked` - should be the `reset` method
-   `currentAction` - will hold the title for the start/pause button, depending on the value of the `isActive` property (in the state)

  

The component will hold two buttons:

-   One for the `start`/`pause` button, will invoke the prop `activateAction` method, and hold the title received from the parent component (the `currentAction` prop)
-   The second is the `reset` button which will invoke the prop `reset` method
