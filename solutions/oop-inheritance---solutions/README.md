# Solution

```
class Person {
	    constructor(name, startYear) {
	        this.name = name
	        this.startYear = startYear
	        this.courses = []
	    }
	

	    addCourse(course) {
	        this.courses.push(course)
	    }
}
	

class Student extends Person {
	    constructor(name, startYear) {
	        super(name, startYear)
	        this.grades = []
	    }
	

	    addCourse(course) {
	        if (this.courses.indexOf(course) == -1) {
	            super.addCourse(course)
	        }
	    }
	

	    receiveGrade(courseName, finalGrade) {
	        this.grades.push({
	            course: courseName,
	            grade: finalGrade
	        })
	    }
}
	

class Teacher extends Person {
	    constructor(name, startYear, salary) {
	        super(name, startYear)
	        this.salary = salary
	        this.courses = {}
	    }
	

	    giveGrade(student, courseName, grade) {
	        student.receiveGrade(courseName, grade)
	    }
	

	    addCourse(course) {
	        let courseNames = Object.keys(this.courses)
	        for (let courseName of courseNames) {
	            if (course === courseName) {
	                this.courses[course] += 1
	                return
	            }
	        }
	        this.courses[course] = 1
	    }
}
	

class TeachingAssistant extends Teacher {
	    constructor(name, startYear, salary) {
	        super(name, startYear, salary)
	    }
}
	

	

class Principal extends Person {
	    constructor(name, startYear) {
	        super(name, startYear)
	        this.teachers = []
	        this.students = []
	    }
	

	    hireTeacher(teacher) {
	        this.teachers.push(teacher)
	        console.log(`${this.name} just hired ${teacher.name}`)
	    }
	

	    recruitStudent(student) {
	        this.students.push(student)
	        console.log(`${this.name} just recruited ${student.name}`)
	    }
	

	    expelStudent(student) {
	

	        for (let i in this.students) {
	            if (this.students[i].name === student.name) {
	                return this.students.splice(i, 1)
	            }
	        }
	    }
	

	    transferStudent(student, principal) {
	        this.expelStudent(student)
	        principal.recruitStudent(student)
	    }
	

}
```