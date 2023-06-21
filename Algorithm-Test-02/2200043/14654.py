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