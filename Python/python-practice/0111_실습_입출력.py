# 문제에서 주어지는 입력을 받기 적합한 입력 코드를 작성하세요. 입력과 똑같이 출력하는 코드를 작성하세요.

# 실습 문제 1
# 공백으로 구분된 정수
# 5 19 2901 2039 41 2 23 40
numbers = list(map(int, input().split()))
print(*numbers)


# 실습 문제 2
# 공백으로 구분된 문자열
# Lorem ipsum dolor sit amet, consectetur adipiscing elit.
words = input().split()
for word in words:
    print(word, end=' ')


# 실습 문제 3
# 테스트 케이스 수와 입력 줄 수가 주어지는 입력
# 첫 줄에 테스트 케이스 수가 주어집니다. 각 테스트 케이스의 첫 번째 줄에 입력 줄 수가 주어집니다.
# 2 
# 3
# 1
# 2 
# 3
# 2
# 1 
# 2
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    for n in range(1, N + 1):
        print(n)


# 실습 문제 4
# 테스트 케이스 수와 입력 줄 수가 주어지는 입력
# 첫 줄에 테스트 케이스 수가 주어집니다. 각 테스트 케이스의 첫 번째 줄에 입력 줄 수가 주어집니다.
# 2
# 3
# 1 1
# 2 2
# 3 3
# 2
# 1 1
# 2 2
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    for n in range(1, N + 1):
        print(f'{n} {n}')


# 실습 문제 5
# 테스트 케이스 수와 입력 줄 수가 주어지는 입력
# 첫 줄에 테스트 케이스 수가 주어집니다. 각 테스트 케이스의 첫 번째 줄에 입력 줄 수가 주어집니다. 각 문장에 포함된 단어를 공백을 기준으로 출력하세요.
# 2 
# 2 
# Lorem ipsum dolor sit amet, consectetur adipiscing elit.
# Donec rutrum ex vel nibh vulputate, ut convallis turpis elementum.
# 5
# Lorem ipsum dolor sit amet, consectetur adipiscing elit.
# Nam eget tellus eu tortor rutrum tincidunt.
# Etiam scelerisque lacus ut enim dignissim, nec pulvinar nisl
# Vivamus quis orci malesuada, mattis libero a, rhoncus sapien.
# Phasellus vehicula turpis a nisl ullamcorper finibus.
import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
print(T)
for t in range(1, T + 1):
    N = int(input())
    print(N)
    for n in range(1, N + 1):
        string = input().split('\n')
        print(*string)


# 실습 문제 6
# 테스트 케이스 수와 입력 줄 수가 주어지는 입력
# 첫 줄에 테스트 케이스 수가 주어집니다. 각 테스트 케이스의 첫 번째 줄에 입력 줄 수가 주어집니다.
# 2  
# 3  
# 1 3 492 32
# 32 90 65 2 1
# 3 9 9
# 2
# 1 
# 4 93 1 2
import sys
sys.stdin = open('input2.txt', 'r')
T = int(input())
print(T)
for t in range(T):
    N = int(input())
    print(N)
    for n in range(N):
        numbers = input().split('\n')
        print(*numbers)


# 실습 문제 7
# 테스트 케이스 수와 입력 줄 수가 주어지는 입력
# 첫 줄에 테스트 케이스와 각 테스트 케이스의 입력 줄 수가 주어집니다.
# 2 1
# 1
# 2
N = list(map(int, input().split()))
for a in range(N[0]):
    for b in range(N[1]):
        print(a + 1)


# 실습 문제 8
# 테스트 케이스 수와 입력 줄 수가 주어지는 입력
# 첫 줄에 테스트 케이스와 각 테스트 케이스의 입력 줄 수가 주어집니다.
# 2 2
# 2 3
# 1 2
# 3 4
# 5 9
import sys
sys.stdin = open('input3.txt', 'r')
N = list(map(int, input().split()))
print(*N)
for a in range(N[0]):
    for b in range(N[1]):
        print(input())


# 실습 문제 9
# 테스트 케이스 수와 입력 줄 수가 주어지는 입력
# 첫 줄에 테스트 케이스와 각 테스트 케이스의 입력 줄 수가 주어집니다.
# 2 3 
# 1 3 492 
# 32 90 65
# 3 9 9
# 1 3 9
# 4 93 1
# 2 4 2
import sys
sys.stdin = open('input4.txt', 'r')
N = list(map(int, input().split()))
print(*N)
for a in range(N[0]):
    for b in range(N[1]):
        print(input())