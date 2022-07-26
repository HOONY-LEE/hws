# open 및 json 모듈 사용예시

import json


movie = open('sample.json', encoding='utf-8')
movie_detail = json.load(movie)

print(movie_detail)


def make_dict(data):
    new_data = {
        '원제': data.get('original_title'),
        '개봉년도': data.get('release_date')[:4],
        '평점': data.get('vote_average')
    }
    return new_data

print(make_dict(movie_detail))