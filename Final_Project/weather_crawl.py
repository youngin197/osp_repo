from bs4 import BeautifulSoup
from pprint import pprint
import requests
import re
from datetime import datetime

now = datetime.now()

html = requests.get('https://search.naver.com/search.naver?query=날씨')
soup = BeautifulSoup(html.text, 'html.parser')
temp = soup.find('div', {'class': 'temperature_text'}).text
today_temp = temp[6:].rstrip().rstrip()

find_address = soup.find('div', {'class':'title_area _area_panel'}).text
lent = len(find_address)//2
print("현재 시간 : ", now.strftime('%Y년 %m월%d일 %H시 %M분')) 
print('현재 온도 : '+today_temp+'℃')
print('현재 위치 : '+find_address[1:lent])

