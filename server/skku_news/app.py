from flask import Flask, render_template, session, url_for, redirect, request, jsonify, flash
from datetime import timedelta
from db_utils import Database

app = Flask(__name__)
app.secret_key = "skku_news"
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=10)
db = Database()

@app.route("/login", methods=("GET", "POST",))
def login():
    if request.method == "POST":
        session["id"] = request.form["id"]
        
        return redirect(url_for("main"))
    
    return render_template("login.html")


@app.route("/register", methods=("GET", "POST",))
def register():
    if request.method == "POST":
        id = request.form["id"]
        pwd = request.form["pwd"]
        name = request.form["name"]
        major = request.form["major"]
        
        if id == "" or pwd == "" or name == "" or major == "none":
            flash(f'Please fill the form!')
            return render_template("register.html")

        reg_result = db.register(id, pwd, name, major)
        
        if reg_result:
            flash(f'Register successfully! Please Login again.')
            return redirect(url_for("login"))
        
        else:
            flash(f'Register failed! Please Check again!')
            return render_template("register.html")
        
    return render_template("register.html")


@app.route("/main")
def main():
    if "id" in session:
        form = {}
        form['id'] = session['id']
        
    return redirect(url_for("login"))


@app.route("/lgout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.debug = True
    app.run()