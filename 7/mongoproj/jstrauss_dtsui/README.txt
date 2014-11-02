Justin Strauss and Derek Tsui
Software Development Period 7
MongoDB Project

This project is an account manager with the following pages:

1. A login page - /login
2. A logout route that logs you out and brings you back to index - /logout
3. A register page - /register
4. At least one page that can be viewed without logging in - /index
5. At least 2 pages that can only be viewed if you are logged in. - /profile and /contacts

If you're logged in, all pages indicate this by displaying your username in the upper left hand corner along with a link to logout. If you’re logged out, the upper left hand corner will simply say “Account Manager” along with a link to the login page.

If you go to a protected page and you're not logged in, it redirects you to the login page. Once you log in (or register then login) it redirects you back to the protected page.

The protected profile page allows you to change your account password.

Tools used in addition to basic Flask:

1. Mongo to store the accounts - username, password, and email.
2. Sessions - to keep track of the state.
3. Flashing - to display one time error messages like invalid password.