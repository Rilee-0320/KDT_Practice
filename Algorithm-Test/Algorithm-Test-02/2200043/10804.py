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