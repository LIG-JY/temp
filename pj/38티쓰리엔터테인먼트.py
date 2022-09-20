import cr_38 as cr
# 티쓰리엔터테인먼트
# URL : http://www.38.co.kr/html/forum/board/?o=v&code=204610&no=31&page=1
# 종목코드 : 204610
# 게시글 number: 1~31

hob_df = cr.make_df(1, 31, '204610')  # startpagenum, endpagenum, 종목코드
hob_df.to_csv('38티쓰리엔터테인먼트.csv')
