import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Happy999",
  #user="datarep",  
  #passwd="password" 
  database="datarepresentation"
)

cursor = db.cursor()
sql="insert into members (email, membershipPlan, startDate, age) values (%s,%s,%s,%s)"

values = ("maryryan@yahoo.ie","Daily", "2020-12-11", 21)
values = ("jameskelly@yahoo.ie","Annually", "2020-11-30", 30)
values = ("johnbsmith@gmail.com","Daily", "2020-12-20", 18)
values = ("sarahobrien@gmail.com","Monthly", "2020-12-08", 27)

cursor.execute(sql, values)

db.commit()
print("1 record inserted, ID:", cursor.lastrowid)