from flask import Blueprint, request, render_template, jsonify
from book_reviews import repo

bp = Blueprint('books', __name__, template_folder='templates')


@bp.route('/')
def all():
    books = repo.find_books(limit=30)
    return render_template('books.html', books=books)


@bp.route('/<int:id>')
def single(id):
    return jsonify(repo.load_book(id))


@bp.route('/search')
def search():
    query = request.args.get('q', '')
    books = repo.find_books(query)
    return render_template('books.html', search_query=query, books=books)
