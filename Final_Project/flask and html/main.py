#!/usr/bin/python3
#-*- coding: utf-8 -*-

####### 오픈소스 프로그래밍 기말 과제 ########

import sys
import flask
import requests.exceptions
import requests as rq
import database.py
import weather_crawl.py
import img_crawl.py
from elasticsearch import Elasticsearch
from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def home() :
	#get html file
	return render_template('main.html')
	
@app.route('/keywords', methods = ['POST'])
def crawling_result() :
	if request.method == 'GET' :
		# html 에서 사용자 정보 입력 받고, 변수로 가져오기
		location = request.form['location']
		gender = request.form['gender']
		
		# 날씨 크롤링 파일 실행 시키기 -> 날씨, 온도 정보를 리턴 받기
		weather, temperature = weather_crawl(location, gender)

		# 이미지 크롤링 파일 실행 시키기 -> 이건 어디서 실행시키든 상관 없음
		
		
		# 날씨, 온도 정보를 가지고 database.py 파일 실행 시키기
		# 여기서 파라미터는 날씨(한글), 기온(정수형), 성별(man, woman)
		
		
		# 마지막으로 사용자에게 result.html 보여주기
		

		
	return render_template('crawling_page.html', presi_names = result)
			
if __name__ == '__main__':
	app.run(debug=True)
	
