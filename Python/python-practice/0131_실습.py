# 백준 2441 별 찍기 - 4
N = int(input())
# N의 수를 입력받는다.
for n in range(N):
    print(' ' * n + '*' * (N-n))
# for문을 돌려 '*'를 한 개씩 줄여나가고 왼쪽에 공백을 한 개씩 추가하여 출력한다.


# 백준 2592 대표값
list = [int(input()) for _ in range(10)]
# 10개의 수를 입력받아 리스트에 저장한다.
cnt = []
# 최빈값을 구하기 위해 빈 리스트를 생성한다.
for num in set(list):
    cnt.append([num, list.count(num)])
# set을 통해 중복된 숫자를 제거한다.
# [숫자, 빈도수] 형식으로 cnt라는 빈 리스트에 저장한다.
cnt.sort(key=lambda x: (x[1], x[0]))
# cnt 리스트를 빈도수, 숫자순으로 정렬한다.
print(int(sum(list)/len(list)))
print(cnt[-1][0])
# 평균과 최빈값을 출력한다.


# 백준 10798 세로 읽기
str = [[char for char in input()] for _ in range(5)]
print(str)
# 다섯줄의 입력을 받고 각 줄의 문자를 개개의 요소로 가지는 리스트를 만든다.
# [['A', 'A', 'B', 'C', 'D', 'D'],
#  ['a', 'f', 'z', 'z'],
#  ['0', '9', '1', '2', '1'],
#  ['a', '8', 'E', 'W', 'g', '6'],
#  ['P', '5', 'h', '3', 'k', 'x']]

max_len = 0
for s in str:
    if len(s) > max_len:
        max_len = len(s)
# 다섯줄 중 가장 긴 문자열의 길이를 구한다.
# 6

for i in range(max_len):
    for j in range(len(str)):
        try:
            print(str[j][i], end='')
        except:
            continue
# 기존의 행값을 열에, 기존의 열값을 행에 넣어 숫자를 하나씩 출력한다.
# 가장 긴 문자열의 길이를 기준으로 했기 때문에 그보다 짧은 문자열에서 오류가 발생.
# try, except 문을 사용하여 오류를 뛰어넘어 출력한다.
# Aa0aPAf985Bz1EhCz2W3D1gkD6x


# 백준 9455 박스
T = int(input())
# 테스트 케이스 수를 입력받는다.
for _ in range(T):
    m, n = map(int, input().split())

    matrix = []
    for _ in range(m):
        matrix.append(list(map(int, input().split())))
# 테스트 케이스 수만큼 행과 열, 각 행의 정보를 입력받아 리스트에 저장한다.

    new_matrix = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            new_matrix[i][j] = matrix[m-j-1][i]
    # 각 행의 정보가 입력된 리스트를 오른쪽으로 90도 돌린 새 리스트를 만든다.

    cnt = 0
    for a in new_matrix:
        for b in range(len(a)):
            if a[b] == 0:
                try:
                    if a.index(1, b) >= 0:
                        first_1 = a.index(1, b)
                        cnt += first_1 - b
                        a[b], a[first_1] = a[first_1], a[b]
                except:
                    continue
    print(cnt)
    # 새로 만든 리스트의 각 행을, 그리고 그 안의 숫자를 하나씩 불러온다.
    # 불러온 숫자가 0일 경우 이후 가장 먼저 1이 나오는 인덱스값을 찾아 0과 가장 가까운 1과의 거리를 구한다.
    # 거리를 구한 후에는 해당 1과 0의 위치를 서로 바꾼다.
    # 이것을 반복하여 0 이후 더이상 1이 나오지 않도록 만든다.
    # 최종적으로 총 거리의 합을 출력한다.


# 백준 1652 누울 자리를 찾아라
N = int(input())
matrix = [[char for char in input()] for _ in range(N)]
# 방의 크기 N을 입력받는다.
# 방의 구조를 나타내는 '.'와 'X' 문자열을 N만큼 입력받고 행렬의 형태로 저장한다.
# [['.', '.', '.', '.', 'X'],
#  ['.', '.', 'X', 'X', '.'],
#  ['.', '.', '.', '.', '.'],
#  ['.', 'X', 'X', '.', '.'],
#  ['X', '.', '.', '.', '.']]

# 1. 가로로 누울 자리 구하기
x_list = []
x_cnt = 0

for x in matrix:
    x = ''.join(x)
    x_list.append(x.split('X'))
# 새로운 리스트(x_list)를 만들어 행렬의 각 리스트 속 요소를 문자 'X'를 기준으로 쪼개어 저장한다.
# [['....', ''], ['..', '', '.'], ['.....'], ['.', '', '..'], ['', '....']]

for lst in x_list:
    for char in lst:
        if char.count('.') >= 2:
            x_cnt += 1
# x_list 속 요소를 순회하며 '.'이 2개 이상 붙어 있는 경우 누울 수 있는 자리 한 개로 카운트한다.

# 2. 세로로 누울 자리 구하기
y_matrix = [[] for _ in range(N)]
for i in range(N):
    for j in range(N):
        y_matrix[i].append(matrix[j][i])
# 기존 행렬의 행 값을 열에, 열 값을 행에 넣어 열 우선 순회 매트릭스를 만든다.
# [['.', '.', '.', '.', 'X'],
#  ['.', '.', '.', 'X', '.'],
#  ['.', 'X', '.', 'X', '.'],
#  ['.', 'X', '.', '.', '.'],
#  ['X', '.', '.', '.', '.']]

y_cnt = 0
y_list = []

for y in y_matrix:
    y = ''.join(y)
    y_list.append(y.split('X'))
# 새로운 리스트(y_list)를 만들어 행렬의 각 리스트 속 요소를 문자 'X'를 기준으로 쪼개어 저장한다.
# [['....', ''], ['...', '.'], ['.', '.', '.'], ['.', '...'], ['', '....']]

for lst in y_list:
    for char in lst:
        if char.count('.') >= 2:
            y_cnt += 1
# y_list 속 요소를 순회하며 '.'이 2개 이상 붙어 있는 경우 누울 수 있는 자리 한 개로 카운트한다.

print(x_cnt, y_cnt)
# 5 4