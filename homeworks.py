import mysql.connector as mysql
import datetime
from prettytable import from_db_cursor

## connecting to the database using 'connect()' method
## it takes 3 required parameters 'host', 'user', 'passwd'
db = mysql.connect(
    host = "localhost",
    user = "drupad",
    passwd = "root",
    database= "homeworks"
)

print("welcome to the homework app devloped by Aaryan Sinha Roy \n This is the pro version in which you can store infinite number of homeworks")
print("press n for new howmwork \n press v for view all homeworks")
cursor = db.cursor()

def newHomework():
    sub=input("enter subject ")
    hwinfo=input("enter homework info ")
    startdate=datetime.datetime.now()
    enddate=input("enter end date ")
    sql = "INSERT INTO srno (subject, hw_info, startdate, enddate) VALUES (%s, %s, %s, %s)"
    val = (sub,hwinfo,startdate,enddate)
    cursor.execute(sql, val)
    db.commit()
    print("record sucessfully created")


def viewRecords():
    print("Here are all your pending homeworks \n ")
    cursor.execute("SELECT * FROM srno")
    #results=cursor.fetchall()
    leresults=from_db_cursor(cursor)
    #for x in results:
    print(leresults)
    print("\n \n please complete your pending homeworks")

inp =input()
if inp=="n":
    newHomework()
elif inp=="v":
    viewRecords()
else:
    print("you shouldnt have clicked it")
