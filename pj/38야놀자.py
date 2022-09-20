import cr_38 as cr
# 야놀자
# URL : http://www.38.co.kr/html/forum/board/?code=350920
# 종목코드 : 350920
# 게시글 number: 3~177

hob_df = cr.make_df(3, 178, '350920')  # startpagenum, endpagenum, 종목코드
hob_df.to_csv('38야놀자.csv')