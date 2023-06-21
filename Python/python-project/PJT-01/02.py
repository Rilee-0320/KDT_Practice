with open('02.txt', 'w', encoding='UTF8') as f:
    t = open('./data/fruits.txt', 'r', encoding='UTF8')
    cnt = 0
    for fruit in list(t):
        cnt += 1
    f.write(str(cnt))
    t.close()

# 모범 답안
# count = 0

# with open('./data/fruits.txt', 'r') as f:
#     lines = f.readlines()
#     for line in lines:
#         count += 1

# with open('./02.txt', 'w') as f:
#     f.write(str(count))
