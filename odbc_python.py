import pyodbc 
import pandas as pd

connection = pyodbc.connect('Driver={SQL Server};'
                      'Server=Server;'
                      'Database;'
                      'Trusted_Connection=yes;')

cursor = connection.cursor()
query = cursor.execute('SELECT * FROM [Server].[dbo].[Database]')
table = pd.DataFrame(query)
print(table)
