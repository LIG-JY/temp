import cr_38 as cr
# 펨트론
# URL : http://www.38.co.kr/html/forum/board/?o=v&code=168360&no=1&page=3
# 종목코드 : 168360
# 게시글 number: 1~74

hob_df = cr.make_df(1, 75, '168360')  # startpagenum, endpagenum, 종목코드
hob_df.to_csv('38펨트론.csv')