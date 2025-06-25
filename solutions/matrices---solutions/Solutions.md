## Exercise 1

```
constructor(row, col) {
	    this.matrix = this.generateMatrix(row, col)
}
print() {
	    console.log(this.matrix)
}
get(x, y) {
	    return this.matrix[x][y]
}
alter(row, col, newNumber) {
	    this.matrix[row][col] = newNumber
}
printColumn(x) {
	    this.matrix.forEach(row => console.log(row[x]))
}
printRow(y) {
	    for (let i = 0; i < this.matrix[y].length; i++) {
	      console.log(this.matrix[y][i])
	    }
}
```

## Exercise 2

```
findCoordinate(number) {
	    for (let i = 0; i < this.matrix.length; i++) {
	      for (let j = 0; j < this.matrix[i].length; j++) {
	        if (this.matrix[i][j] === number) {
	          return({ x: j, y: i })
	        }
	      }
	    }
}
```

## Exercise 3

```
 loadData(salaryData) {
	    this.matrix = []
	    salaryData.forEach(object => this.matrix.push((Object.values(object))))
}
```

## Exercise 4

```
 getEmployees(department) {
	    return this.matrix.filter(row => row[2] === department)
	      .map(row => row[1])
}
```

## Exercise 5

```
 getTotalSalary(department) {
	    let sum = 0
	    this.matrix.filter(row => row[2] === department)
	      .forEach(row => sum += row[3])
	    return sum
}
```

## Exercise 6

```
 findRichest() {
	
	    let highestSalary = 0
	    let name = ''
	

	    for (let i = 0; i < this.matrix.length; i++) {
	      if (this.matrix[i][3] > highestSalary) {
	        name = this.matrix[i][1]
	        highestSalary = this.matrix[i][3]
	      }
	    }
	

	    return name
}
```

## Exercise 7

```
class TicTacToe extends Matrix {
	    constructor() {
	        super()
	    }
	

	    loadBoard() {
	        for (let i = 0; i < 3; i++) {
	            this.matrix[i] = []
	            for (let j = 0; j < 3; j++) {
	                this.matrix[i].push('.')
	            }
	        }
	    }
}
```

## Exercise 8

```
play(rowNum, columnNum, player) {
	        player === 1 ? this.alter(rowNum, columnNum, 'x') : this.alter(rowNum, columnNum, 'o')
}
```

## Exercise 9

```
getColumn(colNum) {
	        let str = ''
	

	        for (let i = 0; i < this.matrix.length; i++) {
	            str += this.matrix[i][colNum]
	        }
	

	        return str
	    }
	

	

	    gettRow(rowNum) {
	        let str = ''
	

	        for (let i = 0; i < this.matrix[rowNum].length; i++) {
	            str += this.matrix[rowNum][i]
	        }
	

	        return str
	    }
	

	    play(rowNum, columnNum, player) {
	        player === 1 ? this.alter(rowNum, columnNum, 'x') : this.alter(rowNum, columnNum, 'o')
	        this._checkThreeInARow() ? console.log(`Congratulations player ${player}`) : null
	    }
	

	    _checkThreeInARow() {
	        let strs = []
	        for (let i = 0; i < 3; i++) {
	            strs.push(this.getColumn(i))
	        }
	

	        for (let i = 0; i < 3; i++) {
	            strs.push(this.gettRow(i))
	        }
	

	        let middle1 = ''
	        for (let i = 0; i < 3; i++) {
	            middle1 += this.matrix[i][i]
	        }
	

	        let middle2 = ''
	        for(let i = 2; i >= 0; i--) {
	            middle2 += this.matrix[i][i]
	        }
	

	

	

	        for(let str of strs) {
	            if((str === 'xxx') || (str === 'ooo')) {
	                return true
	            }
	        }
	

	        return false
	    }
}
```
