# Budget-Analyser
A simple web application for uploading and tracking your finances 

To start the application run Main.py file.

When starting the application you will be presented with the user login page where you have the options to eithe rcreate your own account or use:

- email - ekundayo93@gmail.com 
- user - tester 
- password - tester1

To access the application then you will be automaticly redirected to the user home-page and a menu tab where you can choose to either:
- Upload a file
- view finial data 
- Manually insert finacial data 
- Login/logout

The Database used with the application is SQLITE3, to view sql alqamy datbase created run this in terminal - sqlite3 database.db , select * from User;

The code is basicly built to take the csvfile(bank statments) of a user that gets uploaded through the flask app and run a anlaysis using a clasifyer to catagorise the transactions into spending catogories and display that back on the flask website, but im yet to figure this part out yet.
