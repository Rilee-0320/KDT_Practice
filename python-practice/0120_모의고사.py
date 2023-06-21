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


# SWEA 10804 문자열의 거울상

# 테스트 케이스 수 입력받기
T = int(input())

# 테스트 케이스 수만큼 for문을 사용하여 입력값 받기
for t in range(1, T + 1):
    str = input()
    # 기존의 문자와 바뀌어져 나와야 할 문자를 키-값으로 딕셔너리에 저장
    dict ={'b':'d', 'd':'b', 'p':'q', 'q':'p'}
    # 새로운 문자를 만들기 위한 빈 문자열 생성
    new_word = ''
    # 맨 처음 입력 문자열의 글자를 뒤에서부터 한글자씩 불러와 그에 해당하는 딕셔너리의 값을 새로운 문자열에 추가
    for char in str[::-1]:
        new_word += dict[char]
    print(f'#{t} {new_word}')


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


# SWEA 14654 신용카드 만들기 2

# 테스트 케이스 수 입력받기
T = int(input())

# 테스트 케이스 수만큼 for문을 사용하여 입력값 받기
for t in range(1, T + 1):
    numbers = input()
    # 카드 번호로 시작해야 하는 숫자를 담은 리스트 생성
    start_number = ['3', '4', '5', '6', '9']
    # 입력 숫자열의 시작번호가 3,4,5,6,9가 아니면 0 출력
    if numbers[0] in start_number:
        # 이중 조건문을 통해 '-'를 제거한 글자수가 16자리일 경우 1을, 아닐 경우 0 출력
        numbers = numbers.replace('-', '')
        if len(numbers) == 16:
            print(f'#{t} 1')
        else:
            print(f'#{t} 0')
    else:
        print(f'#{t} 0')