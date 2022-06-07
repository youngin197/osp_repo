#!/usr/bin/python
import get_data
import insert_data

"""
0 : 예외

남자
1 : 반팔 티셔츠, 2 : 긴팔 티셔츠, 3 : 코트, 4 : 셔츠, 5 : 블라우스(자켓), 6 : 니트(스웨터), 7 : 민소매 티셔츠(탱크톱), 8 : 패딩
1 : 청바지, 2 : 트레이닝 바지, 3 : 슬랙스, 4 : 면바지, 5 : 반바지

여자
1 : 반팔 티셔츠, 2 : 긴팔 티셔츠, 3 : 코트, 4 : 셔츠, 5 : 블라우스(자켓), 6 : 니트(스웨터), 7 : 민소매 티셔츠(탱크톱), 8 : 패딩
1 : 청바지, 2 : 트레이닝 바지, 3 : 슬랙스, 4 : 면바지, 5 : 반바지, 6 : 롱스커트, 7 : 레깅스, 8 : 미니스커트

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


def set_table(gender : int) -> dict:
    # 테이블을 만드는 함수
    if gender == 0:
        # 성별이 남자라면
        man = {}


        for t in range(10):      # 날씨
            for w in range(6):     # 온도
                man[(t, w)] = [(0), (0)]


        man[(0, 0)] = man[(0, 1)] = man[(0, 2)] = [[6, 8], [1, 4]]
        man[(0, 3)] = man[(0, 4)] = man[(0, 5)] = [[0], [0]]

        man[(1, 0)] = man[(1, 1)] = man[(1, 2)] = man[(1, 3)] = man[(1, 4)] = man[(1, 5)] = [[6, 5, 8], [1, 4]]

        man[(2, 0)] = [[6, 5, 3], [3, 4]]
        man[(2, 1)] = man[(2, 2)] = man[(2, 3)] = man[(2, 4)] = [[6, 8], [2]]
        man[(2, 5)] = [[0], [0]]

        man[(3, 0)] = [[4, 5], [1, 4]]
        man[(3, 1)] = man[(3, 2)] = man[(3, 3)] = man[(3, 4)] = [[4, 5, 3], [4]]
        man[(3, 5)] = [[0], [0]]

        man[(4, 0)] = [[6, 5], [3]]
        man[(4, 1)] = man[(4, 2)] = [[6, 3, 7], [3]]
        man[(4, 3)] = man[(4, 4)] = [[6, 3, 7], [1]]
        man[(4, 5)] = [[0], [0]]

        man[(5, 0)] = [[6, 7], [3]]
        man[(5, 1)] = man[(5, 2)] = man[(5, 3)] = man[(5, 4)] = [[2, 5, 7], [4]]
        man[(5, 5)] = [[0], [0]]

        man[(6, 0)] = man[(6, 1)] = [[1, 2], [2, 3]]
        man[(6, 2)] = [[1, 2], [4]]
        man[(6, 3)] = man[(6, 4)] = [[1, 2], [1]]
        man[(6, 4)] = [[0], [0]]

        man[(7, 0)] = man[(7, 1)] = man[(7, 2)] = man[(7, 4)] = [[1], [5]]
        man[(7, 3)] = [[2], [5]]
        man[(7, 5)] = [[0], [0]]

        man[(8, 0)]  = man[(8, 1)]  = man[(8, 2)]  = man[(8, 3)]  = man[(8, 4)] = [[1], [5]]
        man[(8, 5)] = [[0], [0]]

        man[(9, 0)] = man[(9, 1)] = man[(9, 2)] = man[(9, 3)] = man[(9, 4)] = [[1], [5]]
        man[(9, 5)] = [[0], [0]]


        return man

    if gender == 1:
        # 성별이 여자라면
        woman = {}

        for t in range(10):      # 날씨
            for w in range(6):     # 온도
                woman[(t, w)] = [(0), (0)]


        woman[(0, 0)] = woman[(0, 1)] = woman[(0, 2)] = [(6, 5, 8), (1)]
        woman[(0, 3)] = woman[(0, 4)] = woman[(0, 5)] = [(0), (0)]

        woman[(1, 0)] = woman[(1, 1)] = woman[(1, 2)] = woman[(1, 3)] = woman[(1, 4)] =  woman[(1, 5)] = [(6, 5, 8), (1)]

        woman[(2, 0)] = [(6, 5, 3), (4)]
        woman[(2, 1)] = woman[(2, 2)] = woman[(2, 3)] = woman[(2, 4)] = [(6, 8), (2)]
        woman[(2, 5)] = [(0), (0)]

        woman[(3, 0)] = woman[(3, 1)] = [(2, 5), (6)]
        woman[(3, 2)] = woman[(3, 3)] = woman[(3, 4)] = [(2, 3), (1)]
        woman[(3, 5)] = [(0), (0)]

        woman[(4, 0)] = [(6), (4)]
        woman[(4, 1)] = [(6), (1)]
        woman[(4, 2)] = [(6), (3)]
        woman[(4, 3)] = woman[(4, 4)] = [(2), (2)]
        woman[(4, 5)] = [(0), (0)]

        woman[(5, 0)] = [(4), (1)]
        woman[(5, 1)] = [(4), (3)]
        woman[(5, 2)] = woman[(5, 3)] = woman[(5, 4)] = [(5), (6)]
        woman[(5, 5)] = [(0), (0)]

        woman[(6, 0)] = woman[(6, 1)] = woman[(6, 2)] = woman[(6, 3)] = woman[(6, 4)] = [(2, 4), (2, 6)]
        woman[(6, 5)] = [(0), (0)]

        woman[(7, 0)] = woman[(7, 1)] = woman[(7, 2)] = woman[(7, 3)] = woman[(7, 4)] = [(1), (5, 8)]
        woman[(7, 5)] = [(0), (0)]

        woman[(8, 0)] = [(7), (8, 7)]
        woman[(8, 1)] = woman[(8, 2)] = woman[(8, 3)] = woman[(8, 4)] = [(1), (5)]
        woman[(8, 5)] = [(0), (0)]

        woman[(9, 0)] = [(1, 7), (5, 7, 8)]
        woman[(9, 1)] = woman[(9, 2)] = woman[(9, 3)] = woman[(9, 4)] = [(7), (5, 7, 8)]
        woman[(9, 5)] = [(0), (0)]
        

        return woman


def get_fashion_info(table : dict, t : int, w : int) -> tuple:
    # 테이블에서 패션 정보를 반환
    return table[(t, w)]


def database(gender : int, temperature : int, weather : str) -> None:
    # if cloth[0] == 0 or len(cloth) == 0:
    #     # 예외 상황
    #     return False

    temperature_index = temperature_index_creator(temperature)     # 기온을 바탕으로 기온의 인덱스를 받아옴

    if temperature_index == 999:
        # 수정
        print("해당 온도는 취급하지 않습니다.")
        return

    weather_index = weather_index_creator(weather)        # 날씨를 바탕으로 날씨의 인덱스를 받아옴

    if weather_index == 999:
        # 수정
        print("해당 날씨는 취급하지 않습니다.")
        return

    # data = get_data.get_data(gender, cloth)        # 데이터를 받아옴

    table = set_table(gender)       # 테이블을 가져옴

    fashion = get_fashion_info(table, temperature_index, weather_index)        # 테이블에서 데이터를 가져옴

    print(fashion)   
    

if __name__ == "__main__":
    database(0, -24, '맑음')
