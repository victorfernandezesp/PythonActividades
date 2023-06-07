import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="Root1234$"
)
mycursor = mydb.cursor()

nombre_bd = 'holaa'
mycursor.execute(f'use {nombre_bd}')

tabla_bd = 'CUSTOMERS'
mycursor.execute(f"INSERT INTO {tabla_bd} VALUES('87654321O', 'ccc', 'dasdfdsafdasfdsfas', '123456123');")
mycursor.execute("SELECT * FROM CUSTOMERS")
myresult = mycursor.fetchall()
for i in myresult:
  print("---------------------------------")
  print(f"DNI: {i[0]}")
  print(f"NOMBRE: {i[1]}")
  print(f"DIRECCION: {i[2]}")
  print(f"NUMERO DE CONTACTO: {i[3]}")
print("---------------------------------")

