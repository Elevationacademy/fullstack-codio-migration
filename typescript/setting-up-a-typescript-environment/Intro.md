Setting up a JavaScript environment to use TypeScript is easy. You install TypeScript through any of the available package managers, such as npm, yarn or pnpm. For this course we will use npm as our baseline, which comes with a NodeJS distribution (specific instruction in the next page).

When we move to TypeScript, we need to consider the following new concepts that are introduced:
- **’.ts’ files.** TypeScript is a separate development language, and therefore, has it’s separate files, based on its own syntax. TypeScript files have the *.ts* extension. These come ‘in addition’ to the JavaScript files, which has the *.js* extension.
- **‘tsconfig.json’.** TypeScript introduces a configuration file called ‘tsconfig.json’, which includes the settings that control how TypeScript behaves, what elements of the programming language will be type-checked, where will the compiled *.js* files will be placed etc.

In this chapter, we will cover the following topics:
1. How to install TypeScript?
1. How to compile TypeScript files?
1. How to configure TypeScript?