from django.shortcuts import render

def book_details(request):
    book = {
        'title' : 'Война и мир',
        'author' : 'Лев Толстой',
        'year' : '1868',
        'price' : '1500',
        'description' : 'Роман в 4 томах'
    }
    return render(request, 'catalog/book_detail.html', {'book':book})


