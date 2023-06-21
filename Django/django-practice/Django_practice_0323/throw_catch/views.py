from django.shortcuts import render

# Create your views here.
def throw(request):
    return render(request, 'throw_catch/throw.html')


def catch(request):
    text = request.GET.get('message')
    context = {
        'text': text
    }
    return render(request, 'throw_catch/catch.html', context)