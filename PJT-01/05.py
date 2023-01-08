import json

# 아래 코드 수정 금지
movie_json = open("data/movie.json", encoding="UTF8")
movie = json.load(movie_json)

# 이하 문제 해결을 위한 코드 작성
info = 'id', 'title', 'vote_average', 'overview', 'genre_ids'
new_dict = {}
for key, value in movie.items():

    if key in info:
        new_dict[key] = value
print(new_dict)

# 모범 답안
# new_movie = {
#     'id': movie['id'],
#     'title': movie['title'],
#     'vote_average': movie['vote_average'],
#     'overview': movie['overview'],
#     'genre_ids': movie['genre_ids'],
# }
# print(new_movie)