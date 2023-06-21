from django.shortcuts import render

# Create your views here.
def calculate(request, num1, num2):
    context = {
        'plus': num1 + num2,
        'minus': num1 - num2,
        'multiply': num1 * num2,
        'divide': num1 // num2,
    }
    return render(request, 'calculate/calculate.html', context)


def index(request):
    return render(request, 'calculate/index.html')