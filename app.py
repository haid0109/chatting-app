import psycopg2

con = psycopg2.connect(
    host = 'localhost',
    port = 8624,
    database = 'chattingApp',
    user = 'haidar',
    password = 'Passw0rd'
)



con.close()
