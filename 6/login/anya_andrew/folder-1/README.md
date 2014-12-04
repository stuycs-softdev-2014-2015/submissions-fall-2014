Mongo Login
===
app.py varibles:
  loggedIn bool
  lastPage str
  

Database contains:
   userData
     |-userName
     |-password
     |-firstName
     |-lastName
     |-email
     

-----

Folks,

Here's the mini project. 

You'll work with one partner (your choice) - put the stuff under submissions and make sure the folder name and or README specifies who the group is comprised of.

At the end of tomorrow (Wednesday) I need each class to self assess and have one person email me with an overall status and how much more lab time you'l need (assuming a due date of Monday).

I'm expecting you to self organize and take care of this.

The project is an account manager. You'll need the following pages:

1. A login page
2. A logout page
3. A register page
4. At least one page that can be viewed without logging in
5. At least 2 pages that can only be viewed if you are logged in.

All pages should indicate if you're logged in or not by displaying either the username or a link to the login page.

If you go to a protected page and you're not logged in, it should redirect you to the login page. Once you log in (or register / login) it should redirect you back to the protected page.

It would be nice if one of the protected pages is a change account specifics page. You might also want to track things like last login or logout or something like that.

Things you'll need in addition to basic flask stuff:

1. Mongo to store the accounts -- username and password is a minimum but you might want to track other info.
2. Sessions - to keep track of your state.
3. You might want to look at flash/flashing in the flask docs - it'll make it easy to do things like displaying one time error messages like invalid password.

You'll probably want to re-use this in future projects so try to write it in a clean / modular way.

MZ


-- 
http://cestlaz.github.com
_______________________________________________
SoftDev mailing list
SoftDev@mailman.cstuy.org
http://mailman.cstuy.org/cgi-bin/mailman/listinfo/softdev