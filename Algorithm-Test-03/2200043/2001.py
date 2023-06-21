# SWEA 2001 파리 퇴치
T = int(input())
# 테스트 케이스 수를 입력받는다.

for t in range(1, T+1):
    N, M = map(int, input().split())
    # 영역의 크기 N과 파리채의 크기 M을 입력받는다.

    numbers = []
    # 빈 리스트를 만든다.

    for _ in range(N):
        numbers.append(list(map(int, input().split())))
    # 파리의 개수를 의미하는 숫자들을 입력받아 이차원 리스트로 저장한다.
    
    max_total = 0
    # 최대한 많은 파리를 잡는 경우의 값을 찾기 위해 max_total 변수를 만들고 0을 저장한다.

    for i in range(N-M+1):
        for j in range(N-M+1):
    # 전체 영역은 'N-M+1'만큼 돈다.
    # 가령 전체 영역이 5*5이고 파리채가 2*2 크기라면 행과 열마다 각각 'N-M+1', 즉 4회씩 돌아야 한다.

            total = 0
            # 각 경우의 총합을 구하기 위해 total 변수를 만들고 0을 저장한다.

            for r in range(M):
                for c in range(M):
                    total += numbers[i + r][j + c]
            # 파리채 크기만큼만 순회하며 파리를 몇 마리씩 잡는지 구한다.

            if total > max_total:
                max_total = total
            # 잡은 파리의 수가 max_total보다 클 경우 max_total에 해당 값을 저장한다.

    print(f'#{t} {max_total}')
    # M 크기의 파리채로 가장 많이 잡을 파리의 수를 출력한다.
