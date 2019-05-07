#!/usr/bin/env python3

import csv
import sys


default_data_file = "books.csv"
out_file = "db-import-books.sql"
table = "books"
text_fields = ['isbn', 'title', 'author']
int_fields = ['year']


def main():
    data_file = default_data_file
    if sys.argv[1:]:
        data_file = sys.argv[1]

    records = load_data(data_file)
    generate_sql(records, sys.stdout)


def load_data(data_file):
    with open(data_file) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        records = []
        for rec in csv_reader:
            for field in text_fields:
                rec[field] = clean(rec[field])
            for field in int_fields:
                rec[field] = int(rec[field])
            records.append(rec)
    return records


def clean(line):
    line = line.replace("'", r"''")  # escape ' using a second ' (SQL is weird)
    return line


def generate_sql(records, out):
    # TODO: generate stmt format string using text_fields and int_fields

    for rec in records:
        stmt = """INSERT INTO {table} (isbn, title, author, year) values ('{isbn}', '{title}', '{author}', {year});"""
        rec['table'] = table
        print(stmt.format(**rec), file=out)


if __name__ == "__main__":
    main()
