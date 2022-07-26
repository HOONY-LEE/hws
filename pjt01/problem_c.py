import json
from pprint import pprint


def movie_info(movies, genres):
    new_genre_dict = {}
    for i in genres:
        new_genre_dict[i.get('id')] = i.get('name')
        
    def move_info2(movie):
       

        result = {
            'genre_ids' : movie.get('genre_ids'),   # 뒤에 삭제되어 출력안되는 코드
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
    
    
    result_list = []
    
    for i in movies_list:
        result_list.append(move_info2(i))
        
    
    
    
    
    
    return result_list    #
    



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))

print(movies_list)
