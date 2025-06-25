Authentication is a concept that relates to the question ‘what users can do once they are logged in’. Authorization deals with initial access using their credentials (*username* and *password*), and authentication deals with what permission does the user have once they are logged in.

In general, a simple way to support authentication is by extending the `User` model from previous sections with a `permission` list or dictionary. Then the only thing you need to do in each endpoint, is query for the right permission, if the user’s object contains the relevant permission, they will be allowed to execute the endpoint, and if not, a 403 error will be raised.

The 403 error code is also of type `status.HTTP_403_FORBIDDEN` which specifically relates to authentication errors.
