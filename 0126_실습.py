# # 백준 10101 삼각형 외우기
# numbers = []
# # 삼각형의 세 각을 저장할 빈 리스트 생성
# for i in range(3):
#     numbers.append(int(input()))
# numbers.sort()
# # 세 각을 입력받아 리스트에 저장하고 오름차순으로 정렬

# if sum(numbers) != 180:
#     print('Error')
# # 세 각의 합이 180이 아닐 경우 Error 출력

# else:
#     if numbers[0] == numbers[1] and numbers[1] == numbers[2]:
#         print('Equilateral')
#     # 세 각이 모두 같으면 'Equilateral' 출력
#     elif numbers[0] != numbers[1] and numbers[1] != numbers[2]:
#         print('Scalene')
#     # 세 각이 모두 다르면 'Scalene' 출력
#     else:
#         print('Isosceles')
#     # 그 외의 경우 'Isosceles' 출력


# # 백준 2720 세탁소 사장 동혁
# T = int(input())
# # 테스트 케이스 수 입력받기

# units = [25, 10, 5, 1]
# # 동전의 단위를 적은 리스트를 생성
# # 입력되는 숫자가 센트 기준이므로 단위 또한 센트 기준으로 한다.

# for t in range(T):
#     money = int(input())
# # 테스트 케이스 수만큼 for문을 돌려 거스름돈으로 줘야 할 금액을 입력받는다.
#     for unit in units:
#         print(money//unit, end=' ')
#         money -= unit * (money//unit)
#     # for문을 통해 쿼터($0.25)부터 차례대로 불러오며 거스름돈을 나눈다.
#     # 쿼터로 줄 수 있는 개수를 구했다면 출력하고 해당 금액만큼 거스름돈에서 감한 뒤 나머지 금액에 대해 똑같은 과정을 반복한다.


# # 백준 1453 피시방 알바
# N = int(input())
# # 손님의 수를 N으로 입력받는다.
# seat_list = []
# cnt = 0
# # 좌석 번호를 저장할 빈 리스트를 만들고 거절당하는 사람의 수를 세기 위해 cnt 변수에 0을 설정한다.

# customers = map(int, input().split())
# # 손님들이 각자 원하는 좌석 번호를 입력받는다.

# for customer in customers:
#     if customer not in seat_list:
#         seat_list.append(customer)
#     else:
#         cnt += 1
#     # 좌석 리스트에 손님들이 원하는 좌석 번호를 추가하고 이미 리스트에 번호가 있는 경우 이미 자리가 차있다는 의미이므로 cnt + 1 한다.

# print(cnt)
# # 거절당한 사람의 수 출력


# # 백준 10773 제로
# N = int(input())
# # 테스트 케이스 수를 입력받는다.
# numbers = []
# # 번호를 저장할 빈 리스트 생성

# for n in range(N):
#     number = int(input())
#     # 테스트 케이스 수만큼 for문을 돌려 번호를 입력받는다.
#     if number != 0:
#         numbers.append(number)
#     else:
#         numbers.pop()
#     # 입력받은 번호가 0이 아닐 경우 리스트에 추가한다.
#     # 입력받은 번호가 0일 경우 리스트에서 가장 최근에 추가된 값을 하나 삭제한다.

# print(sum(numbers))
# # 리스트에 저장된 숫자의 합을 출력


# # 백준 2161 카드 1
# N = int(input())
# # 카드 번호를 입력받는다.

# card_numbers = [n for n in range(1, N+1)]
# # 1부터 입력받은 카드 번호까지의 리스트를 만든다.

# while len(card_numbers) > 1:
#     print(card_numbers.pop(0), end=' ')
#     # 리스트의 첫 번째 숫자를 출력하고 삭제한다.
#     card_numbers.append(card_numbers.pop(0))
#     # 그 다음 숫자를 리스트의 맨 앞에서 삭제하는 동시에 끝에 추가한다.
#     # 이 과정을 카드가 한 장 남을 때까지 반복한다.
# print(card_numbers[0])
# # 마지막 남은 카드의 번호를 출력


# # 백준 9012 괄호
# # 방법(1)
# T = int(input())
# # 테스트 케이스 수 입력받기

# for t in range(T):
#     string = input()
#     # 테스트 케이스 수만큼 for문을 돌려 문자열 입력받기
#     PS = []
#     # 빈 리스트 만들기

#     for bracket in string:
#     # 입력받은 문자열을 한 글자씩 불러온다.
#         if bracket == '(':
#             PS.append(bracket)
#         # 불러온 글자가 '(' 일 경우 리스트에 저장한다.

#         elif bracket == ')':
#             if len(PS) != 0:
#                 PS.pop()
#             # 불러온 글자가 ')'일 경우 리스트에서 하나의 요소를 제거한다.
#             # 리스트에 요소가 없을 경우 오류가 발생할 수 있기 때문에 요소가 하나 이상일 경우에만 실행한다.
#             else:
#                 PS.append(bracket)
#                 break
#             # 리스트에 요소가 하나도 없는 경우 ')'를 추가하고 반복문을 멈춘다.

#     if len(PS) == 0:
#         print('YES')
#     # 리스트의 요소가 없다는 것은 모든 괄호가 양쪽 대칭으로 존재하는 것이기 때문에 YES 출력
#     else:
#         print('NO')
#     # 그 외의 경우 NO 출력

# 방법(2)
T = int(input())
# 테스트 케이스 수 입력받기
for t in range(T):
    string = input()
    cnt = 0
    # 테스트 케이스 수만큼 문자열을 입력받고 cnt라는 변수에 0을 저장
    
    for str in string:
        if str == '(':
            cnt += 1
        else:
            cnt -= 1
        # 입력받은 문자열에서 한 글자씩 불러오며 '('일 경우 cnt에 1을 더하고 ')'일 경우 1을 뺀다.
        
        if cnt < 0:
            break
        # ')' 문자열이 더 많아서 cnt 값이 음수가 되면 조건문을 멈춘다.
    
    if cnt == 0:
        print('YES')
    # cnt가 0인 경우 '('와 ')'가 올바르게 쌍을 이루고 있는 것이므로 YES 출력
    else:
        print('NO')
    # 그 외의 경우에는 NO 출력