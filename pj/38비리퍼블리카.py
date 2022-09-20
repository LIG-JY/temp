import cr_38 as cr
# 비바리퍼블리카
# URL : http://forum.38.co.kr/html/forum/board/?code=285240
# 종목코드 : 285240
# 게시글 number: 9~119

hob_df = cr.make_df(9, 120, '285240')  # startpagenum, endpagenum, 종목코드
hob_df.to_csv('38비바리퍼블리카.csv')