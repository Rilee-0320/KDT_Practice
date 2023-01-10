# 문제에서 주어지는 입력을 받기 적합한 입력 코드를 작성하세요. 입력과 동일하게 출력하는 코드를 작성하세요.

# 실습 문제 1
# 5
number = int(input())
print(number)


# 실습 문제 2
# 2 5
a, b = list(map(int, input().split()))
print(a, b)


# 실습 문제 3
# 1 2 3
a, b, c = list(map(int, input().split()))
print(a, b, c)


# 실습 문제 4
# word1 word2 word3
a, b, c = input().split()
print(a, b, c)


# 실습 문제 5
# 1 2 3 4 5
number = list(map(int, input().split()))
for i in number:
    print(i, end=' ')


# 실습 문제 6
# -10 10
a, b = list(map(int, input().split()))
print(a, b)


# 실습 문제 7
# a b c d e
str = input().split()
print(*str)


# 실습 문제 8
# 3 17 1 39 8 41 2 32 99 2
numbers = list(map(int, input().split()))
for number in numbers:
    print(number, end=' ')


# 실습 문제 9
# 1 4 0 10 2 3 9
numbers = list(map(int, input().split()))
print(*numbers)