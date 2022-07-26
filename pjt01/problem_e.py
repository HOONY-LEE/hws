import json


def dec_movies(movies):
   

    result = []
    movies_ids = []
    for i in movies:
        movies_ids.append(i['id'])
    
    date_title_list = []
    
    for i in movies_ids:
        movies_open = open(f'data/movies/{i}.json', encoding='utf-8')
        movies_detail = json.load(movies_open)
        date_title_list.append((movies_detail.get('release_date')[5:7],movies_detail.get('title')))
            
    for i in date_title_list:
        if i[0] == '12':
            result.append(i[1])
    
    return result
    
    print(result)

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))
