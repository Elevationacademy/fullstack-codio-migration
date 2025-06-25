## Exercise

```
class UniqueArray {
	    constructor() {
	        this.arr = []
	        this.length = 0
	        this.obj = {}
	    }

	    add(item) {
	            if(!this.exists(item)) {
	                this.arr[this.length] = item
	                this.length++
	                this.obj[item] = 1
	            }
	    }
	

	    showAll() {
	        console.log(this.arr)
	    }
	

	    exists(item) {
	        if(this.obj[item]){
	            return true
	        } else {
	            return false
	        }
	    }
	

	    get(index) {
	        if(index <= (this.length - 1)){
	            return this.arr[index]
	        } else {
	            return -1
	        }
	    }
	

}
```


## Extension

```
_isPrimitive(item) {
	        if(typeof item === "number" || typeof item === "string" || typeof item === "boolean" ||typeof item === "undefined" || typeof item === "null" || typeof item === "symbol") {
	            return true
	        } else {
	            return false
	        }
}
	

add(item) {
	        if(this._isPrimitive(item)) {
	            if(!this.exists(item)) {
	                this.arr[this.length] = item
	                this.length++
	                this.obj[item] = 1
	            }
	        }
}

```