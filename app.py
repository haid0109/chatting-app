import psycopg2

try:
    con = psycopg2.connect(
        host = 'localhost',
        port = 8624,
        database = 'chattingApp',
        user = 'haidar',
        password = 'Passw0rd'
    )
    cur = con.cursor()
except Exception as error:
    print(f'could not connect to database: {error}')

try:
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users(
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL,
        password VARCHAR(50) NOT NULL
        );'''
    )
except Exception as error:
    con.rollback()
    print(f'could not create table users: {error}')

cur.close()
con.close()
