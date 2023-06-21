# 백준 1225 이상한 곱셈
import sys

numbers = [list(num) for num in sys.stdin.readline().split()]
# 숫자 A와 B를 각각 리스트로 만들어 numbers라는 리스트에 저장한다.
print(sum(map(int, numbers[0])) * sum(map(int, numbers[1])))
# 숫자 A의 각 자릿수 숫자를 B의 각 자릿수 숫자에 곱해 더하는 것은 A와 B, 각 자릿수 숫자의 합끼리 곱하는 것과 동일하다. 


# 백준 2438 별 찍기 - 1
N = int(input())
for n in range(1, N+1):
    print('*' * n)
# 숫자 N을 입력받고 1부터 N까지 1 ~ N개의 별을 출력한다.


# 백준 2739 구구단
N = int(input())
for n in range(1, 10):
    print(f'{N} * {n} = {N * n}')
# 숫자 N을 입력받고 1부터 9까지 N에 곱한 값을 출력한다.


# 백준 2953 나는 요리사다
scores = [list(map(int, input().split())) for _ in range(5)]
# 요리사 다섯 명의 점수를 이차원 리스트의 형태로 입력받는다.
highest_score = sum(scores[0])
number = 1
# 가장 높은 점수를 첫 번째 요리사의 점수로 임의 설정해놓는다.
for score in scores:
    if sum(score) > highest_score:
        highest_score = sum(score)
        number = 1 + scores.index(score)
# for문을 돌려 첫 번째 요리사의 점수보다 높은 점수가 있을 경우 새롭게 highest_score 변수에 저장한다.
# 오리사의 번호는 0이 아닌 1부터이므로 1을 더한다. 
print(number, highest_score)
# 우승자의 번호와 점수를 출력한다.


# 백준 2669 직사각형 네 개의 합집합의 면적 구하기
x_y = set()
# 중복된 좌표를 제거하기 위한 빈 set 생성
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    # for문을 통해 네 줄의 x1, x2, y1, y2 좌표를 입력받는다.
    for i in range(x1, x2):
        for j in range(y1, y2):
            x_y.add((i, j))
    # 각 줄의 x, y 좌표로 만들 수 있는 모든 튜플을 set에 저장한다.
print(len(x_y))
# 좌표의 개수를 출력한다.