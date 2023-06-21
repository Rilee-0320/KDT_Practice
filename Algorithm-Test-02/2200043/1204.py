# SWEA 1204 최빈수 구하기

# 테스트 케이스 수 입력받기
T = int(input())

# 테스트 케이스 수만큼 for문을 사용하여 입력값 받기
for t in range(1, T + 1):
    n = int(input())
    numbers = map(int, input().split())
    # 입력한 숫자(key)와 빈도수(value)를 짝으로 하는 딕셔너리 생성
    dict = {} 
    # 최빈수가 여러 개일 경우를 위한 리스트 생성
    max_list = []
    for number in numbers:
        # 딕셔너리에 키-값 넣기
        if number not in dict:
            dict[number] = 1
        else:
            dict[number] += 1
    # 딕셔너리 값이 가장 큰 수(최빈수)의 key를 리스트에 넣기
    for key, value in dict.items():
        if value == max(dict.values()): 
            max_list.append(key)
    # 최빈수가 여러 개일 경우 리스트 안에서 가장 큰 수 출력
    print(f'#{n} {max(max_list)}')