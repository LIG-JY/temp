import cr_38 as cr
# 제이비케이랩
# URL : http://www.38.co.kr/html/forum/board/?o=v&code=238930&no=1234&page=15
# 종목코드 : 238930
# 게시글 number: 1234~2520

hob_df = cr.make_df(1234, 2521, '238930')  # startpagenum, endpagenum, 종목코드
hob_df.to_csv('38제이비케이랩.csv')
