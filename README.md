# Data-Representation-2020-Project

This project focuses on the creation of a educational company webpage that provides a variety of medical education courses for students.

### Contents of Github repository in alphabetical order
|File Name | Description                                |
|----------|--------------------------------------------|
| ConFigureDatabase.py |
| CreateDatabase.py | create a table containing students |
| InsertIntoTable.py  | insert a row into the student table |
| MeducateClassSchedule | webpage showing the class schedule
| MeducateContact.js | webpage showing contact details and allows user to ask a question |
| MeducateCourse.html | webpage showing course details |
| MeducateStudentMembership.html | webpage with CRUD interface for interacting with database | Data Rep Project References.doc | project references |
| MeducateStylePage.html | generic style page for webpage |
| Meducatecontact.html | webpage with contact details |
| Meducatehome.html | homepage |
| Meducatelogin.html | webpage allowing student to login |
| Project Description.pdf | Outline of Data Representation Project 2020 |
| README.md | The file that briefly describes the project |
| MemberDAO.py | Data Access Object file for interacting with the student database |
| MemberServer.py | Web server for local gost and Python Anywhere |
| clients.csv | "client" numbers |
| requirement.txt | pip install items |
| Flask.png | picture of FLASK |
| SQL.png| picture of SQL database |
| steth.png | picture used in webpage |
| Scripts folder | containing .exe files non-system processes |

## How to download the repository:
1. Download the repository from the following link <a href=https://github.com/NiamhOL/Data-Representation-2020-Project>Click here</a>  
2. Click the clone or download button towards the right of your screen
3. Download and unzip this file. Save the unziped file to a location on your desktop where it is easily accessible
4. Open the command line and navigate to the location of your downloaded file using a series of cd commands 

## Overview of the project
The data is stored in a MySQL database.
The database queries are defined using the MemberDAO.py database access object.
The MemberServer.py application server calls the queries and returns the results as JSON objects.
AJAX calls are made in the html files and the results are displayed in tables

### Run virtual machine
1. Once you have navigated to the location of your folder using a series of cd commands. Please do the following commands:

```
 python -m venv venv 
 .\venv\Scripts\activate.bat
 set FLASK_APP=memberserver
 set FLASK_ENV=development
 set FLASK_DEBUG=1
 echo %FLASK_APP%
 flask run
 ```
 ![image](https://raw.githubusercontent.com/NiamhOL/Data-Representation-2020-Project/main/Flask.PNG)
 
 
2. Copy the url to the web browser: to view the membership should appear like :http://127.0.0.1:5000/membership.html   to view the general website http://127.0.0.1:5000/Meducatehome.html  and using the tabs we can navigate through the different tabs



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
![image](https://raw.githubusercontent.com/NiamhOL/Data-Representation-2020-Project/main/SQL.PNG)

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

## Author
Niamh O'Leary for HDip in Data Analytics 2019/2020.

## Licence
This project is licensed under the GNU General Public License v3.0 - see the LICENSE.md file for details.
