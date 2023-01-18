# 백준 2789번 유학 금지
input_word = input()

forbidden_char = [i for i in 'CAMBRIDGE']
new_word = ''
for char in input_word:
    if char not in forbidden_char:
        new_word += char
print(new_word)


# 백준 2675번 문자열 반복
T = int(input())
for t in range(T):
    a, b = map(str, input().split())
    new_word = ''
    for char in b:
        new_word += char * int(a)
    print(new_word)


# 백준 10988번 팰린드롬인지 확인하기
word = input()
reversed_word = ''
for char in word[::-1]:
    reversed_word += char
if reversed_word == word:
    print(1)
else:
    print(0)


# 백준 17249번 태보태보 총난타
taebo = input().split('(^0^)')
for t in taebo:
    print(t.count('@'), end=' ')


# 백준 2941번 크로아티아 알파벳
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
str = input()
cnt = 0
for char in croatia:
    if char in str:
        str = str.replace(char, '!')
print(len(str))


# 백준 10809번 알파벳 찾기
S = input()
for i in range(ord('a'), ord('z') + 1):
    if chr(i) in S:
        print(S.index(chr(i)), end=' ')
    else:
        print(-1, end = ' ')