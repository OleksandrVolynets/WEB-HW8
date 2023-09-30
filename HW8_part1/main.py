from models import Author, Quote
import connection


def search_by_name(name: str):
    author = Author.objects(fullname=name).first()
    if author:
        quotes = Quote.objects(author=author)
        for quote in quotes:
            print(f" *{quote.quote}* ")
    else:
        print(f"Author {name} is not defined")


def search_by_tag(tag: str):
    quotes = Quote.objects(tags=tag)
    if tag:
        for quote in quotes:
            print(f" *{quote.quote}* ")
    else:
        print(f"Tag {tag} is not defined")


def capitalize_name(name: str):
    name_list = name.split(" ")
    capitalized_name = str()
    for n in name_list:
        capitalized_name += n.capitalize() + ' '
    return capitalized_name.strip()


def user_input():
    user_input = input(f'Waiting for command and value or input help\n')
    return user_input


def main():
    while True:
        try:
            search = user_input().split(':')
            command = search[0].strip().lower()
            if command == 'exit':
                break
            elif command == 'help':
                print(f"commands:\n help\n exit\n name - search by author`s fullname -- format name: value\n tag - search by tag -- format tag: value\n tags - search by tags -- format tags: value1, value2 ...\n")
            text = search[1].strip().lower()
            if command == 'name':
                search_by_name(capitalize_name(text))
            elif command == 'tag':
                search_by_tag(text)
            elif command == 'tags':
                tags_values = text.split(',')
                print(tags_values)
                for tag in tags_values:
                    search_by_tag(tag.strip())
        except:
            print('Please, enter correct data, format - "command: value"')


if __name__ == '__main__':
    main()


