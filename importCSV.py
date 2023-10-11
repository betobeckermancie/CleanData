import sqlite3

connection = sqlite3.connect("Limpieza.db")
cursor = connection.cursor()

with open ('data.csv', 'r') as file
records = 0

for row in file:
    cursor.execute("INSERT INTO  ")
