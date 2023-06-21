# 명세서를 읽고, 클래스를 정의합니다.
# 정의한 클래스를 활용하여 인스턴스를 생성하고, 메소드를 실행합니다.
# 메소드 실행 결과는 출력 예시와 동일해야 합니다.

# 클래스 이름
    # Calculator

# 인스턴스 변수
    # number1 : 정수 타입
    # number2 : 정수 타입

# 생성자
    # 두 개의 정수를 인자로 받아서 number1, number2 에 저장합니다.

# 메소드
    # plus
    # number1 + number2를 반환(return)합니다.

    # minus
    # number1 - number2를 반환(return)합니다.

    # multiply
    # number1 * number2를 반환(return)합니다.

    # division
    # number1 // number2를 반환(return)합니다.

    # print
    # 인스턴스 변수와 모든 사칙연산 결과를 출력(print)합니다.

class Calculator:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2
    
    def plus(self):
        return self.number1 + self.number2
    
    def minus(self):
        return self.number1 - self.number2

    def multiply(self):
        return self.number1 * self.number2
    
    def division(self):
        return self.number1 // self.number2

# plus
calculator = Calculator(10, 5)
print(calculator.plus())

calculator.number1 = -2
calculator.number2 = 2
print(calculator.plus())

# minus
calculator = Calculator(10, 5)
print(calculator.minus())

calculator.number1 = -2
calculator.number2 = 2
print(calculator.minus())

# multiply
calculator = Calculator(10, 5)
print(calculator.multiply())

calculator.number1 = -2
calculator.number2 = 2
print(calculator.multiply())

# division
calculator = Calculator(10, 5)
print(calculator.division())

calculator.number1 = -2
calculator.number2 = 2
print(calculator.division())

# 출력
calculator = Calculator(10, 5)
print(f'합 : {calculator.plus()}')
print(f'빼기 : {calculator.minus()}')
print(f'곱 : {calculator.multiply()}')
print(f'몫 : {calculator.division()}')

calculator.number1 = -2
calculator.number2 = 2
print(f'합 : {calculator.plus()}')
print(f'빼기 : {calculator.minus()}')
print(f'곱 : {calculator.multiply()}')
print(f'몫 : {calculator.division()}')
