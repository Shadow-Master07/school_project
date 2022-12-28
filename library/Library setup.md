# Setup:-
	- create a new user by logging into the root user
	- new user name should be "shaktiman"
	- new user password should be "12345"
	- host should be localhost
	To make everything work properly, work it out and setup these basic things

```tex
When you have done the setup, then you have to login into the "shaktiman"
account, either using command line or by using GUI.

if on command line run the following command:-
	this is for logging into the account;
		mysql -u shaktiman -p 12345
		then press enter

	Then after the logging in, you have to have your sql file's location 
	in your drive and copy it. Now run this command
		source [paste the path here without these brackets]
	and press enter, the commands will run and your table and database 
	will be created

if on GUI follow this:-
	Login as your do for the root user;
	
	Now, click on sql+ button just below the file tab on top left corner
	of the mysql workbench;
	
	A window pops open, and has the name, SQL file {some number}, just below
	that button there is a folder option, click that and navigate to the 
	directory of that sql file and open it;
	
	Now close to the folder opening button we used, there is a lighting flash 
	button in golden yellow color, click that and it will create and setup 
	the database;
```

## <u>Usage</u>:-

```bash
# Run the program using command line after setting up 
python <file.py>

```

### NOTE:-
	When you have created the table, there is no data in it, so when running python file 
	for the first time and selecting to show, there will be no output so don't panic