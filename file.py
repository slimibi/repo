from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'mydatabase'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route('/')
def users():
    cur = mysql.connection.cursor()
    cur.execute('''USE mydatabase''')
    cur.execute('''SHOW TABLES FROM mydatabase''')
    cur.execute('''SHOW COLUMNS FROM Attestation FROM mydatabase''')
    cur.execute('''SHOW COLUMNS FROM Etudiant FROM mydatabase''')
    cur.execute('''SHOW COLUMNS FROM Convention FROM mydatabase''')
    rv = cur.fetchall()
    return str(rv)

if __name__ == '__main__':
    app.run(debug=True)