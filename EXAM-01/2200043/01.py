# 1 홀수만 더하기
T = int(input())
for t in range(1, T + 1):
    numbers = list(map(int, input().split()))
    total = 0
    for number in numbers:
        if number % 2 == 1:
            total += number
    print(f'#{t} {total}')