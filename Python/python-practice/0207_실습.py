# 백준 17608 막대기
import sys
input = sys.stdin.readline

numbers = []

N = int(input())
for _ in range(N):
    numbers.append(int(input()))
# 막대의 개수와 각 막대의 높이를 입력받아 리스트에 저장한다.

last = numbers[-1]
cnt = 1
# 가장 오른쪽 막대를 기준으로 삼고 가장 오른쪽 막대는 무조건 볼 수 있기 때문에 1부터 카운트한다.

for num in numbers[::-1]:
    if num > last:
        last = num
        cnt += 1
# 막대의 높이를 리스트의 마지막부터 하나씩 불러온다.
# 기준이 된 제일 오른쪽 막대보다 높은 막대가 있으면 1을 카운트하고 기준이 되는 막대 길이를 그 막대 높이로 설정한다.

print(cnt)
# 카운트된 막대의 수를 출력한다.


# 백준 7568 덩치
import sys
input = sys.stdin.readline

N = int(input())
# 전체 사람의 수를 입력받는다.

lst = []

for _ in range(N):
    weight, height = map(int, input().split())
    lst.append((weight, height))
# 사람들의 키와 몸무게를 (몸무게, 키) 형식의 튜플로 리스트에 저장한다.

rank = []
# 등수를 저장할 리스트를 만든다.

for i in range(N):
    cnt = 0
    for j in range(N):
        if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
            cnt += 1
    rank.append(cnt + 1)
# 등수는 자신보다 키와 몸무게 모두 큰 사람의 수 + 1 이다.
# 각 사람들의 등수를 리스트에 저장한다.

for r in rank:
    print(r, end=' ')
# 등수를 출력한다.


# 백준 1063 킹
# 방법 (1)
delta = {'R': (1, 0), 'L': (-1, 0), 'B': (0, -1), 'T': (0, 1), 'RT': (1, 1), 'LT': (-1, 1), 'RB': (1, -1), 'LB': (-1, -1)}
# 8방향 좌표를 키와 함께 딕셔너리에 저장한다.
# x축 방향과 y축 방향 증감을 값으로 한다.

king, stone, N = input().split()
k = [ord(king[0]) - 64, int(king[1])]
s = [ord(stone[0]) - 64, int(stone[1])]
# 킹의 위치, 돌의 위치, 움직이는 횟수 N을 입력받는다.
# 입력받은 킹의 위치, 돌의 위치는 좌표로 변환한다.
# 단, 제일 처음 좌표는 (0,0)이 아니라 (1,1)이다.

for _ in range(int(N)):
    dx, dy = delta[input()]
    nx = k[0] + dx
    ny = k[1] + dy
    # 입력받은 명령에 따라 변경한 좌표를 nx, ny 변수에 저장한다.

    if 0 < nx <= 8 and 0 < ny <= 8:
    # 단, 체스판의 범위를 벗어나지 않아야 한다.

        if nx == s[0] and ny == s[1]:
            sx = s[0] + dx
            sy = s[1] + dy
        # 킹을 명령에 따라 이동시킬 좌표에 돌이 있는 경우 돌도 똑같은 방향으로 움직인다.
            if 0 < sx <= 8 and 0 < sy <= 8:
                k = [nx, ny]
                s = [sx, sy]
            # 단, 돌도 체스판의 범위를 벗어나지 않아야 한다.
        else:
            k = [nx, ny]
        # 그 외의 경우 킹만 움직인다.

print(chr(k[0] + 64) + str(k[1]))
print(chr(s[0] + 64) + str(s[1]))
# 킹과 돌의 최종 좌표를 알파벳, 숫자로 이루어진 위치 정보로 바꾸어 출력한다.

# 방법 (2) -> 좌표, 행·열 변경 연습
delta = {'R': (0, 1), 'L': (0, -1), 'B': (-1, 0), 'T': (1, 0), 'RT': (1, 1), 'LT': (1, -1), 'RB': (-1, 1), 'LB': (-1, -1)}
# 8방향 좌표를 키와 함께 딕셔너리에 저장한다.
# 행과 열 방향 증감을 값으로 한다.

king, stone, N = input().split()
k = [int(king[1]), ord(king[0]) - 64]
s = [int(stone[1]), ord(stone[0]) - 64]

# 킹의 위치, 돌의 위치, 움직이는 횟수 N을 입력받는다.
# 입력받은 킹의 위치, 돌의 위치는 좌표로 변환한다.
# 주의할 점은 1~8 숫자가 행이고 A~H 알파벳이 열을 의미하므로 두 개의 위치를 바꿔 좌표로 변환한다.
# 단, 제일 처음 좌표는 (0,0)이 아니라 (1,1)이다.

for _ in range(int(N)):
    dx, dy = delta[input()]
    nx = k[0] + dx
    ny = k[1] + dy

    # 입력받은 명령에 따라 변경한 좌표를 nx, ny 변수에 저장한다.

    if 0 < nx <= 8 and 0 < ny <= 8:
    # 단, 체스판의 범위를 벗어나지 않아야 한다.

        if nx == s[0] and ny == s[1]:
            sx = s[0] + dx
            sy = s[1] + dy
        # 킹을 명령에 따라 이동시킬 좌표에 돌이 있는 경우 돌도 똑같은 방향으로 움직인다.
            if 0 < sx <= 8 and 0 < sy <= 8:
                k = [nx, ny]
                s = [sx, sy]
            # 단, 돌도 체스판의 범위를 벗어나지 않아야 한다.
        else:
            k = [nx, ny]
        # 그 외의 경우 킹만 움직인다.

print(chr(k[1] + 64) + str(k[0]))
print(chr(s[1] + 64) + str(s[0]))
# 킹과 돌의 최종 좌표를 알파벳, 숫자로 이루어진 위치 정보로 바꾸어 출력한다.