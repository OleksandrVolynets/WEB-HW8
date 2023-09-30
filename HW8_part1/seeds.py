from models import Author, Quote
import connection
import json

file_authors = 'authors.json'
file_quotes = 'quotes.json'

def load_authors(file_path):
    with open(file_path, 'r', encoding="utf-8") as f:
        authors = json.load(f)
        for author in authors:
            fullname = author.get('fullname')
            born_date = author.get('born_date')
            born_location = author.get('born_location')
            description = author.get('description')

            author_to_db = Author(fullname=fullname, born_date=born_date, born_location=born_location, description=description)
            author_to_db.save()


def load_quotes(file_path):
    with open(file_path, 'r', encoding="utf-8") as f:
        quotes = json.load(f)
        for q in quotes:
            author = Author.objects(fullname=q.get("author", None))
            tags = q.get('tags')
            quote = q.get('quote')

            quote_to_db = Quote(tags=tags, author=author[0], quote=quote)
            quote_to_db.save()


if __name__ == '__main__':
    load_authors(file_authors)
    load_quotes(file_quotes)