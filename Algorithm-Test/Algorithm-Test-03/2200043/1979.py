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