# SWEA 5431 민석이의 과제 체크하기
T = int(input())
# 테스트 케이스 수를 입력받는다.

for t in range(1, T + 1):
    students, o_task = map(int, input().split())
    submit = list(map(int, input().split()))
    x_task = ''
# 테스트 케이스 수만큼 반복문을 돌려 학생의 총수, 제출한 학생의 수, 제출한 학생의 번호를 입력받는다.
# 과제를 내지 않은 학생의 번호를 파악하기 위해 빈 문자열을 만든다.

    for n in range(1, students + 1):
        if n not in submit:
            x_task += str(n) + ' '
    # 학생의 총수만큼 반복문을 돌려 과제를 제출한 학생 리스트에 없는 번호를 확인한다.
    # 과제를 제출하지 않은 학생의 번호를, 뒤 띄어쓰기 공백과 함께 문자열에 저장한다.

    
    print(f'#{t} {x_task}')
    # 과제를 제출하지 않은 학생의 번호를 출력한다.