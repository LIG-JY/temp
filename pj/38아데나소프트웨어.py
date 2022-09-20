import cr_38 as cr
# 아데나소프트웨어
# URL : http://www.38.co.kr/html/forum/board/?o=v&code=325380&no=2&page=3
# 종목코드 : 325380
# 게시글 number: 2~118

hob_df = cr.make_df(2, 119, '325380')  # startpagenum, endpagenum, 종목코드
hob_df.to_csv('38아데나소프트웨어.csv')
