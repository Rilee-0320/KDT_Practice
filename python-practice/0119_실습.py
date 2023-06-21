# 백준 2576번 홀수
dict = {
    'even' : [],
    'odd' : []
}
for i in range(7):
    number = int(input())
    if number % 2 == 0:
        dict['even'].append(number)
    else:
        dict['odd'].append(number)

if dict['odd'] == []:
    print(-1)
else:
    print(sum(dict['odd']), min(dict['odd']), sep='\n')


# 백준 10822번 더하기
print(sum(map(int, input().split(','))))


# 백준 2754번 학점계산
grade = {
    'A+': 4.3, 'A0': 4.0, 'A-': 3.7,
    'B+': 3.3, 'B0': 3.0, 'B-': 2.7,
    'C+': 2.3, 'C0': 2.0, 'C-': 1.7,
    'D+': 1.3, 'D0': 1.0, 'D-': 0.7,
    'F': 0.0
}

print(grade[input()])


# 백준 5622번 다이얼
dial_dict = {
    'ABC': 3,
    'DEF': 4,
    'GHI': 5,
    'JKL': 6,
    'MNO': 7,
    'PQRS': 8,
    'TUV': 9,
    'WXYZ': 10,
    '0': 11
}

str = input()
total = 0
for key in dial_dict.keys():
    for char in str:
        if char in key:
            total += dial_dict[key]
print(total)


# 백준 2577번 숫자의 개수
a = int(input())
b = int(input())
c = int(input())
multiply = a * b * c

dict = {}
for char in str(multiply):
    if char not in dict:
        dict[char] = 1
    else:
        dict[char] += 1

one_to_nine = [dict.get(str(i), 0) for i in range(1, 10)]
print(dict.get('0', 0), *one_to_nine, sep='\n')


# 백준 7785번 회사에 있는 사람
T = int(input())
inside = []
company = {}
for t in range(T):
    a, b = input().split()
    company[a] = b
for key in company.keys():
    if company[key] == 'enter':
        inside.append(key)
print(*sorted(inside, reverse=True), sep='\n')