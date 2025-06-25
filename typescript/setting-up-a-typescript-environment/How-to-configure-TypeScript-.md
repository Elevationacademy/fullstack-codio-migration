TypeScript’s settings can be configured in the *tsconfig.json* file. The file allows you to control many aspects of the TypeScript compiler and its behavior. We’ll outline the most important ones.

If you observe the *tsconfig.json* file, you’ll notice most of the settings are commented out and only a few are enabled. In this section we’ll cover the important ones to configure.

## Compiler Options
Let’s open the file and focus on the `compilerOptions` attribute. Let’s focus on four important attributes: target, strict, rootDir, outDir.
```
{
  "compilerOptions": {
	"target": "es6",
	"strict": true,
	"rootDir": "src",
	"outDir": "build"
  }
}
```

### Target
`Target` allows you to control the JavaScript version TypeScript will compile into, and *strict* allows you to enable or disable **strict mode**. More on configuring `strict` later in this chapter.

The available target options include primarily *es6* and *es5*, but it also supports newer versions such as es2020. You can see the full list of supported JS versions [here](https://www.typescriptlang.org/tsconfig#target).

### Strict
The `strict` attribute allows you to toggle ‘strict mode’ on and off. When this is enabled, by default, the language is at the strictest level. All type-checks are validated during compilation when this flag is on. When this flag is set to `true`, the `”use strict”;` syntax is added to the generated `.js` file.

You can control more fine-grained options using other attributes such as ‘noImplicitAny’, or ‘strictNullChecks’. We’ll cover these in the next chapter.

### Root Dir 
This attribute allows you to set the root directory of all the TypeScript files. It’s considered good practice to separate the TypeScript files from the JavaScript ones, to make sure the project’s file system is organized, and it’s easy to deploy `.js` code to other environments with ease (test, production etc.).

You should have a `src` folder in your project’s root directory which will hold the project’s folder structure and the TypeScript files.

Go on and create it. Next move the `app.ts` and `print.ts` to it.

### Out Dir 
Once you set up your `rootDir` attribute, you should choose a separate folder for your JavaScript generated files. It’s best practice to create a `build` folder and use it for your `.js` files.

Create a `build` folder and define it in the `tsconfig` as your `ourDir` folder.

** Delete the redundant `js` files.

Now your project should be much more ordered. The project structure should look like this:

```console
- node_modules
- build // js files
  - app.js
  - print.js  
- source // ts files
  - app.ts
  - print.ts 
- package-lock.json
- tsconfig.json
```

## Other configurations
In addition to compiler options, you can control other important elements, such as what files and folders to include and which ones to ignore. You would want to ignore folders that contain non-JavaScript related files such as .css, .txt, image files etc. Once you set TypeScript in a React, Angular or NodeJS environments, you would want to exclude the entire `node_modules` folder as well.

Oftentimes, you will have a development project which has mixed code, perhaps as part of migrating from an existing JavaScript project to TypeScript. In this case you would want to ensure only specific folders are included in the TypeScript build process. As a result, you would need to use the `include` and `exclude` attributes as follows. Notice that the `include` attribute indicates that only files in the `src` folder must be included in the compilation.
```
{
  "compilerOptions": {
	"target": "es6",
	"strict": true,
	"rootDir": "src",
	"outDir": "build"
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules"]
}
```
