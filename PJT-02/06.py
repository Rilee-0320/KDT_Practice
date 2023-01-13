from dotenv import load_dotenv
load_dotenv()
import os
import requests
from pprint import pprint


def credits(title):
    pass
    # 여기에 코드를 작성합니다.
    API_Key = os.getenv('API_Key')
    title = input()
    URL1 = f'https://api.themoviedb.org/3/search/movie/?api_key={API_Key}&language=ko-KR&region=KR&query={title}'

    try:
        response = requests.get(URL1).json()
        data = response['results']
        movie_id = data[0]['id']

        URL2 = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={API_Key}&language=ko-KR'

        response2 = requests.get(URL2).json()
        cast = response2['cast']
        crew = response2['crew']
        cast_list = []
        crew_list = []
        for one_cast in cast:
            if one_cast['cast_id'] < 10:
                cast_list.append(one_cast['name'])
        for one_crew in crew:
            if one_crew['department'] == 'Directing':
                crew_list.append(one_crew['name'])
        credits = {
            'cast' : cast_list,
            'crew' : crew_list
        }
        return credits
    
    except:
        return None
    
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록 반환
    영화 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
