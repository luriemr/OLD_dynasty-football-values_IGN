import sqlite3

conn = sqlite3.connect('/Users/mr_lurie/Desktop/fantasytrial.db')

cursor = conn.cursor()

for row in cursor.execute("SELECT player, value_1qb from dyno"):

	print("player = ", row[0])
	print("value_1qb = ", row[8], "\n")

conn.commit()
conn.close()
