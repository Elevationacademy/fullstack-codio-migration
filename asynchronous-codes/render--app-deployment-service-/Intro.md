
The time has come for us to release our applications out into the wild! Deploying our applications live can be a fairly complex endeavour, but Render will make it easier.

  
[Render](https://www.render.com) is a "Cloud Application Platform" or PaaS (Platform as a Service). It allows us to build and run our applications in the cloud. It manages hosting our files, serving them, and running drivers to manage our databases as well. Any one of these things can be difficult, but Render makes it easy.

When we deploy a full-stack application we are faced with two main options:
1. **Single repository**. Creating and deploying the server and client in a single repository.
1. **Separate (two) repositories**. Creating and deploying the server and client separately using 2 repositories. 

As always, there are pros and cons for each approach. This guide will focus on the separate repositories approach. We will start with deploying the server side (with a MongoDB), and then discuss how to deploy the client (React) side.
