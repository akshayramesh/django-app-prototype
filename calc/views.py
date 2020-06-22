from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    # return HttpResponse("Hello World")
    return render(request, 'home.html', {'name': 'Akshay'})
    # return HttpResponse(list_of_books())

def list_of_books():
    booksModel = [
        {
            'name' : 'Da Vinci Code',
            'author' : 'Dan Brown'
        },
         {
            'name' : 'Da Vinci Code',
            'author' : 'Dan Brown'
        }
    ]

    return booksModel

def add(request):
    n1 = int(request.POST['num1'])
    n2 = int(request.POST['num2'])
    res = n1+n2
    return render(request, 'result.html', {'result':res})