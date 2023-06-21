from django.shortcuts import render
import random 

# Create your views here.
def today_drinks(request):
    drinks = ['솔의눈', '데자와', '실론티', '아침햇살', '맥콜', '닥터페퍼', 'ZICO', '밀키스', '환타', '포카리스웨트', '박카스', '코카콜라', '아메리카노', '스프라이트', '요구르트', '당근주스']

    context = {
        'drinks': drinks
    }
    return render(request, 'today_drinks.html', context)

def throw(request):
    return render(request, 'throw.html')

def catch(request):
    data = request.GET.get('message')
    context = {
        'data': data,
    }
    return render(request, 'catch.html', context)

def lotto_create(request):

    return render(request, 'lotto_create.html')

def lotto(request):
    number = request.GET.get('number')
    lotto_numbers = [random.sample(range(1, 46), 6) for i in range(int(number))]
    context = {
        'lotto_numbers': lotto_numbers
    }
    return render(request, 'lotto.html', context)