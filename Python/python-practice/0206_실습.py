# 백준 10769 행복한지 슬픈지
import sys

str  = sys.stdin.readline()
# 문자열을 입력받는다.

happy_cnt = 0 ; sad_cnt = 0
# 행복한 이모티콘과 슬픈 이모티콘의 수를 각각 세기 위한 변수를 만든다.

for i in range(len(str)):
    if str[i] == ':':
        if str[i:i+3] ==':-)':
            happy_cnt += 1
        if str[i:i+3] == ':-(':
            sad_cnt += 1
# 입력받은 문자열을 순회한다.
# ':'가 있으면 그 뒤 두 글자로 행복한 이모티콘인지 슬픈 이모티콘인지 판별하여 카운트한다.

if sad_cnt < happy_cnt:
    print('happy')
# 행복한 이모티콘이 더 많을 경우 'happy' 출력

elif sad_cnt > happy_cnt:
    print('sad')
# 슬픈 이모티콘이 더 많을 경우 'sad' 출력

elif sad_cnt == happy_cnt:
    if sad_cnt >= 1:
        print('unsure')
# 행복한 이모티콘과 슬픈 이모티콘이 모두 1개 이상인 상황에서 개수가 같을 경우 'unsure' 출력

    else:
        print('none')
# 이모티콘이 없으면 'none' 출력


# 백준 2455 지능형 기차
import sys

people = 0 ; max_people = 0
# 승객의 인원과 최대 승객의 수를 세기 위한 변수를 만든다.

for _ in range(4):
    people_out, people_in = map(int, sys.stdin.readline().split())
    # 각 역에서 내린 사람의 수와 탄 사람의 수를 입력받는다.

    people += people_in - people_out
    # '탄 사람 수 - 내린 사람 수'를 현재 인원에 더한다.

    if people > max_people:
        max_people = people
    # 현재 인원이 최대 승객 수보다 많은 해당 인원을 최대 승객 수로 설정한다.
    # 이것을 반복하여 최댓값을 구한다.

print(max_people)
# 최대 승객 수를 출력한다.


# 백준 2606 바이러스
import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
# 컴퓨터 수와 연결되어 있는 컴퓨터 쌍의 수를 입력받는다.

graph = [[] for _ in range(N + 1)]
# 빈 리스트를 만든다.

for _ in range(M):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
# 컴퓨터 번호 쌍을 입력받아 인접 리스트로 만든다.

infected = [False] * (N + 1)
# 감염 여부를 확인하기 위한 리스트를 만든다.

start = 1
# 컴퓨터 번호는 1번부터 시작한다.

stack = [start]
infected[start] = True

while stack:
    com_num = stack.pop()

    for adj in graph[com_num]:
        if not infected[adj]:
            infected[adj] = True
            stack.append(adj)
# 각 정점을 순회하며 연결된 정점을 모두 infected = True 처리한다.

print(infected.count(True) - 1)
# 순회가 끝나면 감염된 컴퓨터 수 중 제일 처음 감염된 컴퓨터 한 대를 제외한 값을 출력한다.


# 백준 4963 섬의 개수
import sys

dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]
# 8방향 순회를 위해 행과 열 리스트를 만든다.

while True:
    width, height = map(int, sys.stdin.readline().split())
    # 지도의 너비와 높이를 입력받는다.

    if width == 0 and height == 0:
        break
    # 입력에 0이 두 개 주어지면 반복문을 종료한다.

    graph = []
    
    for _ in range(height):
        graph.append(list(map(int, sys.stdin.readline().split())))
    # 지도를 이차원 리스트로 저장한다.
    
    cnt = 0
    # 섬의 개수를 세는 변수를 만든다.

    for h in range(height):
        for w in range(width):
            if graph[h][w] == 1:
                stack = [(h, w)]
                graph[h][w] = 0
                cnt += 1
    # 지도의 정사각형을 하나씩 순회한다.
    # 정사각형이 1(땅)일 경우 해당 영역을 0(바다)으로 바꾸고 카운트에 1을 더한다.

                while stack:
                    x, y  = stack.pop()
                    for i in range(8):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if 0 <= nx < height and 0 <= ny < width and graph[nx][ny] == 1:
                            stack.append((nx, ny))
                            graph[nx][ny] = 0
                # 1(땅)이었던 영역과 연결된 땅이 있는지 확인하기 위해 8방향 델타값을 순회한다.
                # 지도를 벗어나지 않는 8방향 영역 중 1(땅)이 있으면 해당 영역을 새로운 기준으로 삼고 0으로 바꾼다.
                # 이 과정을 연결된 땅이 더 이상 없을 때까지 반복한다.

    print(cnt)
    # 카운트된 섬의 개수를 출력한다.