# 문제에서 주어지는 입력을 받기 적절한 입력 코드를 작성하세요. 입력과 동일하게 출력하는 코드를 작성하세요.

# 실습 문제 1
# 정수를 출력하세요.
# 5
n = int(input())
print(n)


# 실습 문제 2
# 단어를 구분해서 출력하세요.
# hello python world
words = input().split()
print(words)


# 실습 문제 3
# 테스트 케이스마다 입력 값을 그대로 출력하세요.
# 3 # 테스트 케이스 수
# 1
# 2
# 3
n = int(input())
for n in range(1, n + 1):
    print(input())


# 실습 문제 4
# 2개 이상의 정수를 출력하세요.
# 2 0 3 92 3
numbers = list(map(int, input().split()))
print(numbers)


# 실습 문제 5
# 2개의 정수를 출력하세요.
# 2 3
a, b = list(map(int, input().split()))
print(a, b)


# 실습 문제 6
# 단어를 구분해서 출력하세요.
# I am Programmer
words = input().split()
print(words)


# 실습 문제 7
# 테스트 케이스마다 입력 값을 그대로 출력하세요.
# 5 # 테스트 케이스 수
# 1 2 3
# 4 5 6
# 7 8 9
# 10 11 12
# 13 14 15
n = int(input())

for n in range(1, n + 1):
    numbers = list(map(int, input().split()))
    print(numbers)


# 실습 문제 8
# 테스트 케이스마다 입력 값을 그대로 출력하세요.
# 5 # 테스트 케이스 수
# 1 38 108 29 3 2 39
# 1 9 12 3 5 1
# 28 39 1 20 9 1
# 34 5 6 8
# 9 3 2 10 1 2 4
n = int(input())

for n in range(1, n + 1):
    numbers = list(map(int,input().split()))
    print(numbers)