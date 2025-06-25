## Exercise 1
```
const StringFormatter = function () {
	
	    const capitalizeFirst = function (str) {
	        let newStr = str[0].toUpperCase()
	        newStr += str.slice(1).toLowerCase()
	
	        return newStr
	    }
	
	    const skewerCase = function (str) {
	        let newStr = str.replace(/ /g, "-")
	        return newStr
	    }
	
	    return {
	        capitalizeFirst,
	        skewerCase
	    }
	}
	
	const formatter = StringFormatter()
	
	console.log(formatter.capitalizeFirst("dorothy"))
	console.log(formatter.skewerCase("blue box"))
  ```
  
## Exercise 2
```
const Bank = function () {
	
	    let _money = 500
	
	    const depositCash = function (cash) {
	        _money += cash
	    }
	
	    const checkBalance = function () {
	        console.log(_money)
	    }
	
	    return {
	        deposit: depositCash,
	        showBalance: checkBalance
	    }
	
	}
	
	const bank = Bank()
	
	bank.deposit(200)
	bank.deposit(250)
	bank.showBalance()
```

## Exercise 3
```
const SongsManager = function () {
	

	    const _songs = {}
	

	    const _doesSongExist = function (newSong) {
	        const songKeys = Object.keys(_songs)
	        for(let song of songKeys) {
	            if(song === newSong) {
	                return true
	            }
	        }
	        return false
	    }
	

	    const _shaveSongLink = function (link) {
	        
	        const index = link.indexOf("=")
	        const newLink = link.slice(index + 1)
	

	        return newLink
	    }
	

	    const addSong = function (songName, songLink) {
	        const lowerCaseSong = songName.toLowerCase()
	        
	        if(_doesSongExist(lowerCaseSong)) {
	            console.log("You've already added this song.")
	        } else {
	            const shavedSongLink = _shaveSongLink(songLink)
	            _songs[lowerCaseSong] = shavedSongLink
	        }
	    }
	

	    const getSong = function (songName) {
	        if(_doesSongExist(songName)) {
	            console.log("https://www.youtube.com/watch?v=" + _songs[songName])
	        } else {
	            console.log("This song is not in your list.")
	        }
	    }
	

	

	    return {
	        addSong,
	        getSong
	    }
	}
	

	const songsManager = SongsManager()
	songsManager.addSong("sax", "https://www.youtube.com/watch?v=3JZ4pnNtyxQ")
	songsManager.addSong("how long", "https://www.youtube.com/watch?v=CwfoyVa980U")
	songsManager.addSong("ain't me", "https://www.youtube.com/watch?v=D5drYkLiLI8")
	

	songsManager.getSong("sax") // should print https://www.youtube.com/watch?v=3JZ4pnNtyxQ
	songsManager.getSong("how long")
	songsManager.getSong("ain't me")
	

	songsManager.addSong("sax")
	songsManager.getSong("truth")
```

