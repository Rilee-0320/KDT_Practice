# 백준 2525 오븐 시계
hour, minute = map(int, input().split())
# 현재 시간을 입력받는다.
cooking_time = int(input())
# 요리하는 데 걸리는 분단위 시간을 입력받는다.

minute = minute + cooking_time
# 현재 시각의 분에 요리 소요 시간을 더해준다.

if minute >= 60:
    hour += minute // 60
    minute = minute % 60
# 분이 60 이상일 경우 분을 60으로 나눈 몫을 시간에 더해주고 나머지는 분에 저장한다.
if hour >= 24:
    hour = hour - 24
# 시간이 24를 넘을 경우 해당 시간에서 24를 뺀다.

print(hour, minute)
# 요리가 완료된 시각을 출력한다.


# 백준 2798 블랙잭
N, M = map(int, input().split())
# 카드의 개수 N과 게임의 기준이 되는 카드의 합 M을 입력받는다.

numbers = list(map(int, input().split()))
# 카드 숫자들을 입력받아 리스트에 저장한다.
total = 0
# M 이하의 가장 큰 카드의 합을 구하기 위해 'total'이라는 변수에 0을 저장한다.

for x in range(N-2):
    for y in range(x+1, N-1):
        for z in range(y+1, N):
            if total < numbers[x]+numbers[y]+numbers[z] <= M:
                total = numbers[x]+numbers[y]+numbers[z]
# 삼중 for문을 통해 카드의 값들을 하나씩 불러온다.
# 카드의 합이 M보다는 같거나 작되 가장 큰 카드의 합을 total 변수에 저장한다.

print(total)
# total 값을 출력한다.


# 백준 9076 점수 집계
T = int(input())
# 테스트 케이스 수를 입력받는다.

numbers = []
# 심사위원들의 점수를 저장할 빈 리스트를 만든다.

for _ in range(T):
    numbers.append(sorted(list(map(int, input().split()))))
# 심사위원들의 점수를 오름차순으로 정렬하여 리스트에 저장한다.

for num in numbers:
    if abs(num[1] - num[3]) >= 4:
        print('KIN')
    else:
        print(sum(num[1:4]))
# 테스트 케이스별로 가장 낮은 점수 인덱스[0] 값과 가장 높은 점수 인덱스[4] 값은 제외하고 생각한다.
# 중간 점수 세 개 중 가장 높은 점수와 낮은 점수의 차가 4 이상일 경우 'KIN'을 출력한다.
# 그 외에는 세 개의 점수 총합을 출력한다.


# 백준 1526 가장 큰 금민수
N = int(input())
# 숫자 N을 입력받는다.
lst = []
# 숫자 4와 7로만 이루어진 숫자를 저장할 빈 리스트를 만든다.

for i in range(N+1):
    i = str(i)
    if i.count('4') + i.count('7') == len(i):
        lst.append(int(i))
# 4부터 N까지 for문을 돌려 숫자를 하나씩 확인한다.
# 숫자를 일단 문자열로 변환하고 그 안에 4와 7이 있는 개수가 자릿수와 같은지 비교한다.
# 4와 7의 개수가 자릿수와 같을 경우 4와 7로만 이루어진 숫자이기 때문에 리스트에 저장한다.

print(max(lst))
# 리스트에 저장된 값들 중 가장 큰 수를 출력한다.


# 백준 1436 영화 감독 숌
N = int(input())
# 몇 번째 영화인지 숫자를 입력받는다.

lst = []
# 숫자 666이 들어간 숫자를 저장하기 위해 빈 리스트를 만든다.

i = 666
# 6이 적어도 3개 이상 연속으로 들어간 수 중 가장 작은 수는 666이기 때문에 초기값으로 666을 설정한다.

while True:
    if '666' in str(i):
        lst.append(i)
    # while문을 통해 666이 들어가는 숫자는 리스트에 저장한다.

        if lst.index(i) == N-1:
            print(i)
            break
        # 만약 저장한 숫자의 인덱스값이 N-1이면 해당 수를 출력하고 반복문을 멈춘다.
        # 인덱스값은 0부터 시작하기 때문에 찾고자 하는 영화의 순서-1과 동일하면 된다.
    i += 1
    # if 조건문을 충족하지 않을 경우 숫자를 1씩 늘려가며 반복한다.