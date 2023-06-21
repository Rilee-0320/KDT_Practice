# 예제 1
dict_variable = {}
dict_variable["이름"] = "정우영"
dict_variable["생년월일"] = "19000101"
dict_variable["회사"] = "하이퍼그로스"

print(dict_variable["이름"]) # 정우영
print(dict_variable["생년월일"]) # 19000101
print(dict_variable["회사"]) # 하이퍼그로스


# 예제 2
dict_variable = {"a": "A", "B": "b"}
dict_variable["c"] = "C"
dict_variable["D"] = "d"
dict_variable["e"] = "E"

print(dict_variable["a"]) # A
print(dict_variable["D"]) # d
print(dict_variable["b"]) # ? # 정답: 오류 발생(딕셔너리 안에 "b"라는 key가 없기 때문)


# 예제 3
dict_variable = {}
dict_variable["apple"] = 5000
dict_variable["banana"] = 3000
dict_variable["apple"] = 2000
dict_variable["banana"] = dict_variable["banana"] + 1000

print(dict_variable["apple"] + dict_variable["banana"]) # 6000


# 예제 4
dict_variable = {
    "이름": "정우영",
    "생년월일": "19000101",
    "회사": "하이퍼그로스"
}

for key in dict_variable:
    print(key, dict_variable[key])

"""
이름 정우영
생년월일 19000101
회사 하이퍼그로스
"""


# 예제 5
dict_variable = {
    "이름": "정우영",
    "생년월일": "19000101",
    "회사": "하이퍼그로스"
}

for key, value in dict_variable.items():
    print(key, value)

"""
이름 정우영
생년월일 19000101
회사 하이퍼그로스
"""


# 예제 6
dict_variable = {
    "이름": "정우영",
    "생년월일": "19000101",
    "회사": "하이퍼그로스"
}

print("나이" in dict_variable) # 오류 발생?
# 정답: False(딕셔너리 자료에 특정한 키가 있는지를 알기 위해서는 in 명령을 사용하는데 해당 키가 존재하면 True, 존재하지 않으면 False를 반환)


# 예제 7
dict_variable = {
    "이름": "정우영",
    "생년월일": "19000101",
    "회사": "하이퍼그로스"
}

if "거주지" not in dict_variable:
    dict_variable["거주지"] = "서울특별시"
    # 위 조건문의 조건식이 무엇을 의미하는지 작성하시오.
    # 딕셔너리에 "거주지"라는 키가 없으면 "거주지": "서울특별시"라는 키와 값을 각각 추가해라.

print(dict_variable)

"""
이름 정우영
생년월일 19000101
회사 하이퍼그로스
거주지 서울특별시
"""
"""
정답: {'key': 'value'} 딕셔너리 형태 그대로 출력됨
{'이름': '정우영', '생년월일': '19000101', '회사': '하이퍼그로스', '거주지': '서울특별시'}
"""


# 예제 8
list_variable = []

try:
    list_variable.append(0)
    list_variable.append(1)
    list_variable.append(2)
    print(list_variable[3])

except:
    print("에러가 발생했습니다.")
    print("에러의 원인이 무엇인가요?")

"""
에러가 발생했습니다.
에러의 원인이 무엇인가요?

# 에러 발생 원인: 없는 인덱스 값을 입력했기 때문에
"""


# 예제 9
try:
    number = 1
    if number == 1
        print(number)

except:
    print("에러가 발생했습니다.")
    print("에러의 원인은 무엇인가요?")

"""
에러 원인: if 조건문 끝에 :(colon)이 빠져 있어서
"""


# 예제 10
n = 10
total = 0

for number in range(0, n + 1):
    if number % 2 == 0:
        total += number * 2
    elif number % 2 == 1:
        total += number + 1 * 3

print(total) # 100