from flask import Flask, render_template, redirect, request
import hashlib
import sqlite3
app = Flask(__name__)

#creating a databse model
def init_db():
    with sqlite3.connect("auth.db") as conn:
        conn.execute('''
    CREATE TABLE  IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT , 
                     email VARCHAR(200) NOT NULL, 
                     password VARCHAR(200) NOT NULL )
                     
''')
        conn.commit()
        



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("index.html")

@app.route("/register", methods=['POST', 'GET'])
def register():
    email = request.form.get("email")
    password = request.form.get("password")
    confirm_password = request.form.get("confirm_password")
    if password == confirm_password:
        with sqlite3.connect("auth.db") as conn:
            conn.execute("insert into users values (email=?,passord=?)", (email, password,))
            message = {"text": "Registered well", "category": "success"}
            return render_template("index.html", messages=message)
    else:    
        message = {"text":"Pasword are not the same", "category": "danger"}
        return render_template("register.html", messages = message)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)