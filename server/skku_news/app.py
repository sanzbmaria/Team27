from flask import Flask, render_template, session, url_for, redirect, request, jsonify, flash
from datetime import timedelta
from db_utils import Database


app = Flask(__name__)
app.secret_key = "skku_news"
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=10)
db = Database()

@app.route("/")
def index():
    return redirect(url_for("login"))


@app.route("/login", methods=("GET", "POST",))
def login():
    if request.method == "POST":
        login_result = db.login(request.form["id"], request.form["pwd"])

        if login_result:
            session["id"] = login_result[0]
            session["name"] = login_result[1]
            session["major"] = login_result[2]

            flash(f"Welcome {login_result[1]}")
            return redirect(url_for("main"))

        else:
            flash("Please check your ID and PASSWORD!")
            return render_template("login.html")
    else:
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
    else:
        return render_template("register.html")


@app.route("/main")
def main():
    if "id" in session:
        user = {
            "name": session["name"],
            "major": session["major"]
        }

        boards = []

        for board in db.get_user_boards(session['id']):
            boards.append({
                "major": board[0],
                "link": board[1]
            })

        notices = []

        for notice in db.get_articles(session['id']):
            notices.append({
                "idx": notice[0],
                "title": notice[1],
                "board": notice[2],
                "date": notice[3],
                "link": notice[4]+notice[5],
                "saved": notice[6]
            })
        
        saved_notices = []

        for notice in db.get_favorites(session['id']):
            saved_notices.append({
                "idx": notice[0],
                "title": notice[1],
                "board": notice[2],
                "date": notice[3],
                "link": notice[4]+notice[5],
                "saved": True
            })
        return render_template("index.html", user=user, boards=boards, notices=notices, saved_notices=saved_notices)

    return redirect(url_for("index"))


@app.route("/set-favorite", methods=("POST",))
def set_favorite():
    if "id" in session:
        user_id = session["id"]
        article_idx = request.form["idx"]
        result = db.set_favorites(user_id, article_idx)
        if result:
            flash("Add the article to favorites succesfully.")
        else:
            flash("Delete the article from favorites.")
    else:
        flash("Fail to add article. Please try again.")
    return redirect(request.referrer)


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))




if __name__ == "__main__":
    app.debug = True
    app.run()