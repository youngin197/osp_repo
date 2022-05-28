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

def get_data(gender: str, fashion: tuple) -> dict:
    # 성별, 아이디, 상하의 정보를 받아서 url을 반환하는 함수
    
    es_host = "http://localhost:9200"
    es = Elasticsearch(es_host)

    index_name_top = gender + '_' + 'top'       # 성별_상의
    index_name_bottom = gender + '_' + 'bottom'     # 성별_하의

    query_top = {"query":{"match":{"id":f"{fashion[0]}"}}}      # 상의 쿼리문
    query_bottom = {"query":{"match":{"id":f"{fashion[1]}"}}}       # 하의 쿼리문

    top_data = es.search(index=index_name_top, body=query_top, pretty=True )     # 데이터 가져옴
    bottom_data = es.search(index=index_name_bottom, body=query_bottom, pretty=True)
    
    top_data = top_data['hits']['hits']     # 데이터 변환
    bottom_data = bottom_data['hits']['hits']

    data = {}

    for source in top_data:     # id, 이름, 주소를 data 딕셔너리에 저장함
        data['top'] = source['_source']
    for source in bottom_data:
        data['bottom'] = source['_source']

    
    return data
  


if __name__ == "__main__":
    get_data('woman', (1, 8))
