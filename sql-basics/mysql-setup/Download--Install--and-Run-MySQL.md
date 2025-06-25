
There are a few parts to the MySQL proper setup: Download, Installation, and Running.

  

The process is different for Mac and Windows, and ultimately the goal is to run a local MySQL server on your own machine, and then create a couple of databases with which we will be working.

----------

### Mac Instructions

Run the following commands IN ORDER on your command line in order to download sql on your computer. This install assumes you have homebrew installed on your computer.

1.  If you don't have homebrew on your mac (you can check it by running in the terminal `brew -v` and getting something like `command not found`), you can install it via [this link](https://brew.sh/). It can take time...
2.  `brew install mysql`
3.  `brew services stop mysql`
4.  `brew services start mysql` - these two start a `mysql` server locally on your computer (you usually only have to do this once)
5.  Execute the following command to set the root password to 1234: `mysqladmin -u root password '1234'`
6.  `mysql -u root -p` - here you are accessing the server
    - enter your (mysql) password (`1234`)
7.  Now, in your mysql shell run the following commands:
    - `ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '1234';`
    - `FLUSH PRIVILEGES;` - these commands will allow you to use the old password mechanism in order to be able to connect later to VS code extension.
8.  `create database sql_testing;`
9.  `create database sql_intro;` - these commands create a couple of _databases_, which we'll talk about later
10.  to exit the mysql shell, press `control+z`

  

----------

### PC Instructions

1.  Go to [this](https://downloads.mysql.com/archives/community/) website, choose "Microsoft Windows" and download the 5.5 version of the "MSI Installer". Likely, it will be the 64-bit one, but if you're not sure you can check your computer.
2.  Once you download the installer, run it!
3.  Choose the "Standard" configuration
4.  Install as a windows service AND check "include bin directory in windows path"
5.  Choose the 'create anonymous account' and uncheck the other option.
6.  Finish the install - if prompted, you may need to restart your computer.
    - Make sure to allow any permissions windows asks of you
    - When continued to the "security" page, make sure to check the create anonymous user box and continue to finish the setup.
7.  Open a terminal as an administrator and run `mysqld` - this is what creates the local MySQL server on your computer
8.  Open another terminal as an administrator and run `mysql -u root` - here you are accessing the server
    - In this terminal, run `create database sql_intro;` and `create database sql_testing;`