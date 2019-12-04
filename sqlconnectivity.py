import mysql.connector
def connect_db():
    mydb = mysql.connector.connect(host="localhost",user="to96",password="212207@Pin",database="weather")
    cursor = mydb.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS report1(mobile_num varchar(13),city_name  varchar(30),name VARCHAR(30),Date varchar(15),time varchar(5),temp_description varchar(50),temperature varchar(5) )")
    mydb.commit()
    mydb.close()

def insert(num,city,name,Date,time,desc,temp):
    connect_db()
    mydb = mysql.connector.connect(host="localhost",user="XXXXx",password="XXXXX",database="weather")
    cursor = mydb.cursor()
    query = "INSERT INTO report1 (mobile_num, city_name, name, Date,time, temp_description,temperature) VALUES (%s, %s, %s ,%s,%s,%s ,%s)"
    value = (num , city , name ,Date, time, desc , temp)
    cursor.execute(query,value)
    mydb.commit()
    mydb.close()

def view_all():
    mydb = mysql.connector.connect(host="localhost",user="to96",password="212207@Pin",database="weather")
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM report1")
    rows = cursor.fetchall()
    mydb.commit()
    mydb.close()
    return rows

connect_db()
