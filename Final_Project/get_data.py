#/usr/bin/python

"""
0 : 예외

남자
1 : 반팔 티셔츠, 2 : 긴팔 티셔츠, 3 : 코트, 4 : 셔츠, 5 : 블라우스(자켓), 6 : 니트(스웨터), 7 : 민소매 티셔츠(탱크톱), 8 : 패딩
1 : 청바지, 2 : 트레이닝 바지, 3 : 슬랙스, 4 : 면바지, 5 : 반바지

여자
1 : 반팔 티셔츠, 2 : 긴팔 티셔츠, 3 : 코트, 4 : 셔츠, 5 : 블라우스(자켓), 6 : 니트(스웨터), 7 : 민소매 티셔츠(탱크톱), 8 : 패딩
1 : 청바지, 2 : 트레이닝 바지, 3 : 슬랙스, 4 : 면바지, 5 : 반바지, 6 : 롱스커트, 7 : 레깅스, 8 : 미니스커트

맑음(맑), 구름(구), 흐림(흐), 비(비), 소나기(소), 눈(눈)
"""

import sys, json
from elasticsearch import Elasticsearch

def get_data(gender: int, fashion: list) -> dict:
    # 성별, 아이디, 상하의 정보를 받아서 url을 반환하는 함수
    
    es_host = "http://localhost:9200"
    es = Elasticsearch(es_host)

    if type(gender) == int:
        if gender == 0:
            gender = 'man'
        elif gender == 1:
            gender = 'woman'

    index_name_top = gender + '_' + 'top'       # 성별_상의
    index_name_bottom = gender + '_' + 'bottom'     # 성별_하의

    fashion_top = fashion[0]        # 하의 정보
    fashion_bottom = fashion[1]     # 상의 정보

    top_data = []
    bottom_data = []

    for f in fashion_top:
        query_top = {"query":{"match":{"id":f"{f}"}}}      # 상의 쿼리문
        top_data.append(es.search(index=index_name_top, body=query_top, pretty=True ))     # 데이터 가져옴

    for f in fashion_bottom:
        query_bottom = {"query":{"match":{"id":f"{f}"}}}       # 하의 쿼리문
        bottom_data.append(es.search(index=index_name_bottom, body=query_bottom, pretty=True))        # 데이터 가져옴

    # print(top_data)
    
    top_data = list(map(lambda x : x['hits']['hits'], top_data))     # 데이터 변환
    bottom_data = list(map(lambda x : x['hits']['hits'], bottom_data))

    # print(top_data[1])

    data = {'top' : [], 'bottom' : []}

    for a in top_data:     # id, 이름, 주소를 data 딕셔너리에 저장함
        for source in a:
            data['top'].append(source['_source'])
    for a in bottom_data:
        for source in a:
            data['bottom'].append(source['_source'])

    
    return data
  

if __name__ == "__main__":
    data = get_data('woman', [[1, 2], [8]])
    print(data['top'])
