import json
from pprint import pprint


def movie_info(movie, genres):
    new_genre_dict = {}
    for i in genres:
        new_genre_dict[i.get('id')] = i.get('name')
    
    result = {
        'genre_ids' : movie.get('genre_ids'),
        'id' : movie.get('id'),
        'overview' : movie.get('overview'),
        'poster_path' : movie.get('poster_path'),
        'title' : movie.get('title'),
        'vote_average' : movie.get('vote_average')
    }
    tmp_list = []
    for i in movie.get('genre_ids'):
        tmp_list.append(new_genre_dict[i])
    
    del result['genre_ids']
    result['genre_names'] = tmp_list
    
    return result

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))






