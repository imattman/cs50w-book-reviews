import csv

books = []
by_id = {}
by_isbn = {}


def init_app(app):
    csv_file = app.config['BOOKS_CSV']
    app.logger.info(f"Loading CSV {csv_file}")
    with open(csv_file) as fin:
        reader = csv.DictReader(fin)
        for id, rec in enumerate(reader, start=1):
            rec['id'] = id
            books.append(rec)
            by_id[id] = rec
            by_isbn[rec['isbn']] = rec


def find_books(term='', offset=0, limit=10):
    term = term.lower()
    results = [rec for rec in books
               if (term in rec['isbn'].lower() or
                   term in rec['title'].lower() or
                   term in rec['author'].lower() or
                   term in rec['year'])]

    return results[offset:limit+1]


def load_book(isbn):
    return by_isbn.get(isbn, None)
