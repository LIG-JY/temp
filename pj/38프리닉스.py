import cr_38 as cr
# 프리닉스
# URL : http://www.38.co.kr/html/forum/board/?o=v&code=295110&no=5&page=4
# 종목코드 : 295110
# 게시글 number: 5~120

hob_df = cr.make_df(5, 121, '295110')  # startpagenum, endpagenum, 종목코드
hob_df.to_csv('38프리닉스.csv')