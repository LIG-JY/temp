import cr_38 as cr
# LGCNS
# URL : http://www.38.co.kr/html/forum/board/?code=064400
# 종목코드 : 064400
# 게시글 number: 56457~57854

hob_df = cr.make_df(56457, 57854, '064400')  # startpagenum, endpagenum, 종목코드
hob_df.to_csv('38LGCNS.csv')



