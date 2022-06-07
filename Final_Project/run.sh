#!/bin/bash

##### 8조 기말 프로젝트 실행 쉘 파일 #####

# 1)라이브러리 설치
=======
# 플라스크, 엘라스틱서치, 뷰티풀수프, 리퀘스츠
>>>>>>> from scratch
#sudo apt-get install python-pip
sudo apt update
sudo apt install elasticsearch
pip install flask
pip install beautifulsoup4
pip install requests

# 1)엘라스틱 서치 실행
./elasticsearch-8.2.2/bin/elasticsearch -d

# 2) 데이터 생성
./insert_data.py

# 3)플라스크 실행
flask run

>>>>>>> from scratch
