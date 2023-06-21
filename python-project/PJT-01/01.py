with open('01.txt', 'w', encoding='UTF8') as f:
    f.write('Hello, Python!\n')
    for i in range(1, 6):
        f.write(f'{i}일차 파이썬 공부 중\n')

# 모범 답안
# string_list = [
#     'Hello, Python!',
#     '1일차 파이썬 공부 중',
#     '2일차 파이썬 공부 중',
#     '3일차 파이썬 공부 중',
#     '4일차 파이썬 공부 중',
#     '5일차 파이썬 공부 중',
# ]

# with open('./01.txt', 'w', encoding='UTF8') as f:
#     for string in string_list:
#         f.write(string + '\n')