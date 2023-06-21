# SWEA 3456 직사각형 길이 찾기

# 테스트 케이스 수 입력받기
T = int(input())

# 테스트 케이스 수만큼 for문을 사용하여 입력값 받기
for t in range(1, T + 1):
    # 직사각형이므로 4개의 숫자 중 2개씩 같은 수
    a, b, c = sorted(list(map(int, input().split())))
    # 입력값을 오름차순으로 sort했기 때문에 a와 b가 같을 경우 c 값만 다르므로 c 값을 출력
    if a == b: 
        print(f'#{t} {c}')
    # 입력값을 오름차순으로 sort했기 때문에 a와 b가 다를 경우 a 값만 다르므로 a 값을 출력
    else: 
        print(f'#{t} {a}')