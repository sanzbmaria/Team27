from flask import Blueprint, render_template, session, url_for, redirect, request
from skku_news.forms import LoginForm

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/login', methods=("GET", "POST",))
def login():
    if request.method == "POST":
        pass
    return render_template("login.html", form=)