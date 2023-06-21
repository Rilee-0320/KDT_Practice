# 실습 문제 1
# 정수형 숫자를 입력받고, 10을 더해서 출력하세요.
number = int(input('정수형 숫자를 입력해주세요 > '))
print(number + 10)


# 실습 문제 2
# 좋아하는 음식을 입력받고, 출력하세요.
food = input('좋아하는 음식을 입력해주세요 > ')
print('좋아하는 음식 :', food)


# 실습 문제 3
# 이름과 태어난 연도를 입력받고, 출력하세요. (단, 태어난 연도를 나이로 변환해서 출력하세요.)
name = input('이름을 입력해주세요 > ')
year = 2023 - int(input('태어난 년도를 입력해주세요 > ')) + 1
print('저의 이름은 ' + name + '이고, 올해 나이는 ' + str(year) + '세 입니다.')


# 실습 문제 4
# 문장 두 개를 입력받고, 두 문장을 연결해서 출력하세요.
string1 = input('첫 번째 문장을 입력해주세요 > ')
string2 = input('두 번째 문장을 입력해주세요 > ')
print(string1 + string2)


# 실습 문제 5
# 정수형 숫자 한 개를 입력받고, 정수형 숫자의 부호를 바꿔서 출력하세요.
number = int(input('정수형 숫자를 입력해주세요 > '))
print(number * -1)


# 실습 문제 6
# 정수형 숫자 두 개를 입력받고, 두 정수형 숫자에 대한 아래 산술 연산 결과를 출력하세요.
# 더하기
# 빼기
# 곱하기
# 몫
# 나머지
number1 = int(input('첫 번째 정수형 숫자를 입력해주세요 > '))
number2 = int(input('두 번째 정수형 숫자를 입력해주세요 > '))
print('더하기 연산 :', number1 + number2)
print('빼기 연산 :', number1 - number2)
print('곱하기 연산 :', number1 * number2)
print('몫 연산 :', number1 // number2)
print('나머지 연산 :', number1 % number2)


# 실습 문제 7
# 정수형 숫자 세 개를 입력받고, 세 정수형 숫자의 평균을 출력하세요.
number1 = int(input('첫 번째 정수형 숫자를 입력해주세요 > '))
number2 = int(input('두 번째 정수형 숫자를 입력해주세요 > '))
number3 = int(input('세 번째 정수형 숫자를 입력해주세요 > '))
print(int((number1 + number2 + number3) / 3))


# 실습 문제 8
# 정수형 숫자 다섯 개를 입력받고, 다섯 개의 정수형 숫자를 리스트 객체에 저장해서 출력하세요.
number1 = int(input('첫 번째 정수형 숫자를 입력해주세요 > '))
number2 = int(input('두 번째 정수형 숫자를 입력해주세요 > '))
number3 = int(input('세 번째 정수형 숫자를 입력해주세요 > '))
number4 = int(input('네 번째 정수형 숫자를 입력해주세요 > '))
number5 = int(input('다섯 번째 정수형 숫자를 입력해주세요 > '))
print([number1, number2, number3, number4, number5])


# 실습 문제 9
# 문자열 하나와 정수형 숫자 한 개를 입력받고, 문자열을 정수형 숫자만큼 반복해서 출력하세요.
string = input('문자열을 입력해주세요 > ')
number = int(input('정수형 숫자를 입력해주세요 > '))
print(string * number)


# 실습 문제 10
# 정수형 숫자 다섯 개를 입력받고, 입력할 때마다 입력한 정수형 숫자들의 합을 출력하세요.
number1 = int(input('첫 번째 정수형 숫자를 입력해주세요 > '))
print(number1)
number2 = int(input('두 번째 정수형 숫자를 입력해주세요 > '))
print(number1 + number2)
number3 = int(input('세 번째 정수형 숫자를 입력해주세요 > '))
print(number1 + number2 + number3)
number4 = int(input('네 번째 정수형 숫자를 입력해주세요 > '))
print(number1 + number2 + number3 + number4)
number5 = int(input('다섯 번째 정수형 숫자를 입력해주세요 > '))
print(number1 + number2 + number3 + number4 + number5)
