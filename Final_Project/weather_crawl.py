from bs4 import BeautifulSoup
from pprint import pprint
import requests
import re
from datetime import datetime

def run_weather(ind=11): 
    region_info = {0 : '서울+',
    1 : '경기도+',
    2 : '강원도+',
    3 : '충청남도+',
    4 : '충청북도+',
    5 : '전라남도+',
    6 : '전라북도+',
    7 : '경상남도+',
    8 : '경상북도+',
    9 : '인천+',
    10 : '대전+',
    11 : '대구+',
    12 : '광주+',
    13 : '울산+',
    14 : '부산+',
    15 : '세종+',
    16 : '제주+'}
    p = ''
    
    if ind == 0:
        p = region_info[ind]
    elif ind == 1:
        p = region_info[ind]
    elif ind == 2:
        p = region_info[ind]
    elif ind == 3:
        p = region_info[ind]
    elif ind == 4:
        p = region_info[ind]
    elif ind == 5:
        p = region_info[ind]
    elif ind == 6:
        p = region_info[ind]
    elif ind == 7:
        p = region_info[ind]
    elif ind == 8:
        p = region_info[ind]
    elif ind == 9:
        p = region_info[ind]
    elif ind == 10:
        p = region_info[ind]
    elif ind == 11:
        p = region_info[ind]
    elif ind == 12:
        p = region_info[ind]
    elif ind == 13:
        p = region_info[ind]
    elif ind == 14:
        p = region_info[ind]
    elif ind == 15:
        p = region_info[ind]
    elif ind == 16:
        p = region_info[ind]
    
    
    now = datetime.now()

    html = requests.get('https://search.naver.com/search.naver?query='+p+'날씨')
    soup = BeautifulSoup(html.text, 'html.parser')
    temp = soup.find('div', {'class': 'temperature_text'}).text
    today_temp = temp[6:-2] #현재 온도

    find_address = soup.find('div', {'class':'title_area _area_panel'}).text #현재 탐색 지역
    lent = len(find_address)//2 
    if ind == -1: #그냥 현재 위치 기준 날씨
        p = find_address[1:lent+1]

    weather = soup.find('div', {'class': 'weather_info'})
    today_weather = weather.find('span', {'class' : 'weather before_slash'}).text  #현재 지역의 날씨
    print("현재 시간 : ", now.strftime('%Y년 %m월%d일 %H시 %M분')) 
    print('현재 온도 :  '+ today_temp+'℃')
    print('현재 날씨 : ', today_weather)
    print('현재 위치 :  '+ p[:-1])
    
    reslist = []
    reslist.append(str(today_temp))
    reslist.append(str(today_weather))
    return reslist #해당 구역 온도(0),날씨(1)
