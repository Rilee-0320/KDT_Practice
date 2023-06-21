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