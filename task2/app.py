import os
import sqlite3
from flask import Flask,render_template,request,redirect,session,url_for
from werkzeug.security import generate_password_hash,check_password_hash

app=Flask(__name__)

app.secret_key="secure-secret-key"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "database.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

init_db()

def get_db():
    conn=sqlite3.connect(DB_PATH)
    
    # this line tells sqlite to return each row as dictionary like object instead of tuple
    #allows you to access columns by column name
    conn.row_factory=sqlite3.Row
    return conn

@app.route('/register',methods=['GET','POST'])
def register():
    
    if request.method=='POST':
        username=request.form['username']
        password=generate_password_hash(request.form['password'])
        db=get_db()
        db.execute(
            "INSERT INTO users(username,password)VALUES(?,?)",
            (username,password)
        )
        db.commit()
        return redirect('/login')
    return render_template('register.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']

        db=get_db()

        user=db.execute(
            "SELECT * FROM users WHERE username=?",(username,)
        ).fetchone()
        # fetchone() retrieves the one next row

        if user and check_password_hash(user['password'],password):
            session['user']=user['username']
            # This stores the username in the Flask session.
            return redirect('/dashboard')

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/login')
    return render_template('dashboard.html',user=session['user'])

@app.route('/logout')
def logout():
    session.pop('user',None)
    return redirect('/login')

if __name__=='__main__':
    app.run(debug=True)