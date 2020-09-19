import pandas as pd
import sqlite3

df = pd.read_csv('titanic.csv')
print(df.shape)

df.columns = ['Survived', 'Pclass', 'Name', 'Sex', 'Age', 'Sibs_Spouse', 'Parent_Child', 'Fare']
print(df.head())

conn = sqlite3.connect('titanic.sqlite3')

df.to_sql('titanic', con=conn, if_exists='replace')

cursor = conn.cursor()
cursor.execute('SELECT * FROM titanic;').fetchall()