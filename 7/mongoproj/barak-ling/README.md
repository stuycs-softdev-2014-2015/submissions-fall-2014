Account Manager Project.
Will have the following pages:

1. A login page
2. A logout page
3. A register page
4. At least one page that can be viewed without logging in
5. At least 2 pages that can only be viewed if you are logged in.

All pages should indicate if you're logged in or not by displaying either the username or a link to the login page.

If you go to a protected page and you're not logged in, it should redirect you to the login page. Once you log in (or register / login) it should redirect you back to the protected page.

-Would be nice if one of the protected pages is a change account specifics page.

-Might also want to track things like last login or logout or something like that.

Things needed in addition to basic flask stuff:

1. Mongo to store the accounts -- username and password is a minimum but you might want to track other info.
2. Sessions - to keep track of your state.
3. You might want to look at flash/flashing in the flask docs - it'll make it easy to do things like displaying one time error messages like invalid password.