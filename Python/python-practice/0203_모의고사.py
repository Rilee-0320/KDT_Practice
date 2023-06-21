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


# SWEA 1983 조교의 성적 매기기
T = int(input())
# 테스트 케이스 수를 입력받는다.

grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
# 학점 리스트를 만든다.

for t in range(1, T+1):
    N, K = map(int, input().split())
    scores = []
    # 학생 총수와 학점이 알고 싶은 학생의 번호를 입력받는다.
    # 점수를 저장할 빈 리스트를 만든다.

    for n in range(N):
        mid, final, task = map(int, input().split())
        scores.append([n+1, mid*0.35 + final*0.45 + task*0.2])
    # 학생들의 총점을 [학생 번호, 총점] 형태로 리스트에 저장한다.

    cnt = 0
    grade_num = 0
    # 학점을 부여할 때 N // 10을 계산하기 위 cnt 변수를 만들고 0을 저장한다.
    # 학점 리스트의 인덱스에 사용할 변수 grade_num을 만들고 0을 저장한다.


    for score in sorted(scores, key = lambda x:x[1], reverse=True):
        score[1] = grade[grade_num]
        cnt += 1
        if cnt == N // 10:
            grade_num += 1
            cnt = 0
    # 학생들의 총점 리스트를 총점을 기준으로 하여 내림차순으로 정렬한다.
    # [학생 번호, 총점] 형태로 되어 있는 형태에 총점 대신 학점을 입력한다.
    # 학점을 입력하면서 1씩 카운트하고 그 수가 N // 10이 되면 학점을 하나 낮추어 입력한다.


    print(f'#{t} {scores[K-1][1]}')
    # 찾고자 했던 학생의 학점을 출력한다.


# SWEA 1979 어디에 단어가 들어갈 수 있을까
T = int(input())
# 테스트 케이스 수를 입력받는다.

for t in range(1, T+1):
    N, K = map(int, input().split())
    # 단어 퍼즐의 크기 N과 특정 길이 K를 입력받는다.

    num_lst = []
    # 1과 0으로 표시된 퍼즐의 모양을 입력받는다.

    for n in range(N):
        num_lst.append(input().split())
    # 각 줄의 번호를 이차원 리스트로 저장한다.
    
    # 가로 구하기
    x_num_lst = num_lst
    x_cnt = 0
    # 가로에서 K 길이의 단어를 찾기 위해 똑같은 이차원 리스트를 만든다.
    # K 길이의 가로 단어가 들어갈 곳을 찾기 위해 x_cnt 변수를 만들고 0을 저장한다.

    for x_num in x_num_lst:
        x_n = ''.join(x_num)
        for x_str in x_n.split('0'):
            if x_str == '1'*K:
                x_cnt += 1
    # 이차원 리스트 속 리스트를 하나씩 불러와 하나의 문자열로 합치고 '0' 기준으로 쪼갠다.
    # 쪼갠 요소들에 ('1' * K)의 형태가 있다면 카운트한다. 
    

    # 세로 구하기
    y_num_lst = [[] for _ in range(N)]
    y_cnt = 0
    # 세로에서 K 길이의 단어를 찾기 위해 빈 이차원 리스트를 만든다.
    # K 길이의 세로 단어가 들어갈 곳을 찾기 위해 y_cnt 변수를 만들고 0을 저장한다.

    for i in range(N):
        for j in range(N):
            y_num_lst[i].append(num_lst[j][i])
    # 본래 이차원 리스트에서 세로 방향으로 순회하며 이차원 리스트를 만든다.

    for y_num in y_num_lst:
        y_n = ''.join(y_num)
        for y_str in y_n.split('0'):
            if y_str == '1' * K:
                y_cnt += 1
    # 이차원 리스트 속 리스트를 하나씩 불러와 하나의 문자열로 합치고 '0' 기준으로 쪼갠다.
    # 쪼갠 요소들에 ('1' * K)의 형태가 있다면 카운트한다.

    print(f'#{t} {x_cnt + y_cnt}')
    # 가로 단어를 카운트한 것과 세로 단어를 카운트한 것을 합쳐 출력한다.


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


# SWEA 1218 괄호 짝짓기
for t in range(1, 11):
    N = int(input())
    # 테스트 케이스의 길이를 입력받는다.
    str = input()
    # 문자열을 입력받는다.

    dict = {
        '(' : 1, '[' : 2, '{' : 3, '<' : 4,
        ')' : -1, ']' : -2, '}' : -3, '>' : -4}
    # 딕셔너리를 생성해 위와 같이 여는 괄호와 닫는 괄호를 각각 양수와 음수로 저장한다. 

    total = 0
    # 문자열의 유효성을 판단하기 위해 total이라는 변수를 만들고 0을 저장한다.

    for i in str:
        total += dict[i]
        # 문자열의 한 글자씩 불러오며 해당 값을 total에 더한다.

        if total < 0:
            print(f'#{t} 0')
            break
        # total이 음수인 경우 닫는 괄호가 먼저 나왔다는 의미이므로 유효하지 않은 문자열이므로 0을 출력하고 반복문을 멈춘다.
    else:
        if total == 0:
            print(f'#{t} 1')
        # 모든 반복이 끝났을 때 total 값이 0이라는 것은 여는 괄호와 닫는 괄호의 수가 동일한 유효한 문자열이라는 의미이므로 1을 출력한다.
        else:
            print(f'#{t} 0')
        # total 값이 1 이상으로 남아있는 경우 여는 괄호가 남아있다는 의미이므로 유효하지 않은 문자열이다. 따라서 0을 출력한다.