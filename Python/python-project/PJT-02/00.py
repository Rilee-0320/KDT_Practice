import requests

URL = 'https://api.bithumb.com/public/ticker/BTC_KRW'

response = requests.get(URL).json()
print(response['data']['prev_closing_price'])

# 예시 코드
# import requests

# def get_btc_krw():
#     order_currency = 'BTC'
#     payment_currency = 'KRW'
#     URL = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}'

#     res = requests.get(URL).json()
#     data = res['data']
#     prev_closing_price = data['prev_closing_price']

#     return prev_closing_price

# if __name__ == '__main__':
#     print(get_btc_krw())