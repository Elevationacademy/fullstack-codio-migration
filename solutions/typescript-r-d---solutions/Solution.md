
Person.interface.ts:
```
import {IHobby} from './IHobby.interface';

export interface IPerson {
    name: string,
    age: number,
    height: number,
    hobbies: [IHobby],
    weight: number,
    grow: () => void;
    loseWeight: (number) => void;
    addHobby: (IHobby) => void;
    getHobbiesNames: () => string[];
}
```

Person.ts:
```
import { IHobby } from './IHobby.interface';
import { IPerson } from './IPerson.interface';
class Person implements IPerson {
    name: string;
    age: number;
    height: number;
    hobbies: [IHobby];
    weight: number;
    constructor(name, age, height, weight, hobbies) {
        this.name = name;
        this.age = age;
        this.height = height;
        this.weight = weight;
        this.hobbies = hobbies;
    }
    grow = () => {
        this.age++;
    }
    loseWeight = (number) => {
        this.weight -= number;
    }
    addHobby = (hobby: IHobby) => {
        this.hobbies.push(hobby)
    }
    getHobbiesNames = (): string[] => {
        return this.hobbies.map((h: IHobby) => h.hobbyName)
    }

}
```

Hobby.interface.ts
```
export interface IHobby {
    hobbyName: string,
    years: number
}
```

Hobby.ts:
```
import { IHobby } from './IHobby.interface';
class Hobby implements IHobby {
    hobbyName: string;
    years: number;
    constructor(hobbyName: string, years: number) {
            this.hobbyName = hobbyName;
            this.years = years;
    }
}
```