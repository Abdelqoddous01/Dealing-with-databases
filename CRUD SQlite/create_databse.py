import sqlite3


connection =sqlite3.connect('exemple.db')

#create a cursor

c = connection.cursor()

#create the table

c.execute("CREATE TABLE table_name (column1 Type,column2 type ...)")

#commit the command

connection.commit()

#close the connection 

connection.close() #the connection will close automatecly but it is a good practice to close it manualy