# SWEA 2029. 몫과 나머지 출력하기
T = int(input())
for t in range(1, T + 1):
    a, b = list(map(int, input().split()))
    quotient = a // b
    remainder = a % b
    print(f'#{t} {quotient} {remainder}')


# SWEA 2071. 평균값 구하기
T = int(input())
for t in range(1, T + 1):
    numbers = list(map(int, (input().split())))
    cnt = len(numbers)
    total = sum(numbers)
    result = round(total / cnt)
    print(f'#{t} {round(total / cnt)}')

# SWEA 1938. 아주 간단한 계산기
a, b = map(int, input().split())
print(a + b)
print(a - b)
print(a * b)
print(int(a / b))


# SWEA 2046. 스탬프 찍기
n = int(input())
print('#' * n)


# SWEA 2068. 최대수 구하기
T = int(input())
for t in range(1, T + 1):
    numbers = list(map(int, input().split()))
    result = 0
    for n in numbers:
        if n > result:
            result = n
    print(f'#{t} {result}')