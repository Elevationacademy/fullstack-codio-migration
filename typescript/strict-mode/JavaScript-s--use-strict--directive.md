TypeScript is not the first to introduce strict typing. JavaScript ES5 already introduced the ‘use strict’ directive, which forced run-time type and syntax validation. Strict mode is declared by adding `“use strict";` to the beginning of a script or a function. To affect the entire project, you will place this directive on the first line of your main project file, if you want to affect only a function, you place this directive on the first line of your function code.

### What is checked in ‘use strict’.
When using ‘use strict’ in JavaScript, these are common examples of what is not allowed in strict mode:
- Using a variable, without declaring it
- Using an object, without declaring it
- Deleting a variable (or object)
- Deleting a function
- Duplicating a parameter name