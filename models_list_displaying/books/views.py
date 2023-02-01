import datetime

from django.core.paginator import Paginator
from django.shortcuts import render

from books.models import Book


def books_view(request, date=None):
    template = 'books/books_list.html'

    if date is not None:
        books = Book.objects.all().order_by('pub_date')
        dates = [datetime.datetime.strftime(book.pub_date, "%Y-%m-%d") for book in books]
        books = Book.objects.filter(pub_date=date)
        paginator = Paginator(dates, 1)
        page_number = dates.index(date) + 1
        page = paginator.page(page_number)
        prev_next = {}
        if page.has_previous():
            previous_page_number = page.previous_page_number()
            previous_page = paginator.page(previous_page_number)
            prev_next['previous_object'] = previous_page.object_list[-1]
        if page.has_next():
            next_page_number = page.next_page_number()
            next_page = paginator.page(next_page_number)
            prev_next['next_object'] = next_page.object_list[-1]

    else:
        books = Book.objects.all()
        page = None
        prev_next = {}


    context = {
        'books': books,
        'date': date,
        'page': page,
        'pages': prev_next
    }
    return render(request, template, context)
