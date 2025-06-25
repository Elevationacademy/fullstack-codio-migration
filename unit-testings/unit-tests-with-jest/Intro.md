The concept of "testing" code has been around since Time Immemorial. Maybe not that long though.

  

If we take a moment to step back and think about code in the Real World, then you quickly realize that there are pieces of software out there that are literally processing **billions of dollars** every hour.

  

Or some bio-tech program that might **save a life**.

  

With any code that serves clients, we as the developers need to do everything we can to guarantee the code will work. However, **code changes all the time** - new developers join the team, veteran developers leave - and sometimes a piece of code that was written by Person A in 2019 could be modified by Person B in 2023.

  

One of the reasons to write tests is **to validate that changes in our code do not ruin our code's functionality**.

  

Today we have lots of ways to test code, but ultimately, **a test is just some code that checks that other code is doing what it's meant to**.

Broadly speaking, there are two major types of tests: **unit tests**, and [**integration tests**](http://softwaretestingfundamentals.com/integration-testing/). This lesson will focus on **unit tests**.