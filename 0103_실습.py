# 실습 문제 1
num = int(input('정수를 입력하세요 > '))

if num > 0:
    print(True)
else:
    print(False)


# 실습 문제 2
num1 = int(input('첫 번째 정수를 입력하세요 > '))
num2 = int(input('두 번째 정수를 입력하세요 > '))

if num1 != num2:
    if num1 < num2:
        print(num2)
    else:
        print(num1)
else:
    print(False)


# 실습 문제 3
num = int(input('정수를 입력하세요 > '))

if 1 < num < 10:
    print(True)
else:
    print(False)


# 실습 문제 4
num = int(input('정수를 입력하세요 > '))

if num > 0:
    if num % 2 == 0:
        print(True)
    else:
        print(False)
else:
    print(False)


# 실습 문제 5
num = int(input('정수를 입력하세요 > '))

if 0 <= num <= 100:
    if num >= 60:
        print('합격')
    else:
        print('불합격')
else:
    print('에러')


# 실습 문제 6
string = 'hello world'

for char in string[::-1]:
    print(char)


# 실습 문제 7
num1 = int(input('첫 번째 정수를 입력하세요 > '))
num2 = int(input('두 번째 정수를 입력하세요 > '))

if num1 > num2:
    for i in range(num2 + 1, num1):
        print(i)
elif num1 < num2:
    for i in range(num1 + 1, num2):
        print(i)
else:
    print(False)


# 실습 문제 8
num1 = int(input('첫 번째 정수를 입력하세요 > '))
num2 = int(input('두 번째 정수를 입력하세요 > '))

if num1 > num2:
    for i in range(num1 - 1, num2, -1):
        print(i, end=' ')
elif num1 < num2:
    for i in range(num2 - 1, num1, -1):
        print(i, end=' ')
else:
    print(False)


# 실습 문제 9
num = int(input('정수를 입력하세요 > '))
if  num < 1:
    print(False)
else:
    for i in range(1, num, 2):
        print(i)


# 실습 문제 10
for n1 in range(2, 10):
    for n2 in range(2, 10):
        print(f'{n1} X {n2} = {n1*n2}')