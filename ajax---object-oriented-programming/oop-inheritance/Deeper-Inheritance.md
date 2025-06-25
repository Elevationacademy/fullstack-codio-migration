
As well as having a Parent-Child inheritance relationship, we can also have a Parent-Child-Grandchild relationship, where Child is now the parent of Grandchild. Check this out:

  
```
class TeachingAssistant extends Teacher {
    constructor(name, startYear, salary) {
        super(name, startYear, salary)
    }
}
```
  

Though it would be a little pointless to leave this class as-is, we could and it would work just fine.

See this:
```
const s1 = new Student("Ronda", 2017)
const ta1 = new TeachingAssistant("Brandon", 2014, 20000)

ta1.addCourse("General Relativity")
ta1.giveGrade(s1, "General Relativity", 91)

console.log(ta1.salary) //prints 20000
console.log(ta1.courses) //prints {"General Relativity": 1}
console.log(s1.grades) //prints [{course: "General Relativity", grade: 91}]
```
  

The cool thing here is that `TeachingAssistant` has all the capabilities and attributes - all the powers, if you will - of a `Teacher`, _including the overridden methods_ - and we didn't have to define anything in `TeachingAssistant`'s class - we inherited everything!

  

This type of inheritance is called **Multi-Level Inheritance**, where the flow is A → B → C →...

  

Where **C** inherits from **B** which inherits from **A**.. (theoretically, we could inherit onwards forever)

  

**Spot check:** in terms of `instanceof` - what is `ta1` - a `TeachingAssistant`, a `Teacher`, a `Person`?

<details><summary>Solution</summary>

All three! Polymorphism!

</details>
