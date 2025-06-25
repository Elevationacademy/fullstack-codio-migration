### Phrasing 1
A class/module/function should have a single responsibility

### Phrasing 2
Each module should be responsible to one, and only one, owner or stakeholder

### Not to Be Confused with
The most important thing is not to confuse this principle with 
"FUNCTIONS SHOULD DO ONE THING" which is also a Robert C Martin principle from the **clean code** guide. (which is, none the less a very important guideline)

So what is the difference?

Let's look at this example:

```
class Employee {
    
    calcPayment(){}

    reportHours(){}

    writeEmployee(){
        // saves the employee to a db
    }
}
```

Let's look the the functions inside the `Employee` class. 
Who is the owner of `calcPayment` ? 
Probably the finance department. 
Who is the owner of `reportHours` ?
Probably the HR department.
Who is the owner of `writeEmployee` ?
Probably the R&D department.

So what will happen if this code will change in the future?
We have 3 different owners that might affect this 1 module. This can cause a lot of problems.
We would want to divide this module and make sure that each module has only 1 owner.
