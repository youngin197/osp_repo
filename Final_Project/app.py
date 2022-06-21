#!/usr/bin/python3
# -*- coding: utf-8 -*-

####### 오픈소스 프로그래밍 팀프로젝트 ########

import sys
import flask
import requests.exceptions
import requests as rq
import database
import weather_crawl
# import img_crawl

#from elasticsearch import Elasticsearch
from flask import Flask, render_template, request
from flask import redirect, url_for

app = Flask(__name__)

def get_index(gender : str, location : int) -> tuple:
    gend = 0
    index = 11

    if gender == 'male':
        gend = 0
    else: 
        gend = 1

    if 'seoul' in location:
        index = 0
    elif 'kyunggi' in location:
        index = 1
    elif 'kang' in location:
        index = 2
    elif 'chungnam' in location:
        index = 3 
    elif 'chungbuk' in location:
        index = 4
    elif 'jeonnam' in location:
        index = 5
    elif 'jeonbuk' in location:
        index = 6
    elif 'kyungnam' in location:
        index = 7
    elif 'kyungbuk' in location:
        index = 8
    elif 'inchun' in location:
        index = 9
    elif 'daejeon' in location:
        index = 10
    elif 'dague' in location:
        index = 11
    elif 'gwangju' in location:
        index = 12
    elif 'ulsan' in location:
        index = 13
    elif 'busan' in location:
        index = 14
    elif 'sejong' in location:
        index = 15
    elif 'jeju' in location:
        index = 16


    return gend, index

@app.route('/')
def index():
   return redirect(url_for('main'))

@app.route('/main')
def main():
   return render_template('main.html')

@app.route('/result', methods=['GET', 'POST'])
def get_user_info():
    error = None
    if request.method == "POST":
      # html 에서 사용자 정보 입력 받고, 변수로 가져오기
        gender = request.form['gender']
        location = request.form['location']

        gend, index = get_index(gender, location)

        if index == 11:     # 현위치, 대구
            location = 'dague'

        temp, weather = weather_crawl.run_weather(index)

        url = database.database(gender=gend, temperature=float(temp), weather=weather)
        
        # print(url)
        return render_template('result.html', temp = temp, weather = weather, loc = location, url = url)

      #return render_template('result.html')

#       # 날씨 크롤링 파일 실행 시키기 -> 날씨, 온도 정보를 리턴 받기
#       weather, temperature = weather_crawl(location, gender)

#       # 이미지 크롤링 파일 실행 시키기 -> 이건 어디서 실행시키든 상관 없음
      
      
#       # 날씨, 온도 정보를 가지고 database.py 파일 실행 시키기
#       # 여기서 파라미터는 날씨(한글), 기온(정수형), 성별(man, woman)
      
      
#       # 마지막으로 사용자에게 result.html 보여주기
      
#    #return render_template('crawling_page.html', presi_names = result)
if __name__ == '__main__':
    app.run(debug=True)
