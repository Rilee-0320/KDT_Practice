# 백준 1000번 A+B
a, b = map(int, input().split())
print(a + b)


# 백준 2558번 A+B - 2
total = 0
for i in range(2):
    n =  int(input())
    total += n
print(total)


# 백준 10950번 A+B - 3
T = int(input())
for t in range(T):
    a, b = map(int, input().split())
    print(a + b)


# 백준 10953번 A+B - 6
T = int(input())
for t in range(T):
    a, b =  map(int, input().split(','))
    print(a + b)


# 백준 11021번 A+B - 7
T = int(input())
for t in range(1, T + 1):
    a, b = map(int, input().split())
    print(f'Case #{t}: {a + b}')


# 백준 11022번 A+B - 8
T =  int(input())
for t in range(1, T + 1):
    a, b = map(int, input().split())
    print(f'Case #{t}: {a} + {b} = {a + b}')