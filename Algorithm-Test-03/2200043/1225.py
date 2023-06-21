# SWEA 1225 암호생성기
from collections import deque
# 덱을 사용하여 풀이했다.

for t in range(1, 11):
# 테스트 케이스 수가 문제에서는 주어지지 않았으나 input.txt 파일에 10개의 경우가 있어 range 범위를 1~10까지로 설정했다.
    N = int(input())
    # 순서를 입력받는다.
    numbers = deque(list(map(int, input().split())))
    # 숫자를 입력받는다.
    minus = 1
    # 순회하며 뺄 숫자를 1로 설정한다.
    while True:
        if minus > 5:
            minus = 1
        # 순회하며 감소할 숫자는 5가 최대이므로 5를 초과하면 1로 초기화한다.

        numbers.append(numbers[0] - minus)
        numbers.popleft()
        # 맨 처음 수에서 1~5를 빼고 제일 마지막에 추가한다.
        # 그리고 해당 숫자는 제거한다.

        if numbers[-1] <= 0:
            numbers[-1] = 0
            break
        # 제일 마지막 수가 0보다 작아질 경우 0으로 저장하고 반복문을 멈춘다.

        minus += 1
        # 그 어떤 조건에도 걸리지 않을 경우 감소할 수를 1 높인다.
    
    number = ''
    for num in numbers:
        number += str(num) + ' '
    print(f'#{t} {number}')
    # 반복문이 끝난 암호 배열을 문자열에 담아 테스트 케이스 순서와 함께 출력한다.