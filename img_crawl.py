import os.path
import requests
import re
import urllib.request
from bs4 import BeautifulSoup

#<<수정필요>>
#이미지 블로그 함수
def input_url():
    base_url = 'https://blog.naver.com/PostView.naver?blogId=ksunbum97'  #크롤링을 위한 베이스 주소
    #input_url = input('블로그/게시글(이미지) 주소를 입력\n')
    #number = input_url.split('/')[4]    #게시글번호 추출 - 조건문
    gender = int(input('남성은 0 여성은 1을 눌러주세요 : '))
    cloth = input('찾으려는 옷을 입력하시오 : ')
    if gender == 0:
        if cloth in '민소매':   #인덱스 순서대로 정렬됨
            number = '222748645556'
        elif cloth in '반팔':
            number = '222748646638'
        elif cloth in '반바지':
            number = '222748647042'
        elif cloth in '긴팔티':
            number = '222748696770'
        elif cloth in '니트':
            number = '222748697185'
        elif cloth in '셔츠':
            number = '222748697498'
        elif cloth in '청바지':
            number = '222748697823'
        elif cloth in '면바지':
            number = '222748647898'
        elif cloth in '슬랙스':
            number = '222748648184'
        elif cloth in '트레이닝팬츠':
            number = '222748648614'
        elif cloth in '자켓':
            number = '222748649266'
        elif cloth in '코트':
            number = '222748649540'
        elif cloth in '패딩':
            number = '222748649972'
        elif cloth in '긴팔티':
            number = '222748696770'
        elif cloth in '니트':
            number = '222748697185'
        elif cloth in '셔츠':
            number = '222748697498'
        elif cloth in '청바지':
            number = '222748697823'
    else:
        if cloth in '민소매':
            number = '222748650608'
        elif cloth in '반팔':
            number = '222748651027'
        elif cloth in '반바지':
            number = '222748651501'
        elif cloth in '미니스커트':
            number = '222748652086'
        elif cloth in '긴팔티':
            number = '222748692353'
        elif cloth in '니트':
            number = '222748693286'
        elif cloth in '셔츠':
            number = '222748693771'
        elif cloth in '청바지':
            number = '222748694173'
        elif cloth in '레깅스':
            number = '222748652595'
        elif cloth in '면바지':
            number = '222748653101'
        elif cloth in '슬랙스':
            number = '222748653501'
        elif cloth in '트레이닝팬츠':
            number = '222748653930'
        elif cloth in '롱스커트':
            number = '222748655592'
        elif cloth in '자켓':
            number = '222748655860'
        elif cloth in '코트':
            number = '222748656214'
        elif cloth in '패딩':
            number = '222748656481'
    url = base_url+'&logNo='+number
    return url

#<<수정필요>>
#이미지 저장 위치 입력 / elasticsearch 사용해야되는 부분
def input_save_dest():
    save_dest = 'C:/Users/ksunb/Desktop/ootd(outfit of the day)/images' #파이썬에서는 디렉토리 구분을 '/'로 인식함
    return save_dest

#블로그 방문 함수
def visit_blog(url):
    html = requests.get(url).text
    return html

#게시글 이름으로 폴더 생성 함수
def get_title(html):
    soup = BeautifulSoup(html, 'html.parser')
    contents = str(soup.select('.se-fs-'))  #제목 추출을 위한 셀렉터
    hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')  #한글만 따오기 위해
    result = hangul.sub('', contents)   
    title = result.strip().split('  ')  #공백으로 구분  
    return title[0] #0번째 인덱스가 제목

#블로그 이미지 추출 함수
def get_img_list(html):
    soup = BeautifulSoup(html, 'html.parser')
    imgs = soup.select('.se-image-resource')
    img_list = list()
    for img in imgs:
        img_list.append(img['data-lazy-src'])   #이미지 경로
    return img_list

#(로컬)저장경로 생성 함수
def mkdir(temp_save_dest, title):
    if os.path.isdir(temp_save_dest+'/'+title):
        pass
    else:
        os.makedirs(temp_save_dest+'/'+title)
    return temp_save_dest+'/'+title

#이미지 저장 함수
def save_img(img_list, save_dest):
    for i in range(0, len(img_list), 1):
        ext_idx = (img_list[i].find('?type'))   #확장자 찾기 위해 type 문자열을 먼저 찾고
        ext = (img_list[i][ext_idx-3:ext_idx])  #위에서 찾은 인덱스에서 -3하여 해당 파일의 확장자 확인
        urllib.request.urlretrieve(img_list[i], save_dest+'/'+str(i+1)+'.'+ext)
    return len(img_list)

#메인
if __name__  == '__main__':
    url = input_url()
    temp_save_dest = input_save_dest()
    html = visit_blog(url)
    title = get_title(html)
    img_list = get_img_list(html)
    save_dest = mkdir(temp_save_dest, title)
    img_cnt = save_img(img_list, save_dest)
    print ('{} 제목의 블로그에서 {}개의 이미지를 저장했습니다.'.format(title, img_cnt))
