import cr_38 as cr
# 밴코리아
# URL : http://www.38.co.kr/html/forum/board/?o=v&code=433820&no=6&page=2
# 종목코드 : 433820
# 게시글 number: 6~53

hob_df = cr.make_df(6, 54, '433820')  # startpagenum, endpagenum, 종목코드
hob_df.to_csv('38밴코리아.csv')