import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="Dinesh", passwd="1234",database="dinesh")
mycursor = mydb.cursor()
mycursor.execute("select * from student")

#result = mycursor.fetchall()
result = mycursor.fetchone()
print(result)

print("Hello")
print("hai")

print("bye")
