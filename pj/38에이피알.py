import cr_38 as cr
# 에이피알
# URL : http://www.38.co.kr/html/forum/board/?o=v&code=278470&no=1&page=10
# 종목코드 : 278470
# 게시글 number: 1~439

hob_df = cr.make_df(1, 440, '278470')  # startpagenum, endpagenum, 종목코드
hob_df.to_csv('38에이피알.csv')
