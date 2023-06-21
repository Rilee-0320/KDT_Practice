# 백준 1547 공
cups = [[], [1], [0], [0]]
# 컵이 총 3개이고 1번 컵에 공이 들어 있는 상태로 시작한다.
# 인덱스는 0부터 시작하기 때문에 편의를 위해 빈 리스트를 맨 처음에 하나 더 추가해둔다.

N = int(input())
# 위치를 바꾸는 횟수 N을 입력받는다.

for _ in range(N):
    x, y = map(int, input().split())
    cups[x], cups[y] = cups[y], cups[x]
# N번 동안 입력받은 자리의 컵의 위치를 서로 맞바꾼다.

for i in range(len(cups)):
    if 1 in cups[i]:
        print(i)
# 컵의 이동이 끝난 후에는 현재 공(1)의 어디에 있는 확인하여 해당 위치 번호를 출력한다. 


# 백준 5576 콘테스트
w_score = []
k_score = []
# W 대학과 K 대학의 점수를 따로 저장할 리스트를 각각 만든다.

for i in range(20):
    if i < 10:
        w_score.append(int(input()))
    else:
        k_score.append(int(input()))
# 1~10번째 점수는 W 대학의 점수에, 11~20번째 점수는 K 대학의 점수 리스트에 추가한다.

w_score.sort(reverse=True)
k_score.sort(reverse=True)
# 각각의 리스트를 내림차순으로 정렬한다.

print(sum(w_score[0:3]), sum(k_score[0:3]))
# 각 리스트의 3번째 점수까지의 합을 출력한다.


# 백준 2846 오르막길
N = int(input())
# 상근이가 측정하는 높이의 개수를 입력받는다.
height = list(map(int, input().split()))
# 측정한 높이를 입력받고 리스트에 저장한다.

uphill = []
gap = 0
# 오르막길의 높이 차를 기록할 빈 리스트를 만들고 차이를 일시적으로 저장할 변수를 만들어 0으로 설정한다.

for i in range(N-1):
    if height[i] < height[i+1]:
        gap += height[i+1] - height[i]
    # 리스트의 높이를 하나씩 불러온다.
    # 불러온 수보다 다음 수가 더 클 경우 그 차이를 gap에 저장한다.
    else:
        uphill.append(gap)
        gap = 0
    # 불러온 수가 다음 수보다 같거나 낮을 경우 지금까지의 gap을 uphill 리스트에 저장한다.
    # gap은 다시 0으로 설정한다.
else:
    uphill.append(gap)
# 측정한 높이를 저장한 리스트의 모든 요소를 순회하고 끝이 났을 때 gap에 높이 차를 나타내는 수가 남아 있을 수 있기 때문에 uphill에 gap을 저장하고 끝낸다.

if sum(uphill) == 0:
    print(0)
# uphill 리스트의 총합이 0인 경우 오르막길이 없다는 의미이므로 0을 출력한다.
else:
    print(max(uphill))
# uphill 리스트의 총합이 0이 아닌 경우 가장 큰 오르막길의 크기를 출력한다.


# 백준 1251 단어 나누기
word = list(input())
# 단어를 입력받는다.

N = len(word)
# 단어의 길이를 N에 저장한다.

lst = []
# 뒤집힌 단어를 저장할 빈 리스트를 만든다.

for i in range(N-2):
    first = word[i::-1]
    # 단어를 세 부분으로 나누어봤을 때 첫 번째 부분은 총 단어 길이의 -2 길이까지 차지 가능하다.
    # 해당 부분을 뒤집어 first라는 변수에 저장한다.
    for j in range(i+1, N-1):
        second = word[j:i:-1]
        # 두 번째 부분은 첫 번째 부분이 차지한 끝에서부터 총 단어 길이의 -1 길이까지 차지 가능하다.
        # 해당 부분을 뒤집어 second라는 변수에 저장한다.
        for k in range(j+1, N):
            third = word[:j:-1]
            # 세 번째 부분은 두 번째 부분이 차지한 끝에서부터 총 단어 길이의 끝까지 차지 가능하다.
            # 해당 부분을 뒤집어 third라는 변수에 저장한다.
            reversed_word = first + second + third
            # 세 부분을 모두 합쳐 reversed_word라는 변수에 저장한다.
            lst.append(''.join(reversed_word))
            # reversed_word는 리스트의 형태이기 때문에 문자열로 합쳐 빈 리스트에 저장한다.

print((sorted(lst))[0])
# 리스트를 사전순으로 정렬하여 가장 첫 번째 문자열을 출력한다.