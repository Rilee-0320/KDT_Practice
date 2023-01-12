# SWEA 2072. 홀수만 더하기
T = int(input())
for t in range(1, T + 1):
    numbers = list(map(int, input().split()))
    total = 0
    for number in numbers:
        if number % 2 == 1:
            total += number
    print(f'#{t} {total}')


# SWEA 2056. 연월일 달력
T = int(input())
for t in range(1, T + 1):
    numbers = input().split()
    for number in numbers:
        year = number[0:4]
        month = number[4:6]
        day = number[6:8]
        if int(month) > 12 or int(month) < 1:
            print(f'#{t} -1')
            break
        else:
            if month == '02':
                if int(day) > 28:
                    print(f'#{t} -1')
                    break
            elif month == '04' or '06' or '09' or '11':
                if int(day) > 30:
                    print(f'#{t} -1')
                    break
            else:
                if int(day) > 31:
                    print(f'#{t} -1')
                    break
        print(f'#{t} {year}/{month}/{day}')


# SWEA 2043. 서랍의 비밀번호
number = list(map(int, input().split()))
cnt = 0
while number[0] != number[1]:
    cnt += 1
    number[1] += 1
print(cnt + 1)


# SWEA 1933. 간단한 N의 약수
n = int(input())
list = []
for i in range(1, n + 1):
    if n % i == 0:
        list.append(i)
print(*list)


# SWEA 1288. 새로운 불면증 치료법
T = int(input())
for t in range(1, T + 1):
    number =  int(input())
    s = set()
    cnt = 1
    while True:
        for n in list(str(number)):
            s.add(n)
        if len(s) == 10:
            break
        number //= cnt
        cnt += 1
        number *= cnt
    print(f'#{t} {number}')