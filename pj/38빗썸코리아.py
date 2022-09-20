import cr_38 as cr
# 빗썸코리아
# URL : http://www.38.co.kr/html/forum/board/?o=v&code=341650&no=13&page=15
# 종목코드 : 341650
# 게시글 number: 13~707

hob_df = cr.make_df(13, 708, '341650')  # startpagenum, endpagenum, 종목코드
hob_df.to_csv('38빗썸코리아.csv')