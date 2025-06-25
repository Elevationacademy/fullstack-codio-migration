To get started with TypeScript, we need to install the TypeScript package using npm. Assuming you don’t have TypeScript installed on your machine, we’ll use the following syntax, which will allow us to install the latest version of TypeScript and make sure it’s installed globally.
```
npm install typescript@latest -g
```

Now TypeScript is installed globally, and we can use the TypeScript cli, invoked with the keyword `tsc`.
You can execute:
```
tsc --version
```
You will see the `tsc` version, of course.

Next, we’ll install the *tsconfig.json* file to allow us to control the configuration of TypeScript.
```
tsc --init
```

This will create the default settings of ‘tsconfig.json’.
