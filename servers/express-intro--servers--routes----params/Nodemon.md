
So far when we made changes in our code, we had to save the file, kill the server pressing `ctrl + c` and then run again `node server.js`.

It's annoying!

Luckily for us there is a package that will run the server automatically every time the files where saved.

Open your terminal and run the command `npm install -g nodemon`

The ``-g`` is a flag the tells the computer to install the package globally (it's mean that you can run the command in any project without installing the package again and again).

Now, instead of running `node server.js` you should run `nodemon server.js`.

try changing something in the server.js and save it, go to the browser and refresh the page, you should see the new updates!!

----------

  

PC users:

If you are running into a error message saying something like this:
```
﻿nodemon : File C:\Users\yoni\AppData\Roaming\npm\nodemon.ps1 cannot be loaded because running scripts is disabled on this system.   
For more information, see about_Execution_Policies at https:/go.microsoft.com/fwlink/?LinkID=135170.
At line:1 char:1
```
  

Open your "Window PowerShell" as administrator (You can search for it in the search panel), and run `Set-ExecutionPolicy remotesigned`

  

Mac users:

If you running into problems installing the package, try `sudo npm install -g nodemon` and enter your mac password.