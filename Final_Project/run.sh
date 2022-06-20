#!/bin/bash

##### 8조 기말 프로젝트 실행 쉘 파일 #####

# 1)라이브러리 설치
# 플라스크, 엘라스틱서치, 뷰티풀수프, 리퀘스츠
pip --version
sudo apt-get install python3-pip
sudo apt update
pip install elasticsearch
pip install flask
pip install beautifulsoup4
pip install requests

# 2) 의상 데이터 생성
./insert_data.py
#./app.py

# 3)플라스크 실행
flask run