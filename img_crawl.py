import os.path
import requests
import re
import urllib.request
from bs4 import BeautifulSoup

#메인
# g = 0 : 남자/ 1 : 여자 
# t = str타입의 float수 
# w = str타입
def run_cloth(g, t, w): 
    t = float(t)
    cloth = []
    
    if g == 0: #남자
        if t < -15:
            if '맑' in w: cloth = [7, 8, 14, 16]
            elif '구' in w: cloth = [7, 8, 14, 16]
            elif '흐' in w: cloth = [7, 8, 14, 16]
            elif '비' in w: cloth = [0] #예외처리
            elif '소' in w: cloth = [0]
            elif '눈' in w: cloth #나가면 안되는 날씨.. (if not cloth:)
        elif -15 <= t and t < 4:
            if '맑' in w: cloth = [7, 8, 14, 16]
            elif '구' in w: cloth = [7, 8, 14, 16]
            elif '흐' in w: cloth = [7, 8, 14, 16]
            elif '비' in w: cloth = [7, 8, 14, 16]
            elif '소' in w: cloth = [7, 8, 14, 16]
            elif '눈' in w: cloth = [7, 8, 14, 16]
        elif 4 <= t and t < 9:
            if '맑' in w: cloth = [7, 14, 9, 15]
            elif '구' in w: cloth = [7, 11, 16]
            elif '흐' in w: cloth = [7, 11, 16]
            elif '비' in w: cloth = [7, 11, 16]
            elif '소' in w: cloth = [7, 11, 16]
            elif '눈' in w: cloth = [0]
        elif 9 <= t and t < 12:
            if '맑' in w: cloth = [6, 9, 14]
            elif '구' in w: cloth = [6, 9, 14, 15]
            elif '흐' in w: cloth = [6, 9, 14, 15]
            elif '비' in w: cloth = [6, 9, 14, 15]
            elif '소' in w: cloth = [6, 9, 14, 15]
            elif '눈' in w: cloth = [0]
        elif 12 <= t and t < 17:
            if '맑' in w: cloth = [7, 14, 10]
            elif '구' in w: cloth = [7, 15, 10]
            elif '흐' in w: cloth = [7, 15, 10]
            elif '비' in w: cloth = [7, 15, 8]
            elif '소' in w: cloth = [7, 15, 8]
            elif '눈' in w: cloth = [0]
        elif 17 <= t and t < 20:
            if '맑' in w: cloth = [7, 10]
            elif '구' in w: cloth = [5, 14, 9]
            elif '흐' in w: cloth = [5, 14, 9]
            elif '비' in w: cloth = [5, 14, 9]
            elif '소' in w: cloth = [5, 14, 9]
            elif '눈' in w: cloth = [0]
        elif 20 <= t and t < 23:
            if '맑' in w: cloth = [2, 10]
            elif '구' in w: cloth = [2, 10]
            elif '흐' in w: cloth = [2, 9]
            elif '비' in w: cloth = [2, 8]
            elif '소' in w: cloth = [2, 8]
            elif '눈' in w: cloth = [0]
        elif 23 <= t and t < 28:
            if '맑' in w: cloth = [2, 3]
            elif '구' in w: cloth = [2, 3]
            elif '흐' in w: cloth = [2, 3]
            elif '비' in w: cloth = [3, 5]
            elif '소' in w: cloth = [2, 3]
            elif '눈' in w: cloth = [0]
        elif 28 <= t and t < 35:
            if '맑' in w: cloth = [2, 3]
            elif '구' in w: cloth = [2, 3]
            elif '흐' in w: cloth = [2, 3]
            elif '비' in w: cloth = [2, 3]
            elif '소' in w: cloth = [2, 3]
            elif '눈' in w: cloth = [0]
        elif 35 <= t:
            if '맑' in w: cloth = [2, 3]
            elif '구' in w: cloth = [2, 3]
            elif '흐' in w: cloth = [2, 3]
            elif '비' in w: cloth = [2, 3]
            elif '소' in w: cloth = [2, 3]
            elif '눈' in w: cloth = [0]
    elif g == 1: #여자
        if t < -15:
            if '맑' in w: cloth = [7, 8, 14, 16]
            elif '구' in w: cloth = [7, 8, 14, 16]
            elif '흐' in w: cloth = [7, 8, 14, 16]
            elif '비' in w: cloth = [0] #예외처리
            elif '소' in w: cloth = [0]
            elif '눈' in w: cloth #나가면 안되는 날씨.. (if not cloth:)
        elif -15 <= t and t < 4:
            if '맑' in w: cloth = [7, 8, 14, 16]
            elif '구' in w: cloth = [7, 8, 14, 16]
            elif '흐' in w: cloth = [7, 8, 14, 16]
            elif '비' in w: cloth = [7, 8, 14, 16]
            elif '소' in w: cloth = [7, 8, 14, 16]
            elif '눈' in w: cloth = [7, 8, 14, 16]
        elif 4 <= t and t < 9:
            if '맑' in w: cloth = [7, 14, 9, 15]
            elif '구' in w: cloth = [7, 11, 16]
            elif '흐' in w: cloth = [7, 11, 16]
            elif '비' in w: cloth = [7, 11, 16]
            elif '소' in w: cloth = [7, 11, 16]
            elif '눈' in w: cloth = [0]
        elif 9 <= t and t < 12:
            if '맑' in w: cloth = [5, 14, 13]
            elif '구' in w: cloth = [5, 14, 13]
            elif '흐' in w: cloth = [5, 8, 15]
            elif '비' in w: cloth = [5, 8, 15]
            elif '소' in w: cloth = [5, 8, 15]
            elif '눈' in w: cloth = [0]
        elif 12 <= t and t < 17:
            if '맑' in w: cloth = [7, 9]
            elif '구' in w: cloth = [7, 8]
            elif '흐' in w: cloth = [7, 10]
            elif '비' in w: cloth = [5, 11]
            elif '소' in w: cloth = [5, 11]
            elif '눈' in w: cloth = [0]
        elif 17 <= t and t < 20:
            if '맑' in w: cloth = [6, 8]
            elif '구' in w: cloth = [6, 10]
            elif '흐' in w: cloth = [12, 14]
            elif '비' in w: cloth = [12, 14]
            elif '소' in w: cloth = [12, 14]
            elif '눈' in w: cloth = [0]
        elif 20 <= t and t < 23:
            if '맑' in w: cloth = [12]
            elif '구' in w: cloth = [12]
            elif '흐' in w: cloth = [12]
            elif '비' in w: cloth = [12]
            elif '소' in w: cloth = [12]
            elif '눈' in w: cloth = [0]
        elif 23 <= t and t < 28:
            if '맑' in w: cloth = [2, 3]
            elif '구' in w: cloth = [2, 3]
            elif '흐' in w: cloth = [2, 3]
            elif '비' in w: cloth = [2, 3]
            elif '소' in w: cloth = [2, 3]
            elif '눈' in w: cloth = [0]
        elif 28 <= t and t < 35:
            if '맑' in w: cloth = [1, 4]
            elif '구' in w: cloth = [2, 3]
            elif '흐' in w: cloth = [2, 3]
            elif '비' in w: cloth = [2, 3]
            elif '소' in w: cloth = [2, 3]
            elif '눈' in w: cloth = [0]
        elif 35 <= t:
            if '맑' in w: cloth = [1, 4]
            elif '구' in w: cloth = [1, 3]
            elif '흐' in w: cloth = [1, 3]
            elif '비' in w: cloth = [1, 3]
            elif '소' in w: cloth = [1, 3]
            elif '눈' in w: cloth = [0]
    return cloth