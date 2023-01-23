import pyodbc 
import pandas as pd

connection = pyodbc.connect('Driver={SQL Server};'
                      'Server=DB01;'
                      'VINONLINE;'
                      'Trusted_Connection=yes;')

cursor = connection.cursor()
query = cursor.execute('SELECT * FROM [VINONLINE].[dbo].[Vehicle]')
table = pd.DataFrame(query)
print(table)