# SWEA 10505 소득 불균형

# 테스트 케이스 수 입력받기
T = int(input())

# 테스트 케이스 수만큼 for문을 사용하여 입력값 받기
for t in range(1, T + 1):
    # 사람의 수를 N으로 입력 받기 
    N = int(input())
    # N명의 소득 입력 받기
    incomes = list(map(int, input().split()))
    # 평균 이하의 소득을 가진 사람을 담을 리스트 생성
    less = []
    # N의 소득 중 평균 이하의 소득을 가진 사람을 리스트에 추가
    for income in incomes:
        if income <= (sum(incomes) / N):
            less.append(income)
    # 리스트에 속한 사람의 수 출력
    print(f'#{t} {len(less)}')