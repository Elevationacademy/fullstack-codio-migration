The following code has a few errors. Without running the code in your IDE, identify the errors, fix them and check the following answer to see the valid code.

```JavaScript
const employee: {
  name: string,
  salary: number,
  isManager: false,
  workDays
}

employee = {
  name: 'John',
  salary: 25000,
  isManager = false,
  workDays: [1,1,1,1,0,0];
}

if (employee.isManager) {
  console.log(`${obj.name} is a manager`);
  employee.salary = '30,000k';
} else {
  workDays[2] = false;
  workDays.push(0);
}
```

<details>
<summary>
Solution
</summary>
<div>

```JavaScript
let employee: {
  name: string,
  salary: number,
  isManager: false,
  workDays: number[]
}

employee = {
  name: 'John',
  salary: 25000,
  isManager: false,
  workDays: [1,1,1,1,0,0];
}

if (employee.isManager) {
  console.log(`${employee.name} is a manager`);
  employee.salary = 30000;
} else {
  employee.workDays[2] = 0;
  employee.workDays.push(0);
}
```
</div>
</details>