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

try:
    cur.execute('''
        INSERT INTO
        "users" ("username", "password")
        values (%s, %s)
        ;''', ('haidar2', 'Passw0rd')
    )
except Exception as error:
    con.rollback()
    print(f'could not insert user into user table: {error}')

try:
    cur.execute('''
        SELECT "id", "username", "password"
        FROM "users"
        ;'''
    )
    rows = cur.fetchall()
    for row in rows:
        print(f'''id {row[0]}\n username {row[1]}\n password {row[2]}\n''')
except Exception as error:
    con.rollback()
    print(f'could not fetch users: {error}')

con.commit()
cur.close()
con.close()
