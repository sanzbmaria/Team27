from flask import Flask, render_template, session, url_for, redirect, request
from datetime import timedelta


app = Flask(__name__)
app.secret_key = "skku_news"
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=10)


@app.route("/login", methods=("GET", "POST",))
def login():
    if request.method == "POST":
        session["id"] = request.form["id"]
        return redirect(url_for("main"))
    
    return render_template("login.html")


@app.route("/main")
def main():
    if "id" in session:
        form = {}

        form['id'] = session['id']
        return render_template("main.html", form=form, articles=articles)
    return redirect(url_for("login"))


@app.route("/lgout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.debug = True
    app.run()