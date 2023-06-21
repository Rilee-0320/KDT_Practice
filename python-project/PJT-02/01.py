from dotenv import load_dotenv
load_dotenv()
import os
import requests


def popular_count():
    pass
    # 여기에 코드를 작성합니다.
    API_Key = os.getenv('API_Key')
    URL = f'https://api.themoviedb.org/3/movie/popular?api_key={API_Key}&language=ko-KR&region=KR'
    
    response = requests.get(URL).json()
    data = response['results']
    cnt = len(data)

    return cnt

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
