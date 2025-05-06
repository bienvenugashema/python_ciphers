from flask import Flask, render_template, redirect, session, request
import sqlite3
from datetime import datetime
app = Flask(__name__)

def inti_db():
    with sqlite3.connect("blog.db") as conn:
        conn.execute('''CREATE TABLE  IF NOT EXISTS comments (id INTEGER PRIMARY KEY AUTOINCREMENT , 
                     name VARCHAR(200), 
                     email VARCHAR(200) UNIQUE, 
                     comment VARCHAR(3000)
                     )''')
        


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contacts")
def contacts():
    return render_template("contacts.html")

@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/send_message", methods=['POST'])
def send_message():
    name = request.form['names']
    email = request.form['email']
    comment = request.form['comment']

    with sqlite3.connect("blog.db") as conn:
        fin = conn.execute("INSERT INTO comments (name, email, comment) values (?,?,?)", (name, email, comment))
        if fin:
            message = {"text": "Message send well created succesfullt", "category": "success"}
            return render_template("contacts.html", message=message)
        else:
            message - {"text": "Failed to send comment", "category": "danger"}
            return render_template("contacts.html", message=message)
        
@app.route("/dashboard")
def dashboard():
    #to get users
    with sqlite3.connect("blog.db") as conn:
        search = conn.execute("select * from comments")
        comments= search.fetchall()
        total_comments = len(comments)
        unique_users = len(set(comment[1] for comment in comments))
        
        return render_template("dashboard.html",
                               comments=comments,
                               total_comments=total_comments,
                               unique_users=unique_users,
                               page_title="Admin Dashboard",
                               current_time=datetime.now())
    
@app.route("/delete")
def delete():
    comment_id = request.args.get('id')
    try:
        with sqlite3.connect("blog.db") as conn:
            delete = conn.execute("delete from comments where id = ?", (comment_id,))
            if delete:
                response = {"text": "Comment deleted well", "category": "success"}
                conn.commit()
                return redirect("/dashboard")
            else:
                response = {"text": "Comment not deleted", "category": "danger"}
                return render_template("dashboard.html", response)
    except Exception as e:
        message = {"text": f"Failed to delete comment: {str(e)}", "category": "danger"}
        return redirect("/dashboard")


@app.route("/update")
def update():
    id = request.args.get('id')
    with sqlite3.connect("blog.db") as conn:
        res = conn.execute("select * from comments where id = ?", (id, ))
        user = res.fetchone()
        name = user[1]
        email = user[2]
        comment = user[3]



    return render_template("update.html", names=name, email=email, comment=comment, id=id)

@app.route("/update_comment", methods=['POST', "GET"])
def update_comment():
    id = request.form.get('id')
    name = request.form.get('names')
    email = request.form.get('email')
    comment = request.form.get('comment')
    with sqlite3.connect("blog.db") as conn:
        res = conn.execute('''UPDATE comments
                           set name=?, email=?, comment=? where id= ?''', (name, email, comment,id,  ))
        conn.commit()
        if res:
            messages = {"text": "User upated well", "category": "success"}
            return render_template("dashboard.html", messages=messages)
        else:
            return redirect("/dashboard")
    return redirect("/dashboard")


if __name__=="__main__":
    inti_db()
    app.run(debug=True)