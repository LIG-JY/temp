import cr_38 as cr
# 컬리
# URL : http://forum.38.co.kr/html/forum/board/?o=v&code=408480&no=3&page=8
# 종목코드 : 408480
# 게시글 number: 3~366

hob_df = cr.make_df(3, 367, '408480')  # startpagenum, endpagenum, 종목코드
hob_df.to_csv('38컬리.csv')