import mysql.connector
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
db = mysql.connector.connect(
    host="mysql",
    user="user",
    password="password",
    database="mydb"
)

@app.route('/')
def index():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM mytable")
    data = cursor.fetchall()
    return render_template('index.html', data=data)

@app.route('/add', methods=['POST'])
def add():
    cursor = db.cursor()
    name = request.form['name']
    value = request.form['value']
    cursor.execute("INSERT INTO mytable (name, value) VALUES (%s, %s)", (name, value))
    db.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)