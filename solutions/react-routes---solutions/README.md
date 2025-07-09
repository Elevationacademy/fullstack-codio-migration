# Solutions

## Exercise 1
```
import { Link } from 'react-router-dom';
class Home extends Component {
    render() {
        return (
            <div><div id="u-input"><input type="text" placeholder="Ask and you shall receive" /><div id="button">Seek</div></div>


                <h1 id="home-title">Your Adventure</h1>


                <div id="home-container"><div id="world"><span className="main-directory-text">World</span></div><Link to="/directory/wizards"><div id="wizards"><span className="main-directory-text">Wizards</span></div></Link><Link to="/directory/bestiary"><div id="bestiary"><span className="main-directory-text">Bestiary</span></div></Link><div id="potions"><span className="main-directory-text">Potions</span></div><div id="deities"><span className="main-directory-text">Deities</span></div></div></div>
        );
    }
}
```

## Exercise 2
```
class Fentities extends Component {
    
    render() {
        const fentitiesCategory = this.props.match.params.fentities
        const fentities = this.props.state[fentitiesCategory]
        return (
            <div><h1 id="fentities-title">{fentitiesCategory}</h1><div id="fentities-container">
                    {fentities.map(f => {
                        return (
                            <Link to={`/directory/${fentitiesCategory}/${f.name}`}><div className="mini"><img className="directory-img" src={f.imgUrl} alt="" /><span>{f.name}</span></div></Link>
                        )
                    })}
                </div></div>)
    }
}

class Fentity extends Component {
    render() {
        const { fentities, name } = this.props.match.params
        const fentity = this.props.state[fentities].filter(f => {
            return f.name.toLowerCase() === name.toLowerCase()
        })[0]
        console.log(fentity);
        return (
            <div id="creature-container"><h1>{fentity.name}</h1><img src={fentity.imgUrl} alt="" /><div className="title">Power:</div><div className="power text"> {fentity.power}</div><div className="other text">{fentity.other}</div></div>
        )
    }
}

class App extends Component {
  constructor() {
    super()
    this.state = {
      wizards: [
        { name: "Merlin", power: "Wisdom", other: "Helped King Arthur", imgUrl: "https://tinyurl.com/merlin-image" },
        { name: "Morgana Le Fay", power: "Forces of Nature", other: "Trapped Merlin in a cave for eternity", imgUrl: "https://tinyurl.com/morgana-image" },
        { name: "Gandalf", power: "Plot Convenience", other: "Once broke a bridge", imgUrl: "https://tinyurl.com/gandalf-img" }
      ],
      bestiary: [
        { name: "Smaug", power: "Fire and Flying", other: "Burned a city to with his mouth", imgUrl: "https://tinyurl.com/smaug-image" },
        { name: "Buckbeak", power: "Flying", other: "Knocked over Malfoy like a boss", imgUrl: "https://tinyurl.com/buckbeak-image" },
        { name: "Cerebrus", power: "Having three heads", other: "Holding back the dead since 100 BCE", imgUrl: "https://tinyurl.com/cerebrus-image" }
      ]
    }
  }


  render() {
    const state = this.state
    return (
      <Router>
        <div className="App">
          <div id="home-background"></div>
          <div id="main-links">
          <Link to="/">Home</Link>
          <Link to="/about">About</Link>


          </div>
            <Route path="/" exact component={Home} />
            <Route path="/about" exact render={() => <About items={Object.keys(state)} />} />
            <Route path="/directory/:fentities" exact render={({ match }) => <Fentities match={match} state={state} />}/>
            <Route path="/directory/:fentities/:name" exact render={({match}) => <Fentity match={match} state={state}/>} />
        </div>
      </Router>
    );
  }
}
```

## Extension 1
```
class Fentity extends Component {
    render() {
        const { fentities, name } = this.props.match.params
        const fentity = this.props.state[fentities].filter(f => {
            return f.name.toLowerCase() === name.toLowerCase()
        })[0]
        return (
            <div id="creature-container">
                <Link to={`/directory/${fentities}`}>Back</Link>
                <h1>{fentity.name}</h1>
                <img src={fentity.imgUrl} alt="" />
                <div className="title">Power:</div>
                <div className="power text"> {fentity.power}</div>
                <div className="other text">{fentity.other}</div>
            </div>
        )
    }
}
```

## Extension 2
```
class Fentity extends Component {
	  render() {
	    const {
	      state,
	      match: { params }
	    } = this.props;
	    const fentity = state[params.fentities].find(
	      f => f.name.toLowerCase() === params.name.toLowerCase()
	    );
	

	    return (
	      <React.Fragment>
	        {!fentity ? (
	          <Redirect to="./" />
	        ) : (
	          <div id="creature-container">
	            <Link to="./">Go back</Link>
	            {/* <Link to={`/directory/${this.props.match.params.fentities}`}>Go back</Link> */}
	            <h1>{fentity.name}</h1>
	            <img src={fentity.imgUrl} alt="" />
	            <div className="title">Power:</div>
	            <div className="power text"> {fentity.power}</div>
	            <div className="other text">{fentity.other}</div>
	          </div>
	        )}
	      </React.Fragment>
	    );
	  }
	}
```

## Extension 3
```
class Home extends Component {
	  constructor() {
	    super();
	

	    this.state = { term: '', seek: '' };
	  }
	

	  onChangeSeek = event => {
	    const appState = Object.keys(this.props.state);
	

	    this.setState({
	      term: event.target.value,
	      seek: `/directory/${appState[0]}/${this.props.state[appState[0]][0].name}`
	    });
	  };
	

	  onChangeSelect = event => {
	    this.setState({ seek: event.target.value });
	  };
	

	  generateDropDown() {
	    if (this.state.term.length === 0) {
	      return;
	    }
	

	    const appState = Object.keys(this.props.state);
	    const term = this.state.term.toLowerCase();
	

	    const filteredEntities = appState.map(category =>
	      this.props.state[category]
	        .filter(({ name }) => name.toLowerCase().includes(term))
	        .map(entity => (
	          <option key={entity.name} value={`/directory/${category}/${entity.name}`}>
	            {entity.name}
	          </option>
	        ))
	    );
	

	    return <select onChange={this.onChangeSelect}>{filteredEntities}</select>;
	  }
	

	  render() {
	    return (
	      <div>
	        <div id="u-input">
	          <input
	            type="text"
	            placeholder="Ask and you shall receive"
	            onChange={this.onChangeSeek}
	          />
	          <Link to={this.state.seek} id="button">
	            Seek
	          </Link>
	        </div>
	

	        {this.generateDropDown()}
	

	        <h1 id="home-title">Your Adventure</h1>
	

	        <div id="home-container">
	          <div id="world">
	            <Link to="/directory/world">
	              <span className="main-directory-text">World</span>
	            </Link>
	          </div>
	          <div id="wizards">
	            <Link to="/directory/wizards">
	              <span className="main-directory-text">Wizards</span>
	            </Link>
	          </div>
	          <div id="bestiary">
	            <Link to="/directory/bestiary">
	              <span className="main-directory-text">Bestiary</span>
	            </Link>
	          </div>
	          <div id="potions">
	            <Link to="/directory/potions">
	              <span className="main-directory-text">Potions</span>
	            </Link>
	          </div>
	          <div id="deities">
	            <Link to="/directory/deities">
	              <span className="main-directory-text">Deities</span>
	            </Link>
	          </div>
	        </div>
	      </div>
	    );
	  }
	}
```