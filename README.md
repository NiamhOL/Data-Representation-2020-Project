# Data-Representation-2020-Project

This project focuses on the creation of a educational company webpage that medical education courses for students.

### Contents of Github repository in alphabetical order
|File Name | Description                                |
|----------|--------------------------------------------|
| ConFigureDatabase.py |
| CreateDatabase.py | create a table containing students |
| Data Rep Project References | references used in this project |
| InsertIntoTable.py  | insert a row into the student table |
| MeducateClassSchedule | webpage showing the class schedule
| MeducateContact.js | webpage showing contact details and allows user to ask a question |
| MeducateCourse.html | webpage showing course details |
| MeducateStudentMembership.html | webpage with CRUD interface for interacting with database |
| MeducateStylePage.html | generic style page for webpage |
| Meducatecontact.html | webpage with contact details |
| Meducatehome.html | homepage |
| Meducatelogin.html | webpage allowing student to login |
| Project Description.pdf | Outline of Data Representation Project 2020 |
| README.md | The file that briefly describes the project |
| StudentsDAO.py | Data Access Object file for interacting with the student database |
| StudentsServer.py | Web server for local gost and Python Anywhere |
| clients.csv | "client" numbers |
| steth.png | picture used in webpage |

## How to download the repository:
1. Download the repository from the following link <a href=https://github.com/NiamhOL/Data-Representation-2020-Project>Click here</a>  
2. Click the clone or download button towards the right of your screen
3. Download and unzip this file. Save the unziped file to a location on your desktop where it is easily accessible
4. Open the command line and navigate to the location of your downloaded file using a series of cd commands 

### Run virtual machine
1. Once you have navigated to the location of your folser using a series of cd commands. Please do the following commands:

```
 python -m venv venv 
 .\venv\Scripts\activate.bat
 set FLASK_APP=studentserver
 set FLASK_ENV=development
 set FLASK_DEBUG=1
 echo %FLASK_APP%
 flask run
 ```
 
2. Copy the url to the web browser: to view the membership should appear like :http://127.0.0.1:5000/membership.html   to view the general website http://127.0.0.1:5000/Meducatehome.html  and using the tabs we can navigate through the different tabs
3. Once you reach the login screen enter usernname: and password: 

## Python Anywhere:

Python Anywhere can be accessed at the following link
 * Again you will arrive at the login page and the same username and password should be used. 
 Please enter the following:
   
      * username
      * password
      
 * I have promted this in this situation but this would be removed in a normal situation.  
 * If the incorrect username or password is entered the user will not be able to enter the website until they enter the correct credentials.
 * If you would like to view my work for python anywhere my creddentials are the following:
 
      * email 
      * username
      * password
      
 * I added a module to the service on the host: added corrs - again this can be viewed by loggining into the python anywhere website. 


### MySQL Database 

#### MySQL command to creeate table 
```
 CREATE TABLE members(
       id int NOT NULL AUTO_INCREMENT,
       email VARCHAR(255),
       membershipPlan VARCHAR(20),
       startDate DATE,
       age INT,
       PRIMARY KEY(id)
       );
```

DESC members;

| Field          | Type         | Null | Key | Default | Extra          |
|----------------|--------------|------|-----|---------|----------------|
| id             | int(11)      | NO   | PRI | NULL    | auto_increment |
| email          | varchar(255) | YES  |     | NULL    |                |
| membershipPlan | varchar(20)  | YES  |     | NULL    |                |
| startDate      | date         | YES  |     | NULL    |                |
| age            | int(11)      | YES  |     | NULL    |                |


#### MySQLommand to insert row into table 

insert into students (email, membershipPlan, startDate, age) values ("maryryan@yahoo.ie","Daily", "2020-12-11", 21)

insert into students (email, membershipPlan, startDate, age) values ("jameskelly@yahoo.ie","Annually", "2020-11-30", 30)

insert into students (email, membershipPlan, startDate, age) values ("johnbsmith@gmail.com","Daily", "2020-12-20", 18)

insert into students (email, membershipPlan, startDate, age) values ("sarahobrien@gmail.com","Monthly", "2020-12-08", 27)


| id | email                     | membershipPlan | startDate     | age  |
|----|---------------------------|----------------|---------------|------|
|  1 | maryryan@yahoo.ie         | Daily          | 2020-12-11    |  21  |
|  2 | jameskelly@yahoo.ie       | Annually       | 2020-11-30    |  30  |
|  3 | johnbsmith@gmail.com      | Daily          | 2020-12-20    |  18  |
|  4 | sarahobrien@gmail.com     | Monthly        | 2020-12-08    |  27  |  

