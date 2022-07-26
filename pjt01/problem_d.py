import json


def max_revenue(movies):
    
    movies_ids = []
    for i in movies:
        movies_ids.append(i['id'])
    
    revenue_title_list = []
    
    for i in movies_ids:
        movies_open = open(f'data/movies/{i}.json', encoding='utf-8')
        movies_detail = json.load(movies_open)
        revenue_title_list.append((movies_detail.get('revenue'),movies_detail.get('title')))
        
    revenue_title_list = sorted(revenue_title_list, key = lambda x : x[0], reverse = True)
    
    result = revenue_title_list[0][1]
    
    return result
    
    
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))

    
# 1. movies 폴더 반복문으로 오픈
# 2, 수익이 가장 높은 영화 제목 출력 함수 max_revenue 
