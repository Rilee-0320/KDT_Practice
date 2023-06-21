# 서랍의 비밀번호
number = list(map(int, input().split()))
cnt = 0
while number[0] != number[1]:
    cnt += 1
    number[1] += 1
print(cnt + 1)