import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library_Project.settings')
django.setup()

from library.models import Author, Publisher, Category, Library, Book

# Данные для заполнения
authors = [
    {'first_name': 'Leo', 'last_name': 'Tolstoy', 'birth_date': '1828-09-09'},
    {'first_name': 'Fyodor', 'last_name': 'Dostoevsky', 'birth_date': '1821-11-11'},
    {'first_name': 'Alexander', 'last_name': 'Pushkin', 'birth_date': '1799-06-06'},
]

publishers = [
    {'name': 'Penguin Books', 'website': 'https://www.penguin.co.uk'},
    {'name': 'HarperCollins', 'website': 'https://www.harpercollins.com'},
    {'name': 'Simon & Schuster', 'website': 'https://www.simonandschuster.com'},
]

categories = [
    'Fiction',
    'Science Fiction',
    'Non-Fiction',
]

libraries = [
    {'name': 'Central Library', 'address': 'Main Street', 'city': 'New York', 'country': 'USA'},
    {'name': 'Westside Branch', 'address': 'West Avenue', 'city': 'Los Angeles', 'country': 'USA'},
    {'name': 'Eastside Branch', 'address': 'East Avenue', 'city': 'Chicago', 'country': 'USA'},
]

books = [
    {
        'title': 'War and Peace',
        'genre': 'Fiction',
        'year_published': 1869,
        'author': 'Leo Tolstoy',
        'publisher': 'Penguin Books',
        'category': 'Fiction',
        'library': 'Central Library',
    },
    {
        'title': 'Crime and Punishment',
        'genre': 'Fiction',
        'year_published': 1866,
        'author': 'Fyodor Dostoevsky',
        'publisher': 'HarperCollins',
        'category': 'Fiction',
        'library': 'Westside Branch',
    },
    {
        'title': 'Eugene Onegin',
        'genre': 'Fiction',
        'year_published': 1833,
        'author': 'Alexander Pushkin',
        'publisher': 'Simon & Schuster',
        'category': 'Fiction',
        'library': 'Eastside Branch',
    },
]

# Заполнение данных
for author_data in authors:
    Author.objects.update_or_create(
        first_name=author_data['first_name'],
        last_name=author_data['last_name'],
        defaults={'birth_date': author_data['birth_date']}
    )

for publisher_data in publishers:
    Publisher.objects.update_or_create(
        name=publisher_data['name'],
        defaults={'website': publisher_data['website']}
    )

for category_name in categories:
    Category.objects.update_or_create(name=category_name)

for library_data in libraries:
    Library.objects.update_or_create(
        name=library_data['name'],
        defaults={
            'address': library_data['address'],
            'city': library_data['city'],
            'country': library_data['country'],
        }
    )

for book_data in books:
    book_data['author'] = Author.objects.get(first_name=book_data['author'].split()[0], last_name=book_data['author'].split()[1])
    book_data['publisher'] = Publisher.objects.get(name=book_data['publisher'])
    book_data['category'] = Category.objects.get(name=book_data['category'])
    book_data['library'] = Library.objects.get(name=book_data['library'])
    Book.objects.update_or_create(
        title=book_data['title'],
        defaults={
            'genre': book_data['genre'],
            'year_published': book_data['year_published'],
            'author': book_data['author'],
            'publisher': book_data['publisher'],
            'category': book_data['category'],
            'library': book_data['library'],
        }
    )

print("Данные успешно добавлены!")