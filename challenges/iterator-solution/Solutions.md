# Iterator Solution 1

```
const myIterator = {
    current: 0,
    numbers: [11,13,14,66,67,69,234,456,2,1],
    next: function () {
        while (this.current <= this.numbers.length && this.numbers[this.current] % 2 !== 0){
            this.current++;
        }
        if (this.current >= this.numbers.length) {
            return {
                done: true
            }
        }
        else {
            const val = this.numbers[this.current]
            this.current++;
            return {
                value: val,
                done: false
            }
        }
    },
    [Symbol.iterator]: function () { return this; }
};

for (let x of myIterator) {
    console.log(x)
}
```

# Iterator Solution 2

```
const myIterable = {
    numbers: [11, 13, 14, 66, 67, 69, 234, 456, 2, 1],
    [Symbol.iterator]: function () {
        let self = this
        return {
            current: 0,
            next: function () {
                while (this.current <= self.numbers.length && self.numbers[this.current] % 2 !== 0){
                    this.current++;
                }
                if (this.current >= self.numbers.length) {
                    return {
                        done: true
                    }
                }
                else {
                    const val = self.numbers[this.current]
                    this.current++;
                    return {
                        value: val,
                        done: false
                    }
                }
            },
        }
    }
};

for (let x of myIterable) {
    console.log(x)
}

```