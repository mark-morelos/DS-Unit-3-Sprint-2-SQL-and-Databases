import psycopg2

DB_NAME = 'zninzmrd'
DB_USER = 'zninzmrd'
DB_PASS = 'iOj0vECcKLDZ50DdidwUHsdkVzGj62KX'
DB_HOST = 'lallah.db.elephantsql.com'

# Connect to ElephantSQL - hosted PostgreSQL DB
conn = psycopg2.connect(dbname=DB_NAME,
                        user=DB_USER,
                        password=DB_PASS,
                        host=DB_HOST)

cursor = conn.cursor()

cursor.execute("SELECT * from test_table;")

results = cursor.fetchall()
# print(results)

#### Connect to SQLite DB for TITANIC Data ####

import sqlite3

sl_conn = sqlite3.connect('titanic.sqlite3')
sl_cursor = sl_conn.cursor()
passengers = sl_cursor.execute('SELECT * FROM titanic;').fetchall()
# print(passengers)

create_passenger_table_query = '''
CREATE TABLE IF NOT EXISTS titanic_passenger_list (
    index SERIAL PRIMARY KEY,
    Survived INT,
    Pclass INT,
    Name VARCHAR(30),
    Sex VARCHAR(6),
    Age FLOAT(4),
    Fare FLOAT(8)
)
'''
cursor.execute(create_passenger_table_query)
conn.commit()

for passenger in passengers:
    insert_query = f'''INSERT INTO titanic_passenger_list
    (index, Survived, Pclass, Name, Sex, Age, Fare)VALUES
    {passenger}
    '''
    cursor.execute(insert_query)
conn.commit()