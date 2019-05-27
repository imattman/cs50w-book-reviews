from flask import Blueprint, current_app, request, render_template, jsonify
from flask_login import login_required
from book_reviews import repo

bp = Blueprint('books', __name__, template_folder='templates')


@bp.route('/')
# @login_required
def all():
    page_size = current_app.config.get('PAGE_SIZE', 10)
    books = repo.find_books(limit=page_size)
    return render_template('books.html', books=books)


@bp.route('/<isbn>')
def single(isbn):
    return jsonify(repo.load_book(isbn))


@bp.route('/search')
def search():
    query = request.args.get('q', '')
    books = repo.find_books(query)
    return render_template('books.html', search_query=query, books=books)
