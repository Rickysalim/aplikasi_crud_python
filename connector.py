import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  port=3306,
  user="root",
  password="root",
  database="magang"
)

db = mydb.cursor()

# db.execute("select * from record_data")

# res = db.fetchall()

# for x in res:
#   print(x)