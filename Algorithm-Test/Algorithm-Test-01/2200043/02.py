# 연월일 달력
T = int(input())
for t in range(1, T + 1):
    numbers = input().split()
    for number in numbers:
        year = number[0:4]
        month = number[4:6]
        day = number[6:8]
        if int(month) > 12 or int(month) < 1:
            print(f'#{t} -1')
            break
        else:
            if month == '02':
                if int(day) > 28:
                    print(f'#{t} -1')
                    break
            elif month == '04' or '06' or '09' or '11':
                if int(day) > 30:
                    print(f'#{t} -1')
                    break
            else:
                if int(day) > 31:
                    print(f'#{t} -1')
                    break
        print(f'#{t} {year}/{month}/{day}')