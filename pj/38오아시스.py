import cr_38 as cr
# 오아시스
# URL : http://forum.38.co.kr/html/forum/board/?o=v&code=370190&no=1&page=5
# 종목코드 : 370190
# 게시글 number: 1~174

hob_df = cr.make_df(1, 175, '370190')  # startpagenum, endpagenum, 종목코드
hob_df.to_csv('38오아시스.csv')