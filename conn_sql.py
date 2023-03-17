import pyodbc

conn = pyodbc.connect(
    "Driver={SQL Server};"
    "Server=LAPTOP-MBL9B7IP\SQLEXPRESS;"
    "Database=Testing_43;"
    "Trusted_Connection=yes;"
)
cursor = conn.cursor()
cursor.execute("Select * From Employee")

for row in cursor:
    print(row)

conn.close()
