# 실습 문제 1
# 정수 한 개를 입력받고 해당 숫자가 0보다 큰 숫자라면 True, 아니면 False를 출력하세요.
num = int(input('정수를 입력하세요 > '))

if num > 0:
    print(True)
else:
    print(False)


# 실습 문제 2
# 정수 두 개를 입력받고, 크기가 더 큰 정수를 출력하세요. 두 정수가 같으면 False를 출력하세요.
# (1) 내 답안
num1 = int(input('첫 번째 정수를 입력하세요 > '))
num2 = int(input('두 번째 정수를 입력하세요 > '))

if num1 != num2:
    if num1 < num2:
        print(num2)
    else:
        print(num1)
else:
    print(False)

# (2) 모범 답안
number1 = int(input("첫 번째 정수를 입력하세요 > "))
number2 = int(input("두 번째 정수를 입력하세요 > "))

if number1 == number2:
    print(False)
if number1 > number2:
    print(number1)
if number1 < number2:
    print(number2)


# 실습 문제 3
# 정수 한 개를 입력받고, 해당 정수가 1보다 크고, 10보다 작다면 True 아니면 False를 출력하세요.
# (1) 내 답안
num = int(input('정수를 입력하세요 > '))

if 1 < num < 10:
    print(True)
else:
    print(False)

# (2) 모범 답안
number = int(input("정수를 입력하세요 > "))

if 1 < number and number < 10:
    print(True)
else:
    print(False)


# 실습 문제 4
# 정수 한 개를 입력받고 0보다 크고, 짝수라면 True, 아니면 False를 출력하세요.
num = int(input('정수를 입력하세요 > '))

if num > 0:
    if num % 2 == 0:
        print(True)
    else:
        print(False)
else:
    print(False)


# 실습 문제 5
# 정수 한 개를 입력받고, 아래 조건에 따라 출력하세요.
# 값이 100 초과 / 0 미만이면 "에러" 출력
# 값이 60 이상이면 "합격" 출력
# 값이 60 미만이면 "불합격" 출력
# (1) 내 답안
num = int(input('정수를 입력하세요 > '))

if 0 <= num <= 100:
    if num >= 60:
        print('합격')
    else:
        print('불합격')
else:
    print('에러')

# (2) 모범 답안
number = int(input("정수를 입력하세요 > "))

if number > 100 or number < 0:
    print("에러")
else:
    if number >= 60:
        print("합격")
    else:
        print("불합격")


# 실습 문제 6
# 문자열을 입력받고, 입력받은 문자열을 반대로 한 글자씩 출력하세요.
# 힌트 : 문자열 역슬라이싱
string = 'hello world'

for char in string[::-1]:
    print(char)


# 실습 문제 7
# 정수 두 개를 입력받고, 두 수 사이의 정수를 오름차순으로 출력하세요. 두 값이 같으면 False를 출력하세요.
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
# 정수 두 개를 입력받고, 두 수 사이의 정수를 내림차순으로 한 줄에 모두 출력하세요. 두 값이 같으면 False를 출력하세요.
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
# 정수 한 개를 입력받고, 1부터 입력값 사이의 정수 중 홀수만 출력하세요. 입력값이 1보다 작으면 False를 출력하세요.
# (1) 내 답안
num = int(input('정수를 입력하세요 > '))
if  num < 1:
    print(False)
else:
    for i in range(1, num, 2):
        print(i)

# (2) 모범 답안
number = int(input("정수를 입력하세요 > "))

if number < 1:
    print(False)
else:
    for element in range(1, number):
        if element % 2 == 1:
            print(element)


# 실습 문제 10
# 구구단을 출력하세요.
for n1 in range(2, 10):
    for n2 in range(2, 10):
        print(f'{n1} X {n2} = {n1*n2}')