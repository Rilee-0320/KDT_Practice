# 백준 9498번 시험 성적
score = [n for n in range(0, 101)]
N = int(input())
if N in score[90:]:
    print('A')
elif N in score[80:90]:
    print('B')
elif N in score[70:80]:
    print('C')
elif N in score[60:70]:
    print('D')
else:
    print('F')


# 백준 9093번 단어 뒤집기
T = int(input())

for t in range(T):
    reversed_sentence = []
    sentence = input().split()
    for word in sentence:
        reversed_sentence.append(word[::-1])
    print(*reversed_sentence)


# 백준 11721번 열 개씩 끊어 출력하기
str = input()

while True:
    print(str[:10])
    str = str.replace(str[:10], '')
    if len(str) < 10:
        print(str)
        break


# 백준 2947번 나무 조각
N = list(map(int, input().split()))

while True:
    for n in range(len(N)-1):
        if N[n] > N[n + 1]:
            N[n], N[n + 1] = N[n + 1], N[n]
            print(*N)
    if N == [1, 2, 3, 4, 5]:
        break