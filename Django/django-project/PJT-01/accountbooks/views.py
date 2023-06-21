from django.shortcuts import render, redirect
from .models import AccountBook
from datetime import date
# Create your views here.

INDEX_HTML = 'accountbooks/index.html'
INDEX_PAGE = 'accountbooks:index'

def index(request):
    accountbooks = AccountBook.objects.all()
    context = {
        'accountbooks': accountbooks,
    }
    return render(request, INDEX_HTML, context)


def detail(request, account_book_pk):
    accountbook = AccountBook.objects.get(pk=account_book_pk)
    context = {
        'accountbook': accountbook,
    }
    return render(request, 'accountbooks/detail.html', context)


def new(request):
    today = date.today()
    context ={
        'today': today,
    }
    return render(request, 'accountbooks/new.html', context)

def create(request):
    accountbook = AccountBook()
    accountbook.note = request.POST.get('note')
    accountbook.description = request.POST.get('description')
    accountbook.category = request.POST.get('category')
    accountbook.amount = request.POST.get('amount')
    accountbook.date = request.POST.get('date')
    accountbook.save()
    return redirect(INDEX_PAGE)



def edit(request, account_book_pk):
    accountbook = AccountBook.objects.get(pk=account_book_pk)
    context = {
        'accountbook': accountbook,
    }
    return render(request, 'accountbooks/edit.html', context)


def update(request, account_book_pk):
    accountbook = AccountBook.objects.get(pk=account_book_pk)
    accountbook.note = request.POST.get('note')
    accountbook.description = request.POST.get('description')
    accountbook.category = request.POST.get('category')
    accountbook.amount = request.POST.get('amount')
    accountbook.date = request.POST.get('date')
    accountbook.save()

    return redirect('accountbooks:detail', account_book_pk)


def delete(request, account_book_pk):
    accountbook = AccountBook.objects.get(pk=account_book_pk)
    accountbook.delete()
    return redirect(INDEX_PAGE)


def copy(request, account_book_pk):
    accountbook = AccountBook.objects.get(pk=account_book_pk)
    tmp_note = accountbook.note
    tmp_description = accountbook.description
    tmp_category = accountbook.category
    tmp_amount = accountbook.amount
    tmp_date = accountbook.date

    new_accountbook = AccountBook(note=tmp_note, description=tmp_description, category=tmp_category, amount=tmp_amount, date=tmp_date)
    new_accountbook.save()

    return redirect(INDEX_PAGE)