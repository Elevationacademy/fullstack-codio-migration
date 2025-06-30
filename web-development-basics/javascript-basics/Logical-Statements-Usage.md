# Logical Statements Usage

Logical operators are an important tool in implementing an efficient code.


- Avoid Chaining Logical conditions inside of each other
- Try to Simplify our conditions 

Don't: 
```
function isItMorning(time){
    if(time > 6){
        if(time <12){
            return true
        }
    }
    return false
}
```

Please Avoid this aswell:
```
function isItMorning(time){
    if(time < 6){
        continue
    }else{
        if(time <12){
            return true
            }
    }
    return false
}
```

Do:
```
function isItMorning(time){
    if(time > 6 && time < 12){
            return true
    }
    return false
}
```