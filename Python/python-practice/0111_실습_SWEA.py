# SWEA 2047. 신문 헤드라인
str = input()
print(str.upper())


# SWEA 2025. N줄 덧셈
number = int(input())
total = 0
for n in range(number + 1) :
    total += n
print(total)


# SWEA 1936. 1대1 가위바위보
dict = {
    (1, 2) : 'B',
    (1, 3) : 'A',
    (2, 1) : 'A',
    (2, 3) : 'B',
    (3, 1) : 'B',
    (3, 2) : 'A'
}
game = tuple(map(int, input().split()))
print(dict[game])


# SWEA 2027. 대각선 출력하기
for i in range(5):
    print(('+'*i) + '#' + ('+'*(4-i)))


# SWEA 2058. 자릿수 더하기
number = int(input())
total = 0
while number > 0 :
    n = number % 10
    number = number // 10
    total += n
print(total)


# SWEA 2019. 더블더블
n = int(input())
total = 1
for i in range(n + 1):
    # print(i)
    print(total, end=' ')
    total = total * 2