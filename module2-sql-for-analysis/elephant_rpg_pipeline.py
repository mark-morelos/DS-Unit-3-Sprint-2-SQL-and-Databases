import psycopg2

DB_NAME = 'yxonkvmp'
DB_USER = 'yxonkvmp'
DB_PASS = '6V84LRTxRrzrkW09nb69QigNUhoRvy-_'
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

#### Connect to SQLite DB for RPG Data ####

import sqlite3

sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_cursor = sl_conn.cursor()
characters = sl_cursor.execute('SELECT * FROM charactercreator_character;').fetchall()
# print(characters)

#### Create the Character Table in Postgres and Insert Data ####

create_character_table_query = '''
CREATE TABLE IF NOT EXISTS rpg_characters (
    character_id SERIAL PRIMARY KEY,
    name VARCHAR(30),
    level INT,
    exp INT,
    hp INT,
    strength INT, 
    intelligence INT,
    dexterity INT,
    wisdom INT
)
'''
cursor.execute(create_character_table_query)
conn.commit()

for character in characters:
    insert_query = f'''INSERT INTO rpg_characters
    (character_id, name, level, exp, hp, strength, intelligence, dexterity, wisdom) VALUES
    {character}
    '''
    cursor.execute(insert_query)
conn.commit()