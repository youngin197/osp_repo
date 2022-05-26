#!/bin/usr/python
from elasticsearch import Elasticsearch as es

"""
0 : 예외, 1 : 반팔 티셔츠, 2 : 긴팔 티셔츠, 3 : 맨투맨, 4 : 셔츠, 5 : 블라우스, 6 : 니트, 7 : 민소매 티셔츠, 8 : 청바지, 9 : 슬랙스, 10 : 면바지
맑음(맑), 구름(구), 흐림(흐), 비(비), 소나기(소), 눈(눈)
"""

def temperature_index_creator(t: int) -> int:
    # 기온을 바탕으로 기온의 인덱스를 반환하는 함수
    if t <= -50: return 999
    elif t <= -16: return 0
    elif t <= 4: return 1
    elif t <= 8: return 2
    elif t <= 11: return 3
    elif t <= 16: return 4
    elif t <= 19: return 5
    elif t <= 22: return 6
    elif t <= 27: return 7
    elif t <= 35: return 8
    elif t <= 60: return 9
    else: return 999


def weather_index_creator(w: str) -> int:
    # 날씨를 바탕으로 날씨의 인덱스를 반환하는 함수
    # 999를 반환하면 해당 날씨는 취급하지 않는다는 뜻임
    w = w[0]
    if w == '맑': return 0
    elif w == '구': return 1
    elif w == '흐': return 2
    elif w == '비': return 3
    elif w == '소': return 4
    elif w == '눈': return 5
    else: return 999


def set_table() -> dict:
    # 테이블을 만드는 함수
    d = {}
    for w in range(6):      # 날씨
        for t in range(10):     # 온도
            d[(w, t)] = (0, 0)

    d[(0, 8)] = (1, 4)
    d[(1, 8)] = d[(2, 8)] = d[(3, 8)] = (1, 13)
    
    return d


temperature = int(input())      # 기온을 입력 받음, 수정
temperature_index = temperature_index_creator(temperature)     # 기온을 바탕으로 기온의 인덱스를 받아옴

if temperature_index == 999:
    # 수정
    print("해당 온도는 취급하지 않습니다.")

weather = input()       # 날씨를 입력 받음, 수정
weather_index = weather_index_creator(weather)        # 날씨를 바탕으로 날씨의 인덱스를 받아옴

if weather_index == 999:
    # 수정
    print("해당 날씨는 취급하지 않습니다.")


table = set_table()

key = table[(weather_index, temperature_index)]

print(key)
