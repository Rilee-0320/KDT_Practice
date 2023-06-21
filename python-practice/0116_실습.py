# 백준 10039번 평균 점수
score_list = []
new_score_list = []
for n in range(5):
    score = int(input())
    score_list.append(score)
for each_score in score_list:
    if each_score < 40:
        each_score = 40
        new_score_list.append(each_score)
    else:
        new_score_list.append(each_score)
print(int(sum(new_score_list) / 5))


# 백준 10871번 X보다 작은 수
a, b = map(int, input().split())
numbers = list(map(int, input().split()))
for number in numbers:
    if number < b:
        print(number, end=' ')


# 백준 2480번 주사위 세 개
numbers_list = sorted(list(map(int, input().split())))

if numbers_list[0] == numbers_list[1] == numbers_list[2]:
    print(10000 + numbers_list[0] * 1000)
elif numbers_list[0] != numbers_list[1] != numbers_list[2]:
    print(numbers_list[2] * 100)
else:
    print(1000 + numbers_list[1] * 100)


# 백준 10886번 0 = not cute / 1 = cute
# 방법 (1)
T =  int(input())
cnt_o = 0
cnt_x = 0
answers = []
for t in range(T):
    answer = int(input())
    answers.append(answer)
    for a in answers:
        if answer == 1:
            cnt_o += 1
        else:
            cnt_x += 1
if cnt_o > cnt_x:
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')

# 방법 (2)
T =  int(input())
answers = []
for t in range(T):
    answer = int(input())
    answers.append(answer)
if answers.count(1) > answers.count(0):
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')


# 백준 2506번 점수 계산
# 방법 (1)
number_of_questions = int(input())
answers = list(map(int, input().split()))
score = 0
score_list = []
for answer in answers:
    if answer == 1:
        score += 1
        score_list.append(score)
    else:
        score = 0
print(sum(score_list))

# 방법 (2)
number_of_questions = int(input())
answers = list(map(int, input().split()))

while True:
    total = 0
    score = 0
    for answer in answers:
        if answer == 1:
            score += 1
            total += score
        else:
            score = 0
    print(total)
    break