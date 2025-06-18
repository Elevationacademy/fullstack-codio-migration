# JavaScript Exercises

1. **Count Object Properties**: 
   Write a function that counts the number of properties in an object.
   ```javascript
   function countProperties(obj) {
       // Your code here
   }
   // Test the function with
   console.log(countProperties({ name: 'Alice', age: 25 })); // Should return 2
   ```

2. **Check for Nested Property**:
   Write a function to check if a nested property exists in an object.
   ```javascript
   function hasNestedProperty(obj, key) {
       // Your code here
   }
   // Test the function with
   console.log(hasNestedProperty({ user: { name: 'Bob', age: 30 } }, 'user.name')); // Should return true
   ```

3. **Calculate Age from Birth Year**:
   Create an object `person` with properties `name` and `birthYear`. Write a function that calculates age from the birth year.
   ```javascript
   let person = {
       name: 'John',
       birthYear: 1990
   };

   function calculateAge(obj) {
       // Your code here
   }
   // Test the function with
   console.log(calculateAge(person)); // Should return age
   ```

4. **Update Object Property**:
   Write a function that updates the value of a given property in an object.
   ```javascript
   function updateProperty(obj, key, value) {
       // Your code here
   }
   // Test the function with
   console.log(updateProperty({ name: 'Alice' }, 'name', 'Bob')); // Should change name to Bob
   ```

5. **Nested Object Creation**:
   Write a function to create a nested object from a single object with dot-separated keys.
   ```javascript
   function createNestedObject(obj) {
       // Your code here
   }
   // Test the function with
   console.log(createNestedObject({ 'user.name': 'Alice', 'user.age': 25 })); // Should return { user: { name: 'Alice', age: 25 } }
   ```

6. **Display Object in HTML**:
   Write a function that takes an object and displays its properties and values in HTML format.
   ```javascript
   function displayObjectInHTML(obj) {
       // Your code here
   }
   // Test with an object of your choice
   ```

7. **Object Property Checker**:
   Write a function that checks if a property exists in an object.
   ```javascript
   function hasProperty(obj, key) {
       // Your code here
   }
   // Test the function with
   console.log(hasProperty({ name: 'Alice', age: 25 }, 'age')); // Should return true
   ```

8. **Add Method to Object**:
   Add a method `greet` to an object `person` that returns "Hello, [name]!".
   ```javascript
   let person = {
       name: 'John',
       greet: function() {
           // Your code here
       }
   };
   // Test the method with
   console.log(person.greet()); // Should return "Hello, John!"
   ```

9. **Object to Array Conversion**:
   Write a function that converts an object into an array of `[key, value]` pairs.
   ```javascript
   function objectToArray(obj) {
       // Your code here
   }
   // Test the function with
   console.log(objectToArray({ name: 'Alice', age: 25 })); // Should return [['name', 'Alice'], ['age', 25]]
   ```

10. **Merge Two Objects**:
    Write a function that merges two objects into one.
    ```javascript
    function mergeObjects(obj1, obj2) {
        // Your code here
    }
    // Test the function with
    console.log(mergeObjects({ name: 'Alice' }, { age: 25 })); // Should return { name: 'Alice', age: 25 }
    ```
