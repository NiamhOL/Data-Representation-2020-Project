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


## Run virtual machine

Once you have navigated to the location of your folder using a series of cd commands. Please following:

# Data-Representation-Project-2019

## How to download the repository:
1. Download the repository from the following link <a href=https://github.com/NiamhOL/Data-Representation-2020-Project>Click here</a>  
2. Click the clone or download button towards the right of your screen
3. Download and unzip this file. Save the unziped file to a location on your desktop where it is easily accessible
4. Open the command line and navigate to the location of your downloaded file using a series of cd commands 

### Run virtual machine
1. Once you have navigated to the location of your folser using a series of cd commands. Please do the following commands:
 *  python -m venv venv 
 * .\venv\Scripts\activate.bat
 * set FLASK_APP=memberserver
 * set FLASK_ENV=development
 * set FLASK_DEBUG=1
 * echo %FLASK_APP%
 * flask run
 
2.  Copy the url to the web browser: to view the membership should appear like :   to view the general website   and using the tabs we can navigate through the different tabs
3. Once you reach the login screen enter usernname:andrew and password: andrew


## Python Anywhere:

Python Anywhere can be accessed at the following link
 * Again you will arrive at the login page and the same username and password should be used. 
 <b> Please enter the following:
   
      * username: 
      * password: 
      
 * I have promted this in this situation but this would be removed in a normal situation.  
 * If the incorrect username or password is entered the user will not be able to enter the website until they enter the correct credentials.
 * If you would like to view my work for python anywhere my creddentials are the following:
 
      * email: 
      * username:
      * password: 
      
 * I added a module to the service on the host: added corrs - again this can be viewed by loggining into the python anywhere website. 


### MySQL Database 

#### MySQLommand to creeate table 

 CREATE TABLE members(
       id int NOT NULL AUTO_INCREMENT,
       email VARCHAR(255),
       membershipPlan VARCHAR(20),
       startDate DATE,
       age INT,
       PRIMARY KEY(id)
       );


DESC members;

| Field          | Type         | Null | Key | Default | Extra          |
|----------------|--------------|------|-----|---------|----------------|
| id             | int(11)      | NO   | PRI | NULL    | auto_increment |
| email          | varchar(255) | YES  |     | NULL    |                |
| membershipPlan | varchar(20)  | YES  |     | NULL    |                |
| startDate      | date         | YES  |     | NULL    |                |
| age            | int(11)      | YES  |     | NULL    |                |


#### MySQLommand to insert row into table 

insert into members (email, membershipPlan, startDate, age) values ("marygarcia@gmail.com","Monthly", "2018-07-24", 23)

insert into members (email, membershipPlan, startDate, age) values ("jameskelly@yahoo.ie","Annually", "2018-11-02", 30)

insert into members (email, membershipPlan, startDate, age) values ("johnbyrne@gmail.com","Daily", "2019-02-12", 19)

| id | email                     | membershipPlan | startDate  | age  |
|----|---------------------------|----------------|------------|------|
|  1 | marygarcia@gmail.com      | Monthly        | 2018-07-24 |   23 |
|  2 |  jameskelly@yahoo.ie      | Annually       | 2018-11-02 |   30 |
|  3 |  johnbyrne@gmail.com      | Daily          | 2019-02-12 |   19 |
