import cr_38 as cr
# 지엔티파마
# URL : http://www.38.co.kr/html/forum/board/?o=v&code=228980&no=3393&page=15
# 종목코드 : 228980
# 게시글 number: 3393~4272

hob_df = cr.make_df(3393, 4273, '228980')  # startpagenum, endpagenum, 종목코드
hob_df.to_csv('38지엔티파마.csv')
