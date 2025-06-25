## Exercise 1

Create a function called ‘sum()’ which takes an array of numbers, calculates the sum of all numbers and returns that value.

Create a 2nd function called *isEven()* which takes a number and returns *true* if it’s an even number, of *false* if it’s an odd number.

Run 3 examples of calling *isEven()* and *sum()* with a random array of numbers. For each example use *console.log()* to print the array, followed by the sum, followed by the result of the *isEven()* function for the sum of each array.

<details>
<summary>Solution</summary>
<div> 

```
function sum(numbers: number[]): number {
    return numbers.reduce((a, b) => a + b);
}

function isEven(num: number): boolean {
    return num % 2 === 0;
}

const numArray1: number[] = [4,7,44,5,234];
const numArray2: number[] = [65,33,5,2532,32,6];
const numArray3: number[] = [54,6,656,4];

console.log(`${numArray1} | ${sum(numArray1)} | ${isEven(sum(numArray1))}`);
console.log(`${numArray2} | ${sum(numArray2)} | ${isEven(sum(numArray2))}`);
console.log(`${numArray3} | ${sum(numArray3)} | ${isEven(sum(numArray3))}`);

```
</div>
</details>

## Exercise 2

We want to create a small application that allows us to create student objects with grades and then print the average of their grades.

You need to create an array of *Student* classes. The *Student* class will have a standard constructor, and can be initiated with name, age and an array of grades.

The *Student* class will have 2 functions, *addGrade(grade)* which will add a grade to the grades array, *getGradeAvg()* which will calculate the average grade from all grades.


### Logic of the code
You need to create 3 students, add 4 unique grades for each student. Then print the list of students, whereby each print-out will include the student's name and the average grade.


|||info
## Hint

- Make sure to include correct TypeScript types for variables and functions. Keep special attention to return types.
- To make it easier, you can create Student objects first, and then initialize a *Student[]* array with the already created *Student* objects

|||

<details>
<summary>Solution</summary>
<div> 

```
class Student {
    full_name: string;
    age: number;
    grades: number[];
  
    constructor(full_name: string, age: number, grades: number[]) {
      this.full_name = full_name;
      this.age = age;
      this.grades = grades;
    }
  
    addGrade(grade: number): void {
      this.grades.push(grade);
    }

    getGradeAvg(): number {
        const average = this.grades.reduce((a, b) => a + b, 0) / this.grades.length;
        return average;
    }    
}

const student1: Student = new Student("John Smith", 23, [77,68,99,98]);
const student2: Student = new Student("Mike Johnson", 35, [84,85,75,88]);
const student3: Student = new Student("Jeff Howard", 32, [79,92,94,96]);
  
const students: Student[] = [student1, student2, student3];

students.forEach(student => {
    console.log(`${student.full_name}: ${student.getGradeAvg()}`);
});

```
</div>
</details>