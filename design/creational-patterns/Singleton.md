A singleton is a single instance, static, global instance that can be accessed from everywhere.
This pattern solves two problems at once:
1. Forcing a class to have only one instance.
2. Having a global access point for a resource.

Singletons are used when you want to ensure that a certain resource is only instantiated once.
It is used a lot for static data, configuration, and similar cases.

Here is an example of singleton implementation in vanilla JavaScript:
```JavaScript
function Singleton() {
  class SingletonData {
  }

  const _instance = new SingletonData();
  function getInstance() {
    return _instance;
  }

  return {
    getInstance
  }
}
```
Let's break this down to better understand. Our `Singelton` function holds an inner "private" variable called `_instance`. This inner variable holds the only and single instance of the inner "private" class `SingletonData`. The `Singelton` function returns the `getInstance` function so clients can get a hold of the signle global instance of `SingletonData`.

Here is an identical example, only this time in TypeScript (which is more friendly than JavaScript when it comes to design patterns):
```JavaScript
class Singleton {
  private static instance: Singleton;

  private constructor() { }

  public static getInstance(): Singleton {
    if (!Singleton.instance) {
      Singleton.instance = new Singleton();
    }
    return Singleton.instance;
  }
}
```
As you can see here, we have a static `instance` field which holds the actual instance,
we have a static getter method `getInstance()` which returns the instance, but also lazily initializes it, and we have a private constructor.
Remember that if you do not implement a private constructor the class will have a public parameterless constructor by default and it will make your singleton implementation not enforceable.

Now, let's add some functionality to our Singleton.

JavaSript:
```JavaScript
function Singleton() {
  class SingletonData {
    constructor() {
      this.notes = ["do","re","me","fa","sol","la","si"];
    }

    getNotes(count) {
      return this.notes.slice(0, count)
    }
  }

  const _instance = new SingletonData();
  function getInstance() {
    return _instance;
  }

  return {
    getInstance
  }
}
```
TypeScript:
```
class Singleton {
  private static instance: Singleton;
  private notes: string[];

  private constructor() { 
    this.notes = ["do","re","me","fa","sol","la","si"];
  }

  public static getInstance(): Singleton {
    if (!Singleton.instance) {
      Singleton.instance = new Singleton();
    }
    return Singleton.instance;
  }

  public getNotes(count: number): string[] {
    return this.notes.slice(0, count);
  } 
}
```
We have added a list of notes which is initialized at the constructor,
we also added a method that returns the notes according to a count sent by the user.

Notice that the list of notes and our method are not static, they do not belong to the class itself but to the specific instance.

This is how we use this method.

JavaScript:
```
const notes = Singleton().getInstance().getNotes(3)
```
TypeScript:
```
const notes: string[] = Singleton.getInstance().getNotes(3)
```
As you can see, we can call `Singleton.getInstance()` anywhere, because it is static, and then we are calling the non static method `getNotes()` which belongs to the  instance.

### Pitfalls and risks
There are a few things to consider while planning to use a singleton.
1. It is risky when used in multithreaded programs. A different thread can create another instance of our supposedly single-instance class.
2. It is harder to unit test a singleton class.
3. Using singleton can sometimes point to bad design, it can mean that the resource is more accessible than actually necessary. It is sometimes just easier to use a singleton than to use a more sophisticated design, so try to avoid using singleton just to go easy on yourself.