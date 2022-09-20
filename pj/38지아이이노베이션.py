import cr_38 as cr
# 지아이이노베이션
# URL : http://www.38.co.kr/html/forum/board/?o=v&code=358570&no=105&page=15
# 종목코드 : 358570
# 게시글 number: 105~994

hob_df = cr.make_df(105, 995, '358570')  # startpagenum, endpagenum, 종목코드
hob_df.to_csv('38지아이이노베이션.csv')
