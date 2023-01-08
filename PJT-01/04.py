with open('04.txt', 'w', encoding='UTF8') as f:
    t = open('data/fruits.txt', 'r', encoding='UTF8')
    dict = {}
    for fruit in list(t):
        fruit = fruit.replace('\n', '')
        if fruit not in dict:
            dict[fruit] = 1
        else:
            dict[fruit] += 1

    for key, value in dict.items():
        f.write(f'{key} {value}\n')
    t.close()

# 모범 답안
# fruit_dict = {}

# with open('./data/fruits.txt', 'r') as f:
#     fruits = f.readlines()
#     for fruit in fruits:
#         fruit = fruit.strip()

#         if fruit not in fruit_dict:
#             fruit_dict[fruit] = 1

#         elif fruit in fruit_dict:
#             fruit_dict[fruit] += 1

# with open('./04.txt', 'w') as f:
#     for fruit, count in fruit_dict.items():
#         f.write(f'{fruit} {count} \n')