#!/usr/bin/python3

# DataBase를 구축하는 코드

# 0 : 예외
# 남자
# 1 : 반팔 티셔츠, 2 : 긴팔 티셔츠, 3 : 코트, 4 : 셔츠, 5 : 블라우스(자켓), 6 : 니트(스웨터), 7 : 민소매 티셔츠(탱크톱), 8 : 패딩
# 1 : 청바지, 2 : 트레이닝 바지, 3 : 슬랙스, 4 : 면바지, 5 : 반바지
# t1_m : 남자 상의 반팔 티셔츠
# b1_m : 남자 하의 청바지
# 여자
# 1 : 반팔 티셔츠, 2 : 긴팔 티셔츠, 3 : 코트, 4 : 셔츠, 5 : 블라우스(자켓), 6 : 니트(스웨터), 7 : 민소매 티셔츠(탱크톱), 8 : 패딩
# 1 : 청바지, 2 : 트레이닝 바지, 3 : 슬랙스, 4 : 면바지, 5 : 반바지, 6 : 롱스커트, 7 : 레깅스, 8 : 미니스커트
# t1_wm : 여자 상의 반팔 티셔츠

import sys, json, time
from elasticsearch import Elasticsearch

def insert_data():
    # DataBase에 데이터를 넣음
    es_host = "http://localhost:9200"
    es = Elasticsearch(es_host)
    index_name = tuple(['man_top', 'man_bottom', 'woman_top', 'woman_bottom'])      # 인덱스의 이름

    es.indices.delete(index=index_name, ignore = [400, 404])        # 혹시 파일이 중복되서 들어갈 수 있으므로

    with open('./data.json') as f:
        # 경로 수정 필요함
        data = json.load(f)

    for name in index_name:
        # index_name별로 데이터를 가져옴
        for index, document in enumerate(data[name], 1):
            es.index(index= name, id= index, document= document) 

    time.sleep(1)
            

if __name__ == "__main__":
    insert_data()


# **************************************************************************************************
# *************************** 아래는 딕셔너리 형태의 데이터임 ****************************************
# **************** 모든 딕셔너리 데이터는 json 형태로 저장해놓았으므로 필요시에 참조 ******************
# **************************************************************************************************


# t1_wm = {
#     "name": "short t shirt",
#     "url_1": "https://postfiles.pstatic.net/MjAyMjA1MjdfOSAg/MDAxNjUzNjE1Mzk2MDg3.hc6Lo1QLDSxLLAjtZYAXOLcBVbsO2dJQsJcGDRPPnwgg.I1v26eZXUSg0pUCTVNdLAdsHNAtoGPcTm9ExJz1DmHcg.JPEG.ksunbum97/%EC%97%AC%EC%9E%90_%EB%B0%98%ED%8C%94_1.jpg?type=w966",
#     "url_2": "https://postfiles.pstatic.net/MjAyMjA1MjdfMjcg/MDAxNjUzNjE1Mzk2MTA1.T79Zl0QDA9dSTeZwME2kBLKuYdIAP4iiTwHW33FqaVwg.hgcx7GiPm_vDKfYB7bnnxsHTX_lRhb7bo8Kp6yyKWDsg.JPEG.ksunbum97/%EC%97%AC%EC%9E%90_%EB%B0%98%ED%8C%94_2.jpg?type=w966",
#     "url_3": "https://postfiles.pstatic.net/MjAyMjA1MjdfMTI4/MDAxNjUzNjE1Mzk2MDk2.EQZrFcfW_Ey2WvQkduYdvbfx_faWm9anUY_Kolvtyw4g.va8Re3DC4_kOLy6bt2oEVXWhueGTAdG-VuoL1SsPZIUg.JPEG.ksunbum97/%EC%97%AC%EC%9E%90_%EB%B0%98%ED%8C%94_3.jpg?type=w966"
# }

# t2_wm = {
#     "name": "long t shirt",
#     "url_1": "https://postfiles.pstatic.net/MjAyMjA1MjdfNTAg/MDAxNjUzNjE3Mjc0MTI0.wim7K-oPN_CQLzaERT64k25rYgjXIAMo3YCt_dHi5wQg.UQO35QD7zlwap8DM3stqs95ur7IPBq17Rpmb-m3-cBgg.JPEG.ksunbum97/%EA%B8%B4%ED%8C%94%ED%8B%B0_5_1.jpg?type=w966",
#     "url_2": "https://postfiles.pstatic.net/MjAyMjA1MjdfMjk3/MDAxNjUzNjE3Mjc0MTIy.LJ0PjXnx3dXYr3r8NAYO1oGPmlxbhtFUUQxJW-eCQlwg.xXQdbbESHE7b9YzlhATIQcfKdDQRxhS2et1OVAbYSmgg.JPEG.ksunbum97/%EA%B8%B4%ED%8C%94%ED%8B%B0_5_2.jpg?type=w966",
#     "url_3": "https://postfiles.pstatic.net/MjAyMjA1MjdfMjIy/MDAxNjUzNjE3Mjc0MTI3.3aW5XNwmYIZedJVv-k9UzD5PFsaABtMcTN1XzFt82x4g.OZYQclmXEbTXcm_rVVw3koqRC4innjA8XY7WuF1VjfIg.JPEG.ksunbum97/%EA%B8%B4%ED%8C%94%ED%8B%B0_5_3.jpg?type=w966"
# }

# t3_wm = {
#     "name": "coat",
#     "url_1": "https://postfiles.pstatic.net/MjAyMjA1MjdfMjg0/MDAxNjUzNjE1NjMxNjkx.hsBWGiZLS4j9mbxLcm91ylA25Aj6jyD970ecHVLCd1Ug.bgbtB7Uhapddsu0VKHHY4WM8oPFZRqs5RlFNva0-Q7Ig.JPEG.ksunbum97/%EC%BD%94%ED%8A%B8_15_3.jpg?type=w966",
#     "url_2": "https://postfiles.pstatic.net/MjAyMjA1MjdfMjU5/MDAxNjUzNjE1NjMxNjg1.kGgPLlMtIxKCbnIOz9iufj6a00D-UDiT-xp6HGGce80g.A9eOKo8ypO3bCdZwN7CMacob29EzZACHosPoI4pk8tgg.JPEG.ksunbum97/%EC%BD%94%ED%8A%B8_15_1.jpg?type=w966",
#     "url_3": "https://postfiles.pstatic.net/MjAyMjA1MjdfNTcg/MDAxNjUzNjE1NjMxNjkz.osrveORouJx6a-WmsFehiAWbjIUc_LQfPS0vouCaoeUg.4g6NQ-YqYehEwMzQxJMSw9kz6980w07K-LuO5bVMybAg.JPEG.ksunbum97/%EC%BD%94%ED%8A%B8_15_2.jpg?type=w966"
# }

# t4_wm = {
#     "name": "shirt",
#     "url_1": "https://postfiles.pstatic.net/MjAyMjA1MjdfNTEg/MDAxNjUzNjE3MzM3MzQy.NC8XfCNGNWuwluhil_S4vVLy5SjJYRlEnxFzqlgbwKIg.ZGj_6-51I6S1vkeff_sAgDzW4CSc5BZEu8WC9JlmzoMg.JPEG.ksunbum97/%EC%85%94%EC%B8%A0_6_3.jpg?type=w966",
#     "url_2": "https://postfiles.pstatic.net/MjAyMjA1MjdfMjk3/MDAxNjUzNjE3MzM3MzM4.L3frjDdrCMjg_NcvzGmVKJmizHEMEYo_OCEVYvmSy_wg.-bg-Y-7BecVTekrRCvJ1322-y5BvufPm4OwJtUyuhNgg.JPEG.ksunbum97/%EC%85%94%EC%B8%A0_6_1.jpg?type=w966",
#     "url_3": "https://postfiles.pstatic.net/MjAyMjA1MjdfMjE3/MDAxNjUzNjE3MzM3MzQ1.7c2v0KGO9XstOjpCgvNXY_cr7cWSzYBIEdPDat48VJAg.UcA7BQ9xFHWICSRJ3qCa4SItPJ8OAe7W1Xe7JwjnHJ8g.JPEG.ksunbum97/%EC%85%94%EC%B8%A0_6_2.jpg?type=w966"
# }

# t5_wm = {
#     "name": "jacket",
#     "url_1": "https://postfiles.pstatic.net/MjAyMjA1MjdfNTQg/MDAxNjUzNjE1NjE0Mzcx.SfX2Ql6Xix0hT9K4DxMPTfplHs7lcDkTTxlybyR2noMg.CXywtsiQ8RcQ0zvasOT4YhnD0431WexEXEcDEY8suLgg.JPEG.ksunbum97/%EC%9E%90%EC%BC%93_14_3.jpg?type=w966",
#     "url_2": "https://postfiles.pstatic.net/MjAyMjA1MjdfMjM3/MDAxNjUzNjE1NjE0Mzgz.fJbRSf2avnEEgEXwUZRFVCKo4WkcjUbrkDQUBvxYf20g.fR0Ng3PRNdiMO3ycf4hlLPbUt-m_6IMVCEajVOk3jfIg.JPEG.ksunbum97/%EC%9E%90%EC%BC%93_14_1.jpg?type=w966",
#     "url_3": "https://postfiles.pstatic.net/MjAyMjA1MjdfMTc3/MDAxNjUzNjE1NjE0Mzk0.aWjrzyLM3brHYOkwuQs44TUfBpcKcT_EpWzmzSfnY2kg.3SJ9d5Lz9JZSa-Imm6IqQ65FgluC2uh5Qd0LY6-t_F0g.JPEG.ksunbum97/%EC%9E%90%EC%BC%93_14_2.jpg?type=w966"
# }

# t6_wm = {
#     "name": "sweater",
#     "url_1": "",
#     "url_2": "",
#     "url_3": ""
# }

# t7_wm = {
#     "name": "tank top",
#     "url_1": "https://postfiles.pstatic.net/MjAyMjA1MjdfMzUg/MDAxNjUzNjE1Mzc3MDk0.FznGB2vXKDqnjra8rTD186td2XJWUdFdMbyrkjBK8Lwg.T7-PAmpZlKfI-1ZLBeYxpIuqeeBSibDnmpWMs5qiY4Yg.JPEG.ksunbum97/%EC%97%AC%EC%9E%90_%EB%AF%BC%EC%86%8C%EB%A7%A4_1.jpg?type=w966",
#     "url_2": "https://postfiles.pstatic.net/MjAyMjA1MjdfMTU2/MDAxNjUzNjE1Mzc3MTE1.KEN31lTV7nt6erhpmokOQ2G_LhyCQRxxWUiOyHLlMx4g.yrG4mIOg8Ez64OzhsUUjF8-H9xzU1SRD8zGk_OCJvrEg.JPEG.ksunbum97/%EC%97%AC%EC%9E%90_%EB%AF%BC%EC%86%8C%EB%A7%A4_2.jpg?type=w966",
#     "url_3": "https://postfiles.pstatic.net/MjAyMjA1MjdfNDUg/MDAxNjUzNjE1Mzc3MTEw.si8cjzIahZEyHcw79-sxKBdTPZL_opogBB9elh2O-PUg.lJ6ngFnq9nTOdXFPZvNwio1FonUpGSPa6pHYR5IoSm0g.JPEG.ksunbum97/%EC%97%AC%EC%9E%90_%EB%AF%BC%EC%86%8C%EB%A7%A4_3.jpg?type=w966"
# }

# t8_wm = {
#     "name": "padding",
#     "url_1": "https://postfiles.pstatic.net/MjAyMjA1MjdfMjA0/MDAxNjUzNjE1NjQyNjM3.p2W6oYu3vji9JOn_bRYidCip2-DZVb4l_lbjnvucNxQg.ksPGVQTSHNesTuzsqCEBh8tkS_UwnLsxxZrew2kMzscg.JPEG.ksunbum97/%ED%8C%A8%EB%94%A9_16_3.jpg?type=w966",
#     "url_2": "https://postfiles.pstatic.net/MjAyMjA1MjdfMjcy/MDAxNjUzNjE1NjQyNjM3.fnlDRoELemo41YvvuWcpfRUi9Nm7Bl5kLtI4M-Yq68wg.QZYZdihnQLWmtxbSjnVZjujXocf7tbxDVTYfj_uojb8g.JPEG.ksunbum97/%ED%8C%A8%EB%94%A9_16_1.jpg?type=w966",
#     "url_3": "https://postfiles.pstatic.net/MjAyMjA1MjdfMjU1/MDAxNjUzNjE1NjQyNjQ2.bEn76HpoPcgi-WCGj6w_ETMBYIh2YTi_x8bldFHPViQg.Efhgz84JdUjhn7vmzJI8_fYkZwhn2VpvjT3HePfrmNcg.JPEG.ksunbum97/%ED%8C%A8%EB%94%A9_16_2.jpg?type=w966"
# }




# b1_wm = {
#     "name": "jeans",
#     "url_1": "https://postfiles.pstatic.net/MjAyMjA1MjdfMjgw/MDAxNjUzNjE3MzU0NDky.nu8nxp0HNFyAiIstWlGeArquuCUJHasGVkthcL5w0A4g.N2d0Ebs5yCKlpxCqWBZwlSHE0Jz26Jaf8tlxoO6Q9aIg.JPEG.ksunbum97/%EC%B2%AD%EB%B0%94%EC%A7%80_8_3.jpg?type=w966",
#     "url_2": "https://postfiles.pstatic.net/MjAyMjA1MjdfMjE4/MDAxNjUzNjE3MzU0NTAy.kCLdtZbgI0tEEKwPxJyhp8CnXU3uxtYD2aTsE3iV4pAg.FZ7SLauYW3Ma0Lu1cBMhK_R9D9l6raKadhuPvOXU87gg.JPEG.ksunbum97/%EC%B2%AD%EB%B0%94%EC%A7%80_8_1.jpg?type=w966",
#     "url_3": "https://postfiles.pstatic.net/MjAyMjA1MjdfMjY0/MDAxNjUzNjE3MzU0NTAw.sF6pUydMQVba7bxs305shXqO3WhQ5CKwTtcjPZgv_68g.jLlqmNJu67O25KprD0hSGdBJkulAZ72qhbPzLDDigTog.JPEG.ksunbum97/%EC%B2%AD%EB%B0%94%EC%A7%80_8_2.jpg?type=w966"
# }

# b2_wm = {
#     "name": "training bottom",
#     "url_1": "https://postfiles.pstatic.net/MjAyMjA1MjdfODUg/MDAxNjUzNjE1NTI2ODY4.h2F9rr1fkzYeMlMEUeOL8I5I60sNVb5tKvDMLHWKYFMg.QqJ_BXcb5KVFHv4LMtPrnOawTIX0Om18cPaBnMnb4Nwg.JPEG.ksunbum97/%EC%97%AC%EC%9E%90_%ED%8A%B8%EB%A0%88%EC%9D%B4%EB%8B%9D%ED%8C%AC%EC%B8%A01.jpg?type=w966",
#     "url_2": "https://postfiles.pstatic.net/MjAyMjA1MjdfMTg3/MDAxNjUzNjE1NTI2ODc3.xJPin0QqO_zGoHp11oJ1ULm0KEyooRET36U7QScEJnUg.xB-1FGs6invkQ-kE1tFglLBvggWYe359yihMQTT62Sog.JPEG.ksunbum97/%EC%97%AC%EC%9E%90_%ED%8A%B8%EB%A0%88%EC%9D%B4%EB%8B%9D%ED%8C%AC%EC%B8%A02.jpg?type=w966",
#     "url_3": "https://postfiles.pstatic.net/MjAyMjA1MjdfNDkg/MDAxNjUzNjE1NTI2ODgy.qYsjGSWSpIbLsifdwvojvl7Nb57du0yluGU9XeRmYiMg.XE1Wr4ItZbvFpPBzQ7SA5evfT6R8DNs3yaAAuGwjcZQg.JPEG.ksunbum97/%EC%97%AC%EC%9E%90_%ED%8A%B8%EB%A0%88%EC%9D%B4%EB%8B%9D%ED%8C%AC%EC%B8%A03.jpg?type=w966"
# }

# b3_wm = {
#     "name": "slacks",
#     "url_1": "https://postfiles.pstatic.net/MjAyMjA1MjdfMjY5/MDAxNjUzNjE1NTA2Njcw.bSu2ukwAu0dQ2J1DZlMe9TX66YQ6PIqJG91bbTrZvi0g.vQm0685gus-mHzZqeqilqlM9SqgaS1nxyC0TgSw-uRsg.JPEG.ksunbum97/%EC%97%AC%EC%9E%90%EC%8A%AC%EB%9E%99%EC%8A%A41.jpg?type=w966",
#     "url_2": "https://postfiles.pstatic.net/MjAyMjA1MjdfMTk4/MDAxNjUzNjE1NTA2NjY3.koJlc_eiA4K4tEUKGogUNTCtuCirk7UYCscnFC82Mwkg.649DJjzDyqARs5JfrAIVWfHYNiNrwRHJTTX6i8omvOAg.JPEG.ksunbum97/%EC%97%AC%EC%9E%90%EC%8A%AC%EB%9E%99%EC%8A%A42.jpg?type=w966",
#     "url_3": "https://postfiles.pstatic.net/MjAyMjA1MjdfMTg0/MDAxNjUzNjE1NTA2Njcz.qxulLi3LwvzcBHlvdXNtEgUv6Mf5Hqk0-e2-PTwiTHAg.aMMLRPd8eRur71Saldb12lUW4gCm7m_PSk6P8RdV0c8g.JPEG.ksunbum97/%EC%97%AC%EC%9E%90%EC%8A%AC%EB%9E%99%EC%8A%A43.jpg?type=w966"
# }

# b4_wm = {
#     "name": "cotton bottom",
#     "url_1": "https://postfiles.pstatic.net/MjAyMjA1MjdfODcg/MDAxNjUzNjE1NDg5MDEy.gT_aAYSIu347UrygIKWpj3eX8EAPMTQ8cVHclWgTwc4g.i3Lujec8q1_vo9Gvk2a-83l-jQTkedl7zqqNorNEKmUg.JPEG.ksunbum97/%EC%97%AC%EC%9E%90%EB%A9%B4%EB%B0%94%EC%A7%801.jpg?type=w966",
#     "url_2": "https://postfiles.pstatic.net/MjAyMjA1MjdfMTYx/MDAxNjUzNjE1NDg5MDEy.hpTh22dnretCIfSVOTd8stt3kBzETrxYWO4tPAl4eo0g.onR3Bk9P-8YITYGFTqe9tiT8yeYigKNuiw0l1bjqboIg.JPEG.ksunbum97/%EC%97%AC%EC%9E%90%EB%A9%B4%EB%B0%94%EC%A7%802.jpg?type=w966",
#     "url_3": "https://postfiles.pstatic.net/MjAyMjA1MjdfMTM4/MDAxNjUzNjE1NDg5MDMz.j9reFcYHvEzH5qtULpumGoo1dzocngIvMFS_yxrPhoUg.JLyhxs_7qoujYKykvmakgrm0uNvNBMh4OC5azTow7vMg.JPEG.ksunbum97/%EC%97%AC%EC%9E%90%EB%A9%B4%EB%B0%94%EC%A7%803.jpg?type=w966"
# }

# b5_wm = {
#     "name": "short bottom",
#     "url_1": "https://postfiles.pstatic.net/MjAyMjA1MjdfMjQ2/MDAxNjUzNjE1NDE0MTk3.5eP0l2okKWtS2qkF8a6NyVdIjlmAkhM74DZcyPx80_Mg.V9kVdbZ7WXRrZzgcL-DA4jqXKilaFSZb9bmxzQdh_-og.JPEG.ksunbum97/%EC%97%AC%EC%9E%90_%EB%B0%98%EB%B0%94%EC%A7%80_1.jpg?type=w966",
#     "url_2": "https://postfiles.pstatic.net/MjAyMjA1MjdfNjQg/MDAxNjUzNjE1NDE0MTk5.-J7s9wBX22TRhmHEJ-2Yu-62Va9RZElmf97lmV29xEog.rYlZ5rE7-4ytSkrUWUFgm18EVaN7Z68GhQvmHyK3Hwkg.JPEG.ksunbum97/%EC%97%AC%EC%9E%90_%EB%B0%98%EB%B0%94%EC%A7%80_2.jpg?type=w966",
#     "url_3": "https://postfiles.pstatic.net/MjAyMjA1MjdfMjQw/MDAxNjUzNjE1NDE0MjAz.bixbYFy3CWSb9Dj4vCNAI0raOpncYyCWS3TOuFgH9bgg.M6FYKEFCa3tXkoFOJMQdXc3G6kCqbkOuKyb3sa7M8Lwg.JPEG.ksunbum97/%EC%97%AC%EC%9E%90_%EB%B0%98%EB%B0%94%EC%A7%80_3.jpg?type=w966"
# }

# b6_wm = {
#     "name": "long skirt",
#     "url_1": "https://postfiles.pstatic.net/MjAyMjA1MjdfMTMx/MDAxNjUzNjE1NjAwMzk5.emEeMEwbNIvfznq8s53juv0e4CfsVzOogz6wY5P09PAg.Sn8_uUIjahqa649ybIXTaHDd17xDlq-s4utKy0QrK2Yg.JPEG.ksunbum97/%EB%A1%B1%EC%8A%A4%EC%BB%A4%ED%8A%B8_13_3.jpg?type=w966",
#     "url_2": "https://postfiles.pstatic.net/MjAyMjA1MjdfMTMw/MDAxNjUzNjE1NjAwNDAy.T5pZ-M-8eAXC5gebONbj1slXkYLvKlPGJidkdKn-I4gg.hZKn5faBnXuodp5vmrwePAdsuXgjUajgteM1NJ8PSxgg.JPEG.ksunbum97/%EB%A1%B1%EC%8A%A4%EC%BB%A4%ED%8A%B8_13_1.jpg?type=w966",
#     "url_3": "https://postfiles.pstatic.net/MjAyMjA1MjdfMTg4/MDAxNjUzNjE1NjAwNDY5.4LtOVrzjwK2r_B2yFaP9uhhbu2pDv0XLeTtDZBvbEI8g.vjE2S1grNHEOSX0tte5IY7ysD7bP1D_eSBuc5V15tPIg.JPEG.ksunbum97/%EB%A1%B1%EC%8A%A4%EC%BB%A4%ED%8A%B8_13_2.jpg?type=w966"
# }

# b7_wm = {
#     "name": "leggings",
#     "url_1": "https://postfiles.pstatic.net/MjAyMjA1MjdfNjYg/MDAxNjUzNjE1NDY2NDY0.TpYTkSqRX-1KeQ04Jdn15aXOW7GTz9bQbc9QtztnYIUg.4DgGh1Be88pbrJBv3Gzg2XAkZ653PmUi7GPOYKWkiVIg.JPEG.ksunbum97/%EC%97%AC%EC%9E%90%EB%A0%88%EA%B9%85%EC%8A%A41.jpg?type=w966",
#     "url_2": "https://postfiles.pstatic.net/MjAyMjA1MjdfMTEg/MDAxNjUzNjE1NDY2NDY1.p3EdcEBHK6EZzskfNERnP7pJiggqGhfS7-HDX_CJdrEg.vovYYdCjU17ubi0zOmn2R2M6ZBma7KMBupezt5HA0IUg.JPEG.ksunbum97/%EC%97%AC%EC%9E%90%EB%A0%88%EA%B9%85%EC%8A%A42.jpg?type=w966",
#     "url_3": "https://postfiles.pstatic.net/MjAyMjA1MjdfMTg4/MDAxNjUzNjE1NDY2NDgx.aYT7RmleSx8_sew1lk49Mhiz8Z2hYy8saWpW4ca5xrIg.HQr94bkotRki3LSWRG8xU-KMd_C1g2-lIH0U9zrhkmEg.JPEG.ksunbum97/%EC%97%AC%EC%9E%90%EB%A0%88%EA%B9%85%EC%8A%A43.jpg?type=w966"
# }

# b8_wm = {
#     "name": "mini skirt",
#     "url_1": "https://postfiles.pstatic.net/MjAyMjA1MjdfMTYx/MDAxNjUzNjE1NDM5NjU0.zhvXab-IUWK8l_XrQv07ZG-f1Xazp2YEriWaF8V671wg._a7jlNun2TB1Rb9ZOcFDqZ-rr8IULVII1SV_UWM-e7Ig.JPEG.ksunbum97/%EC%97%AC%EC%9E%90_%EB%AF%B8%EB%8B%88%EC%8A%A4%EC%BB%A4%ED%8A%B8_1.jpg?type=w966",
#     "url_2": "https://postfiles.pstatic.net/MjAyMjA1MjdfMjUg/MDAxNjUzNjE1NDM5NjU2.p-ksvdgK2P1igeYoxfVxLNV4UjsaV6IyKB_-iJ3L4tsg.3oi7eYQYa3vQ5mtlMIq7Zb-E93oasXGeLMqgzKXHFn0g.JPEG.ksunbum97/%EC%97%AC%EC%9E%90_%EB%AF%B8%EB%8B%88%EC%8A%A4%EC%BB%A4%ED%8A%B8_2.jpg?type=w966",
#     "url_3": "https://postfiles.pstatic.net/MjAyMjA1MjdfMTc0/MDAxNjUzNjE1NDM5NjY0.tHcRw4hnqlGM8nEpmjFgv5hQvMCB_8iRFN855baBHr4g.cH8ZWLnHB5bAZd_FkdkcXbM1qq8AyHZ2qHytN3jKQJ4g.JPEG.ksunbum97/%EC%97%AC%EC%9E%90_%EB%AF%B8%EB%8B%88%EC%8A%A4%EC%BB%A4%ED%8A%B8_3.jpg?type=w966"
# }





# t1_m = {
#     "name": "short t shirt",
#     "url_1": "https://postfiles.pstatic.net/MjAyMjA1MjdfNTMg/MDAxNjUzNjE1MTkzNTgx.RShqOSBRn1GzO9RznJGw3c2HXpf_An9IJKKUhTZ3mccg.fhIxXNXm7YCgW0o7wMfkuL_AL_rC-8YI_JcXgxq3tVEg.JPEG.ksunbum97/%EB%82%A8%EC%9E%90_%EB%B0%98%ED%8C%94_1.jpg?type=w966",
#     "url_2": "https://postfiles.pstatic.net/MjAyMjA1MjdfMjky/MDAxNjUzNjE1MTkzNTc4.eid2LiBFh44BWlSh2ZnLqnCuSnQlalDqr5WAQXKojpog.nwVYK_9UsAkm466SwCYBSV5G4yxg-aOFrJ6C2hO8VMog.JPEG.ksunbum97/%EB%82%A8%EC%9E%90_%EB%B0%98%ED%8C%94_2.jpg?type=w966",
#     "url_3": "https://postfiles.pstatic.net/MjAyMjA1MjdfODcg/MDAxNjUzNjE1MTkzNTcz.JyqT02DU6gcYFE0930xUTw6wDMf9eRu_rVpTCyrzUXcg.jcMfhqjtaIYRqmSYKsyUGsYEJsn1BzRD8EyL7Idj950g.JPEG.ksunbum97/%EB%82%A8%EC%9E%90_%EB%B0%98%ED%8C%94_3.jpg?type=w966"
# }

# t2_m = {
#     "name": "long t shirt",
#     "url_1": "https://postfiles.pstatic.net/MjAyMjA1MjdfMTc3/MDAxNjUzNjE3NDcxNDY5.25P0FAGgpnyD5iPGkO5UPXjCp9L7WWBiMRVLg4f6jRgg.zAeoxholfZ2DDPcjaH4e3efRIFPguVqtya4BO0C2bpsg.JPEG.ksunbum97/%EA%B8%B4%ED%8C%94%ED%8B%B0_5_3.jpg?type=w966",
#     "url_2": "https://postfiles.pstatic.net/MjAyMjA1MjdfMTc3/MDAxNjUzNjE3NDcxNDY5.25P0FAGgpnyD5iPGkO5UPXjCp9L7WWBiMRVLg4f6jRgg.zAeoxholfZ2DDPcjaH4e3efRIFPguVqtya4BO0C2bpsg.JPEG.ksunbum97/%EA%B8%B4%ED%8C%94%ED%8B%B0_5_3.jpg?type=w966",
#     "url_3": "https://postfiles.pstatic.net/MjAyMjA1MjdfMjI2/MDAxNjUzNjE3NDcxNDgy.vr2D53KE5zUV2T7w0XckIjyVW1Ta-aeIXc4tr0t2wQ8g.yiub6Wj7KtcU1QZ0B2SLye4p0VbU8dHpMOocUfd906Ag.JPEG.ksunbum97/%EA%B8%B4%ED%8C%94%ED%8B%B0_5_2.jpg?type=w966"
# }

# t3_m = {
#     "name": "coat",
#     "url_1": "https://postfiles.pstatic.net/MjAyMjA1MjdfNDMg/MDAxNjUzNjE1MzMxMzk4.WPTRVi6L2EyPAd3TRXNx95Fcnya2PPtKPv-_XE2VDegg.ZKcW2kJF4Lkayk5_akNwuXAB4oQDSGDkpMW_DyPUv4cg.JPEG.ksunbum97/%EC%BD%94%ED%8A%B8_15_3.jpg?type=w966",
#     "url_2": "https://postfiles.pstatic.net/MjAyMjA1MjdfMjE5/MDAxNjUzNjE1MzMxNDA0._z6DKxAubrM5_GRHc9jMS3PZfHLj7EUEBCImTOcTVq0g.VkcH_CcqZ3SsW4kyJJ4-061rpkVB-7KtaHWpMW5l040g.JPEG.ksunbum97/%EC%BD%94%ED%8A%B8_15_1.jpg?type=w966",
#     "url_3": "https://postfiles.pstatic.net/MjAyMjA1MjdfMTIy/MDAxNjUzNjE1MzMxNDA4.LPlxR8Gs9Q7f8ixWbaL3NiyU6fAQwIdnYz9KXhZMu58g.txNvWGCQRHfp36cNCYdWmmJ3iZTQfrIOHyV8gQz-LHMg.JPEG.ksunbum97/%EC%BD%94%ED%8A%B8_15_2.jpg?type=w966"
# }

# t4_m = {
#     "name": "shirt",
#     "url_1": "https://postfiles.pstatic.net/MjAyMjA1MjdfMTk2/MDAxNjUzNjE3NTAyODU3.h6UrqMNJIyElXMOn6bCCZJtIpf05UKuA7qGPRQ7PO6Ug.t3touqmLwvJ39MtpSdp3n9mRurheI8QFnMmoo7pp9vkg.JPEG.ksunbum97/%EC%85%94%EC%B8%A0_6_3.jpg?type=w966",
#     "url_2": "https://postfiles.pstatic.net/MjAyMjA1MjdfOTUg/MDAxNjUzNjE3NTAyODU2._GrggKkBvXm7vMUNV7cXRwygu6WFAGX9PGJtw0ndTzsg.ElifosmD3X2Hxk6t__SGMHBfHo-B64121faKBPZ3EVYg.JPEG.ksunbum97/%EC%85%94%EC%B8%A0_6_1.jpg?type=w966",
#     "url_3": "https://postfiles.pstatic.net/MjAyMjA1MjdfODQg/MDAxNjUzNjE3NTAyODY1.4djc0aa4mntLrzxuOkP8p-VqaK3tI7hTxDZXH-yYkAwg.PeERb9jLpiYB_Uyj3bG6XnKw9syktXjXHm6rduHua0Mg.JPEG.ksunbum97/%EC%85%94%EC%B8%A0_6_2.jpg?type=w966"
# }

# t5_m = {
#     "name": "jacket",
#     "url_1": "https://postfiles.pstatic.net/MjAyMjA1MjdfMTc3/MDAxNjUzNjE1MzE1MjQx.KZz8dWEvJu5eBtIUY87pMiuQ2-Pq2U7IxzwkwVjkeagg.YS6jxMntWk93jgdCXupjtNI4LcVupSUI-sq-tsiCbzIg.JPEG.ksunbum97/%EC%9E%90%EC%BC%93_14_3.jpg?type=w966",
#     "url_2": "https://postfiles.pstatic.net/MjAyMjA1MjdfODAg/MDAxNjUzNjE1MzE1MjQy.TFjVvfcAaSQOzPGfxvfK2Hc5N1VbPce6t744ufTxaHYg.echkrtIJineYNlcYqHkYLaPttHt-ceMNlp2jFBKM7kkg.JPEG.ksunbum97/%EC%9E%90%EC%BC%93_14_1.jpg?type=w966",
#     "url_3": "https://postfiles.pstatic.net/MjAyMjA1MjdfMjQy/MDAxNjUzNjE1MzE1MjQ0.FrBfUDcwAUTbbybrheat3pWilWktrxs8z0mGuHn5HScg.bGhRq_oEXSa4UDFIRs_n7zkRwhfGddKNpLpQOinoR4wg.JPEG.ksunbum97/%EC%9E%90%EC%BC%93_14_2.jpg?type=w966"
# }

# t6_m = {
#     "name": "sweater",
#     "url_1": "https://postfiles.pstatic.net/MjAyMjA1MjdfMTcx/MDAxNjUzNjE3NDg4MDI4.SMzkLGZdoGHnTbqPvPGejbFEufU0q7LBVWB6XBfuwWog.-ChqE4sRgRCE_yg8Y4RWJ1DuNmZ9oQfIAcFrRDmYVccg.JPEG.ksunbum97/%EB%8B%88%ED%8A%B8_7_3.jpg?type=w966",
#     "url_2": "https://postfiles.pstatic.net/MjAyMjA1MjdfNTgg/MDAxNjUzNjE3NDg4MDM0.7Mx-SWg3bwGBxi7IOxsPCiwE8bSSi5W-P5fm_4-RCcQg.y7oczBxKid16XBK6CZSb82ECHON_M6Fkme7baubJE4wg.JPEG.ksunbum97/%EB%8B%88%ED%8A%B8_7_1.jpg?type=w966",
#     "url_3": "https://postfiles.pstatic.net/MjAyMjA1MjdfNDUg/MDAxNjUzNjE3NDg4MDQw.j5KKF-ERPbv2L6lDuq_SLKBFaBgZkkg4dAXhb2kJ7g8g.6kThkxu9BfzqxL5egVIZhqpguSDZcScjC2tHZYXoD6cg.JPEG.ksunbum97/%EB%8B%88%ED%8A%B8_7_2.jpg?type=w966"
# }

# t7_m = {
#     "name": "tank top",
#     "url_1": "https://postfiles.pstatic.net/MjAyMjA1MjdfNjMg/MDAxNjUzNjE1MTMwMDQz.MZmhxwMl1tdn8JLELuJgAXUAKG1H1CcQEQgolxjOLdQg.1_A8vFJ56z-Gb3MQ9bPasNZsfcWFQdTfiraTb-gcH0Ug.JPEG.ksunbum97/%EB%82%A8%EC%9E%90_%EB%AF%BC%EC%86%8C%EB%A7%A4_1.jpg?type=w966",
#     "url_2": "https://postfiles.pstatic.net/MjAyMjA1MjdfMTA5/MDAxNjUzNjE1MTMwMDU2.0n4yHGuaXxOw5hlr5mhv-W2IAK_mvxHDeXBxaxqYnSUg.xvjikiVUQmHsrLxQ25ku7HzVs-NIju3sJfs8wowlGl0g.JPEG.ksunbum97/%EB%82%A8%EC%9E%90_%EB%AF%BC%EC%86%8C%EB%A7%A4_2.jpg?type=w966",
#     "url_3": "https://postfiles.pstatic.net/MjAyMjA1MjdfMjEy/MDAxNjUzNjE1MTMwMDQ3.vIKDj7_G3eIlIBvJPXqFfn3yyrJu2XAQhKYHQE2CV0cg.v9hTleIX0djFOFTlcL3m_CB0RNp87yPjONK8pW4NZKog.JPEG.ksunbum97/%EB%82%A8%EC%9E%90_%EB%AF%BC%EC%86%8C%EB%A7%A4_3.jpg?type=w966"
# }

# t8_m = {
#     "name": "padding",
#     "url_1": "https://postfiles.pstatic.net/MjAyMjA1MjdfMTk5/MDAxNjUzNjE1MzQ2NjYw.QSWABL91FdHueXAhUbDxYTYOh87oDP8JvxzmFITEYLMg.PIZripUKnf4E_0rdBbJ8AZ9gIE7MyBKGjznsVb_exu0g.JPEG.ksunbum97/%ED%8C%A8%EB%94%A9_16_3.jpg?type=w966",
#     "url_2": "https://postfiles.pstatic.net/MjAyMjA1MjdfMjkz/MDAxNjUzNjE1MzQ2NjYz.iGG5U16G90mQKiG54Rn-MChRURyD6xoh65k81Me-uhMg.Vx4uk9fnQAQ5oUMcKDAmWfsLNqUUE8DgEwa7WhMgBjcg.JPEG.ksunbum97/%ED%8C%A8%EB%94%A9_16_1.jpg?type=w966",
#     "url_3": "https://postfiles.pstatic.net/MjAyMjA1MjdfNDcg/MDAxNjUzNjE1MzQ2Njc4.c7GxsnSSBpkd2-tcLTk7TDeQpCAKPtkXsCs7LJ3hINIg.4QgAdT9IbU7aAAXsNkoP8ODsd9_UpPPOo95Oe5Rwnocg.JPEG.ksunbum97/%ED%8C%A8%EB%94%A9_16_2.jpg?type=w966"
# }

# b1_m = {
#     "name": "jeans",
#     "url_1": "https://postfiles.pstatic.net/MjAyMjA1MjdfNDcg/MDAxNjUzNjE1MzQ2Njc4.c7GxsnSSBpkd2-tcLTk7TDeQpCAKPtkXsCs7LJ3hINIg.4QgAdT9IbU7aAAXsNkoP8ODsd9_UpPPOo95Oe5Rwnocg.JPEG.ksunbum97/%ED%8C%A8%EB%94%A9_16_2.jpg?type=w966",
#     "url_2": "https://postfiles.pstatic.net/MjAyMjA1MjdfMTg4/MDAxNjUzNjE3NTE2OTEx.IP3TObXLdF25F3jj9dt18pC-CTo3NH0xr2i0jvnUwFgg.6EcGWr-GJjZtWMSry3TM5pRGMzokTgYQpIGD0oqHQbwg.JPEG.ksunbum97/%EC%B2%AD%EB%B0%94%EC%A7%80_8_1.jpg?type=w966",
#     "url_3": "https://postfiles.pstatic.net/MjAyMjA1MjdfMzIg/MDAxNjUzNjE3NTE2OTEy.PRhCzEfpc7lbiJN4TMctFUlnM6iZ3wyaF4ie9FtP8K4g.zLNeE5yGs0_CyGFv1l05_gMpGD8KlxZo98ZH08bhl_gg.JPEG.ksunbum97/%EC%B2%AD%EB%B0%94%EC%A7%80_8_2.jpg?type=w966"
# }

# b2_m = {
#     "name": "training bottom",
#     "url_1": "https://postfiles.pstatic.net/MjAyMjA1MjdfMjM1/MDAxNjUzNjE1MjkwOTU5.QVt3IiIFnPQOxYlhvKaLiEw1clGlar-cnjeasvU8c3Qg.N7LujiKQ8Mlnd0YzMYF7qFFxfjCQ4gwGfhfpdEjc8WAg.JPEG.ksunbum97/%EB%82%A8%EC%9E%90_%ED%8A%B8%EB%A0%88%EC%9D%B4%EB%8B%9D%ED%8C%AC%EC%B8%A01.jpg?type=w966",
#     "url_2": "https://postfiles.pstatic.net/MjAyMjA1MjdfMTky/MDAxNjUzNjE1MjkwOTYx.63QCzoAheLV7uMM5YMkzHkrpkbsbm8i0qgTzariOD_Mg.0u6YiSOgGHLIQXY-Ov2qVi4eXAQfdUiawT9pdCccng4g.JPEG.ksunbum97/%EB%82%A8%EC%9E%90_%ED%8A%B8%EB%A0%88%EC%9D%B4%EB%8B%9D%ED%8C%AC%EC%B8%A03.jpg?type=w966",
#     "url_3": "https://postfiles.pstatic.net/MjAyMjA1MjdfMjQw/MDAxNjUzNjE1MjkwOTc5.Qesz1ycOxEVwQiIORn2SVywDogNs1xFvX9PemDRVQJog.dbqV37wgm2K3Ss6t4pCuxfq2ED5qnG2e3hkGVYitoz4g.JPEG.ksunbum97/%EB%82%A8%EC%9E%90%ED%8A%B8%EB%A0%88%EC%9D%B4%EB%8B%9D%ED%8C%AC%EC%B8%A02.jpg?type=w966"
# }

# b3_m = {
#     "name": "slacks",
#     "url_1": "https://postfiles.pstatic.net/MjAyMjA1MjdfMjU2/MDAxNjUzNjE1MjcxODA3.92gi5yQwfEZ4QsDLar_7rP_u679_v3uZDm8u_MHxVRog.BGql6lAifC8fxjg_WAaVhc93-XtloaLvisijdGFJatog.JPEG.ksunbum97/%EB%82%A8%EC%9E%90%EC%8A%AC%EB%9E%99%EC%8A%A41.jpg?type=w966",
#     "url_2": "https://postfiles.pstatic.net/MjAyMjA1MjdfNDcg/MDAxNjUzNjE1MjcxODA4._fTRkk-RQXYBbTTsRgDklY93wy743rfUb2130kljBqsg.jzPKALlEhEMdSBD73EsM-fuC99lQDzB5H0t4-PHXYJkg.JPEG.ksunbum97/%EB%82%A8%EC%9E%90%EC%8A%AC%EB%9E%99%EC%8A%A42.jpg?type=w966",
#     "url_3": "https://postfiles.pstatic.net/MjAyMjA1MjdfMjM3/MDAxNjUzNjE1MjcxODE4.RhWi2wwhj6fADUUtxD2AvWz5OPZffZg2ZhuqfhUImqog.g0Rxd2GSdkV76EjC6Q03TX_U2KvWW22-lOjEHK8mTDcg.JPEG.ksunbum97/%EB%82%A8%EC%9E%90%EC%8A%AC%EB%9E%99%EC%8A%A43.jpg?type=w966"
# }

# b4_m = {
#     "name": "cotton bottom",
#     "url_1": "https://postfiles.pstatic.net/MjAyMjA1MjdfMTQz/MDAxNjUzNjE1MjQyMDk5.FLTdnEwRQfZDA1sfZ7gKgP1o-ypjOCdRIezxncWj1EYg.SRtlbCmcIPp8HZm8b_RmNnglFXYgYMFWyOMtTZy2R6kg.JPEG.ksunbum97/%EB%82%A8%EC%9E%90%EB%A9%B4%EB%B0%94%EC%A7%80.jpg?type=w966",
#     "url_2": "https://postfiles.pstatic.net/MjAyMjA1MjdfMjQ0/MDAxNjUzNjE1MjQyMTAx.zV28TiG1Iap3aFarCT84jt-Iga8ad1Sx7F9PO-rCqYEg.ETxIdgrtDE4jLRtru_lL2vBMmWUEi5urk2JVm-t4mjgg.JPEG.ksunbum97/%EB%82%A8%EC%9E%90%EB%A9%B4%EB%B0%94%EC%A7%802.jpg?type=w966",
#     "url_3": "https://postfiles.pstatic.net/MjAyMjA1MjdfNDYg/MDAxNjUzNjE1MjQyMTE4.AljiLzoWFnYwrWg4XXT3oYDsxX9C6d65-4ZFgt4-ub4g.-yydFsKHeG82BTjLh2kfQdEnyRx-INHKxo2w7E0d8FAg.JPEG.ksunbum97/%EB%82%A8%EC%9E%90%EB%A9%B4%EB%B0%94%EC%A7%803.jpg?type=w966"
# }

# b5_m = {
#     "name": "short bottom",
#     "url_1": "https://postfiles.pstatic.net/MjAyMjA1MjdfNjgg/MDAxNjUzNjE1MjE2ODIz.fEOKZHGhhkuOMjvTphXXhIaxAezOMbWBRL9SxLBizP4g.MXNP_ELEqYVSyzKsx5nlhT9WYjws5VAfxG79sJWQK98g.JPEG.ksunbum97/%EB%82%A8%EC%9E%90_%EB%B0%98%EB%B0%94%EC%A7%80_1.jpg?type=w966",
#     "url_2": "https://postfiles.pstatic.net/MjAyMjA1MjdfMTY1/MDAxNjUzNjE1MjE2ODM2.5A2txx0TSbg3yPn_JYHgjTUpHS9BdVnSMjKKEIFv-0og.sAvYCxveQpXBEl46Z8q4WGFkOZhMuP0WbQABIj86_6Yg.JPEG.ksunbum97/%EB%82%A8%EC%9E%90_%EB%B0%98%EB%B0%94%EC%A7%80_2.jpg?type=w966",
#     "url_3": "https://postfiles.pstatic.net/MjAyMjA1MjdfODcg/MDAxNjUzNjE1MjE2ODM3.JCpXWXCsTERH_HAI29oDVbUNJM16AlKZ-20hNVaQLOAg.YJIEkDW9XwfCgn43gvJ54oZRB8TSQHrM81st_mbsvgYg.JPEG.ksunbum97/%EB%82%A8%EC%9E%90_%EB%B0%98%EB%B0%94%EC%A7%80_3.jpg?type=w966"
# }
