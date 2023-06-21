# 백준 9085번 더하기
T = int(input())
for t in range(T):
    N = int(input())
    list = [n for n in map(int, input().split())]
    print(sum(list))


# 백준 10824번 네 수
number_list = input().split()
number1 = ''
number2 = ''
for i in range(4):
    if i < 2:
        number1 += number_list[i]
    else:
        number2 += number_list[i]
print(int(number1) + int(number2))


# 백준 3009번 네 번째 점
# 방법 (1)
x_list = []
y_list = []
for t in range(3):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)
if sorted(x_list)[0] == sorted(x_list)[1]:
    new_x = sorted(x_list)[2]
else:
    new_x = sorted(x_list)[0]
if sorted(y_list)[0] == sorted(y_list)[1]:
    new_y = sorted(y_list)[2]
else:
    new_y = sorted(y_list)[0]
print(new_x, new_y)

# 방법 (2)
x_list = []
y_list = []
for t in range(3):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

for i in range(3):
    for x in x_list:
        if x_list.count(x) == 1:
            new_x = x
    for y in y_list:
        if y_list.count(y) == 1:
            new_y = y
print(new_x, new_y)


# 백준 10952번 A+B - 5
while True:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    print(a + b)


# 백준 1110번 더하기 사이클
N = int(input())
number_list = []
cnt = 0
while True:
    number_list.append(N)
    a = N // 10
    b = N % 10
    N = (b * 10) + ((a + b) % 10)
    if N not in number_list:
        cnt += 1
    else:
        cnt += 1
        print(cnt)
        break