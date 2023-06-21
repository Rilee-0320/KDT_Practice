from django.shortcuts import render

# Create your views here.
def number_print(request, num):
    context = {
        'num': num
    }
    return render(request, 'print/number_print.html', context)

def index(request):
    return render(request, 'print/index.html')