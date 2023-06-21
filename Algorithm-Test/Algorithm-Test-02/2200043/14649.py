# SWEA 14649 신용카드 만들기 1

# 테스트 케이스 수 입력받기
T = int(input())

# 테스트 케이스 수만큼 for문을 사용하여 입력값 받기
for t in range(1, T + 1):
    numbers = list(map(int, input().split()))
    total = 0
    # 실제로 홀수 자리는 range(0)에서부터 시작하므로 홀수자리 조건과 짝수자리 조건을 반대로 집어넣기
    for i in range(15):
        if i % 2 == 1:
            total += numbers[i]
        else:
            total += numbers[i] * 2
    # 15자리의 총합이 10으로 나누어 떨어지면 0 출력
    if total % 10 == 0:
        print(f'#{t} 0')
    # 15자리의 총합이 10으로 나누어 떨어지지 않으면 총합을 10으로 나누어 나머지를 구하고 그 나머지를 10에서 빼 10을 만들기 위한 숫자를 알아낸다.
    else:
        print(f'#{t} {10 - (total % 10)}')