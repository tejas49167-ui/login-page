from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("user.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            a TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        a = request.form["a"]

        # Save into DB
        conn = sqlite3.connect("user.db")
        c = conn.cursor()
        c.execute("INSERT INTO users (name, a) VALUES (?, ?)", (name, a))
        conn.commit()
        conn.close()
        return "You got blue tick check your account"
       
    return render_template("index.html")
@app.route("/show")
def show():
    conn = sqlite3.connect("user.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    data = c.fetchall()
    conn.close()
    return str(data)  


if __name__ == "__main__":
    app.run(debug=True)
