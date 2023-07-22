import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'Bhargavi@1404'

	)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE CustomerRelations")

print("All set!")
 