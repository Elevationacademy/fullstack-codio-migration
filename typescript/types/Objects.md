Objects in TypeScript must have all the correct properties and value types.


```ts
let person: {
  name: string;
  location: string;
  isProgrammer: boolean;
};

person = {
  name: 'John',
  location: 'Israel',
  isProgrammer: true,
};
```

If we try to assign a wrong type we will get an error:
```ts
person.isProgrammer = 'Yes'; // ERROR, must be of 'boolean' type
```

Another important thing to notice is that all properties are required by default, which means that if we try to create an object with a missing property we will get an error:
```ts
person = {
  name: 'John',
  location: 'Israel',
}; 
// ERROR, missing 'isProgrammer' property
```

If we want to define an optional property we can do it with the `?:` syntax, like this:

```ts
let person: {
  name: string;
  location: string;
  isProgrammer?: boolean;
};
```

Now we can define a person without the `isProgrammer` property:

```ts
person = {
  name: 'John',
  location: 'Israel',
}; 
```