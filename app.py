from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",        
    database="charity_tracker"
)

cursor = db.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    amount = request.form['amount']

    #  this is written by me so that I can remember that it was for Insertion into database
    sql = "INSERT INTO donations (name, email, amount) VALUES (%s, %s, %s)"
    val = (name, email, amount)
    cursor.execute(sql, val)
    db.commit()

    return "Thank you for your donation, " + name + "!"

if __name__ == '__main__':
    app.run(debug=True)
