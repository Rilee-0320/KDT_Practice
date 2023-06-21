# 백준 10817 세 수
numbers = list(map(int, input().split()))
# 숫자들을 입력받아 리스트에 저장한다.
numbers.sort(reverse=True)
# 리스트를 내림차순으로 바꾼다.
print(numbers[1])
# 두 번째 큰 값을 출력한다.


# 백준 20001 고무오리 디버깅
start = input()
# 다른 문장과는 별개로 '고무오리 디버깅 시작' 문장을 입력받는다.
list = []
# 입력되는 문자열을 저장할 빈 리스트를 생성한다.

while True:
    str = input()
    # 문자열을 입력받는다.
    if str == '고무오리 디버깅 끝':
        break
    # '고무오리 디버깅 끝'이 입력되면 반복문을 멈춘다.
    elif str == '문제':
        list.append(str)
    # '문제'라는 문자열이 입력되면 리스트에 추가한다.
    else:
        if list:
            list.pop()
        # '고무오리'라는 문자열이 입력됐을 경우 리스트에 요소가 있으면 해당 요소를 삭제한다.
        else:
            list.append('문제')
            list.append('문제')
        # '고우오리'라는 문자열이 입력됐을 경우 리스트에 어떠한 요소도 없다면 '문제'라는 문자열을 두 개 추가한다.

if list:
    print('힝구')
# 리스트에 요소가 남아있다는 것은 모든 문제를 해결하지 못했다는 의미이므로 '힝구' 출력
else:
    print('고무오리야 사랑해')
# 리스트에 남은 요소가 없다는 것은 모든 문제를 해결했다는 의미이므로 '고무오리야 사랑해' 출력


# 백준 1269 대칭 차집합
a, b = map(int, input().split())
# A 집합과 B 집합의 원소 개수를 입력받는다.
A = set(map(int, input().split()))
# A 집합의 원소를 set으로 입력받는다.
B = set(map(int, input().split()))
# B 집합의 원소를 set으로 입력받는다.

print(len(A^B))
# A, B 집합의 대칭 차집합 원소 개수를 출력한다.


# 백준 3052 나머지
remainder = set()
# remainder(나머지)라는 이름의 빈 set 생성

for _ in range(10):
    number = int(input())
    remainder.add(number%42)
    # for문을 돌려 10회 동안 숫자를 입력받고 그 숫자를 42로 나눈 나머지를 set에 저장한다.
print(len(remainder))
# set에는 중복된 요소가 저장되지 않으므로 set의 요소 개수를 출력하여 서로 다른 나머지가 몇 개인지 알 수 있다.


# 백준 1181 단어 정렬
# 방법(1)
import heapq

N = int(input())
set = set()
heap = []
# 단어의 개수 N을 입력받고 빈 set와 빈 리스트를 생성한다.

for _ in range(N):
    string = input()
    set.add(string)
    # 중복된 단어를 제거한 목록을 만들기 위해 입력된 단어를 set에 저장한다.
for str in set:
    heapq.heappush(heap, (len(str), str))
    # set에 저장된 단어(중복이 없는 단어들)를 하나씩 불러오며 (단어의 길이, 단어) 형식의 튜플로 리스트에 저장한다.
while len(heap) > 0:
    print(heap[0][1])
    heapq.heappop(heap)
    # while문을 통해 heap의 요소를 하나씩 출력 및 삭제하고 빈 리스트가 될 때까지 반복한다.

# 방법(2)
N = int(input())
set = set()
words = []
# 단어의 개수 N을 입력받고 빈 set와 빈 리스트를 생성한다.

for _ in range(N):
    string = input()
    set.add(string)
    # 중복된 단어를 제거한 목록을 만들기 위해 입력된 단어를 set에 저장한다.
for str in set:
    words.append((len(str), str))
    # set에 저장된 단어(중복이 없는 단어들)를 하나씩 불러오며 (단어의 길이, 단어) 형식의 튜플로 리스트에 저장한다.

for length, word in sorted(words, key=lambda x: (x[0], x[1])):
    print(word)
# 람다 함수를 사용해 1차적으로는 단어의 길이에 따라 정렬, 길이가 같을 경우 2차적으로는 단어 순으로 정렬한다.
# 그 후 정렬된 단어만 출력


# 백준 11286 절댓값 힙
import sys
import heapq

N = int(sys.stdin.readline())
heap = []
# 연산의 개수 N을 입력받는다.
# 빈 리스트를 생성한다.

for _ in range(N):
    num = int(sys.stdin.readline())
    # for문을 N만큼 돌리며 숫자를 입력받는다.
    if num == 0:
        if heap:
            print(heap[0][1])
            heapq.heappop(heap)
        # 입력받은 숫자가 0인데 리스트에 요소가 있을 경우 첫 번째 요소(튜플)의 숫자를 출력한다.
        # 그리고 해당 요소를 리스트에서 삭제한다.
        else:
            print(0)
        # 입력받은 숫자가 0인데 리스트에 비어 있는 경우 0을 출력한다.
    
    else:
        if num < 0:
            heapq.heappush(heap, (num * -1, num))
        # 입력받은 숫자가 음수일 경우 (절댓값, 숫자) 형식의 튜플로 리스트에 저장한다.       
        else:
            heapq.heappush(heap, (num, num))
        # 입력받은 숫자가 양수일 경우 (숫자, 숫자) 형식의 튜플로 리스트에 저장한다.