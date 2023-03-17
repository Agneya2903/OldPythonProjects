import pyodbc

conn = pyodbc.connect(
    "Driver={SQL Server};"
    "Server=LAPTOP-MBL9B7IP\SQLEXPRESS;"
    "Database=Testing_43;"
    "Trusted_Connection=yes;"
)
cursor = conn.cursor()
cursor.execute("Select * From Information_Schema.Columns Where TABLE_NAME ='Emp_Details'")
cursor.execute("select *, SUM(E_Salary) Over (Partition BY Gender order by E_Salary)As Running_Salary,"
               "MIN(E_Salary) Over (Partition BY Gender) As MIN_SALARY,"
               "MAX(E_Salary) Over (Partition BY Gender) As Max_SALARY,"
               "Count(E_Salary) Over (Partition By Gender)AS Total_SAL_Count From Emp_Details;")

for row in cursor:
    print(row)

conn.close()
