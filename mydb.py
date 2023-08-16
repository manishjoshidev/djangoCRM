import mysql.connector
dataBase=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='admin'

)
#prepare a cursopr object
cursorObject=dataBase.cursor()
#create a database
cursorObject.execute("CREATE DATABASE elderco")
print("All Done")