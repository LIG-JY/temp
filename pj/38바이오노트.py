import cr_38 as cr
# 바이오노트
# URL : http://www.38.co.kr/html/forum/board/?o=v&code=377740&no=4&page=3
# 종목코드 : 377740
# 게시글 number: 4~93

hob_df = cr.make_df(4, 94, '377740')  # startpagenum, endpagenum, 종목코드
hob_df.to_csv('38바이오노트.csv')