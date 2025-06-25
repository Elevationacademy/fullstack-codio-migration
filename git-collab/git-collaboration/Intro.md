Now that we know how to use version control properly with committing changes, creating branches, push to our remote, and merging branches, we can move on to git collaboration!

  

This lesson will explain how to properly collaborate on projects through git and github. We'll cover:

-   Git collaboration methodology
-   How to add collaborators to a repo
-   Working on separate branches
-   Fetching
-   Pulling
-   Pull requests
-   Handling merge issues

  

----------

  

#### **BAD GIT COLLABORATION**

  

They key to git collaboration is separation of concerns. Having multiple people work on the same project can be messy. Imagine the following scenario:

-   Cindy and John are working together on a project, building a new landing page. The page already has a navbar
-   Cindy changes the name of some of the navbar buttons while working on her feature
-   John is changing the design and doesn't know that Cindy changed a couple navbar names
-   They are both working on master so all hell breaks loose when they try to push because there are conflicting changes, and until the mess is sorted out, the company is without a clean landing page.

  

Had Cindy and John worked on separate branches that would have helped a bit, but if they worked on the same feature, they still would have issues when trying to merge back into the `master` branch.