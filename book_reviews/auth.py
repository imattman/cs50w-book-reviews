from flask import Blueprint, request, render_template, redirect
from flask_login import LoginManager, UserMixin
from book_reviews import repo

bp = Blueprint('auth', __name__, template_folder='templates')

login_manager = LoginManager()


def init_app(app):
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User()


@bp.route('/login')
def login():
    return "login"


@bp.route('/logout')
def logout():
    return redirect('/')


class User(UserMixin):
    pass
