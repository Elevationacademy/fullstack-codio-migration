Once TypeScript is installed, you can go ahead and compile files, projects and make the TypeScript compiler ‘watch’ for file changes and compile files as they change during development.

For this let's create a simple typescript file called `app.ts`.
It will include the following content:
```typescript
let message: string = "hello"
message += "!!"
console.log(message);
```

Create another file called `print.ts` with the following content:
```typescript
let greeting: string = "hello"
console.log(greeting);
```

# Compiling

### Compiling a single TypeScript file
You can compile a single *.ts* file using the `tsc` command:
```
tsc app.ts
```
This will compile the file into `app.js` in the same folder.

### Compiling a TypeScript project?
To compile an entire project, we would run the following command from the project’s root folder:
```
tsc --build
```

This option will compile the entire project and will consider all of the folder settings defined in the *tsconfig.json* file. More on that later.

### Automatic compilation
To use automatic file compilation during development, without needing to manually compile the project, you can run the following command from the project’s root folder. This will ‘listen’ to file changes and automatically compile the entire project.
```
tsc --watch
```
Now let's verify it!
Go to your `print.ts` file and add a cat name:
```typescript
let greeting: string = "hello"
let catName: string = "fifi"
console.log(greeting + " " + catName);
```
Now go to the js version - `print.js`. You will see that the `catName` variable was added without any action on your side. 
How sweet!!