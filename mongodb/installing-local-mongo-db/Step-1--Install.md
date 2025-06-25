
Depending on your computer, there are different ways to install Mongo:

|||important
## MongoDB V5

Please make sure to download V5. you can use this [link as reference](https://www.mongodb.com/download-center/community/releases/archive#:~:text=Archive%3A%20mongodb%2Dwindows%2Dx86_64%2D5.0.14.zip) to see all versions.
|||

**Windows**:

-   Go to [mongo's website](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-windows/#download-mdb-edition) and follow the download instructions with the following notes:
-   At a certain point you will be asked to install MongoD as a Service - **do not** do this
-   You will also be prompted to install MongoDB Compass; this is optional
-   Before running the server for the first time, we must create the directory to which the MongoDB server will write its data
-   By default, this folder is `C:\data\db`
-   As such, go to your `C:\` drive, and create a `data` folder. Inside of `data`, create a `db` folder
-   We can now run Mongo commands from the directory where we installed MongoDB, but we would like to be able to run these commands from anywhere
-   If you know what it means to add the mongo path to your computer's global variables, then go ahead and do so
-   Otherwise, see [this video](https://youtu.be/sBdaRlgb4N8?t=90) for instructions on how to do that
-   If you are windows 10 users see [this video](https://youtu.be/ll2tY6KH8Tk?t=141) (Watch until 4:45 where he starts talking about mongo service)
-   Notice that the first thing we see in the video is where our Mongo files were saved
-   Also notice that once he finishes explaining "adding the path", he talks about creating the `data\db` directory which we've already done

  

**Mac:**

Since Apple updated Mac OS to Catalina, there are few steps to do. follow [this article](https://medium.com/better-programming/installing-mongodb-on-macos-catalina-aab1cbe0c836) to install MongoDB correctly. note that this article is for users that have Catalina version, if you have prior version of Mac OS, use the following instruction:

-   The easiest way to install MongoDB on a Mac is through Homebrew. If you don't already have Homebrew installed on your Mac by now, enter the below code into a terminal window (without the "$"):
-   `$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
-   then after Homebrew is finished installing:
-   `$ brew update`
-   `$ brew install mongodb`
-   Before running the server for the first time, we must create the directory to which MongoDB server will write its data. By default, this folder is `\data\db` on Mac. You need to create this directory as with the correct permissions so type: `mkdir -p /data/db`. Create those folders now.
-   Ensure that user account running MongoDB has the proper directory permissions by running these commands:
-   `sudo chown -R id -un /data/db` and write your password down
