import cr_38 as cr
# 큐라티스
# URL : http://www.38.co.kr/html/forum/board/?o=v&code=348080&no=2200&page=15
# 종목코드 : 348080
# 게시글 number: 2200~3115

hob_df = cr.make_df(2200, 3116, '348080')  # startpagenum, endpagenum, 종목코드
hob_df.to_csv('38큐라티스.csv')
