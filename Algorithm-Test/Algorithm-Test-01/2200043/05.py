T = int(input())
for t in range(1, T + 1):
    number = int(input())
    new_set = set()
    cnt = 0
    n = 1
    while number * n:
        quotient = (number * n) // 10
        remainder = (number * n) % 10
        new_set.add(quotient)
        new_set.add(remainder)
        cnt = cnt + 1
        n = n + 1
        if sorted(new_set) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
            break
    print(cnt)