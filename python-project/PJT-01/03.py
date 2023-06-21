with open('03.txt', 'w', encoding='UTF8') as f:
    t = open('./data/fruits.txt', 'r', encoding='UTF8')
    fruit_list = list(t)
    new_list = []
    cnt = 0
    for fruit in fruit_list:
        if fruit not in new_list:
            if fruit.endswith('berry\n'):
                new_list.append(fruit)
    f.write(str(len(new_list)) + '\n')
    for i in new_list:
        f.write(i)
    t.close()

# 모범 답안
# fruit_list = []
# fruit_count = 0

# with open('./data/fruits.txt', 'r') as f:
#     fruits = f.readlines()
#     for fruit in fruits:
#         fruit = fruit.strip()
#         if fruit[-5:] == 'berry':
#             if fruit not in fruit_list:
#                 fruit_list.append(fruit)
#                 fruit_count += 1

# with open('./03.txt', 'w') as f:
#     f.write(str(fruit_count) + '\n')

#     for fruit in fruit_list:
#         f.write(fruit + '\n')

