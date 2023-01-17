# 백준 10818번 최소, 최대
T = int(input())
numbers = sorted(list(map(int, input().split())))
print(f'{numbers[0]} {numbers[T - 1]}')


# 백준 11720번 숫자의 합
N = int(input())
total = 0
numbers = list(map(int, input()))
for number in numbers:
    total += number
print(total)


# 백준 2750번 수 정렬하기
T = int(input())
list = []
for t in range(T):
    number = int(input())
    list.append(number)
for i in sorted(list):
    print(i)


# 백준 2562번 최댓값
list = [int(input()) for i in range(9)]
no = 0
for number in list:
    if number == max(list):
        no += 1
        print(number, no, sep='\n')
    else:
        no += 1