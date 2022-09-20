import cr_38 as cr
# 뉴로메카
# URL : http://www.38.co.kr/html/forum/board/?o=v&code=348340&no=68
# 종목코드 : 348340
# 게시글 number: 1~68

hob_df = cr.make_df(1, 69, '348340')  # startpagenum, endpagenum, 종목코드
hob_df.to_csv('38뉴로메카.csv')
