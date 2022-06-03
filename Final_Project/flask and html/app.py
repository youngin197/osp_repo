#!/usr/bin/python3
# -*- coding: utf-8 -*-

####### 오픈소스 프로그래밍 팀프로젝트 ########

import sys
import flask
import requests.exceptions
import requests as rq
# import database.py
# import weather_crawl.pyimage.png
# import img_crawl.py
from elasticsearch import Elasticsearch
from flask import Flask, render_template, request
from flask import redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
	return redirect(url_for('main'))

@app.route('/main')
def main():
	return render_template('main.html')

@app.route('/result', methods=['GET'])
def get_user_info() :
	error = None
	if request.method == "GET":
		# html 에서 사용자 정보 입력 받고, 변수로 가져오기
		gender = request.form['gender']
		location = request.form['location']
		print(location, gender)
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
