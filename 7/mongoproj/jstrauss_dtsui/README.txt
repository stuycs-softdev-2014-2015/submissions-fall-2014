Justin Strauss and Derek Tsui
Software Development Period 7
MongoDB Project

This project is an account manager with the following pages:

1. A login page - /login
2. A logout route that logs you out and brings you back to index - /logout
3. A register page - /register
4. At least one page that can be viewed without logging in - /index
5. At least 2 pages that can only be viewed if you are logged in. - /profile and /contacts

If you're logged, all pages indicate this by displaying your username in the upper left hand corner along with a link to logout. If you’re logged out, the upper left hand corner will simply say “Account Manager” and along with a link to the login page.

If you go to a protected page and you're not logged in, it redirects you to the login page. Once you log in (or register then login) it redirects you back to the protected page.

It would be nice if one of the protected pages is a change account specifics page. You might also want to track things like last login or logout or something like that.

Tools used in addition to basic Flask:

1. Mongo to store the accounts -- username and password is a minimum but you might want to track other info.
2. Sessions - to keep track of your state.
3. You might want to look at flash/flashing in the flask docs - it'll make it easy to do things like displaying one time error messages like invalid password.