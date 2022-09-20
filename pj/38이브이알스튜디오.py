import cr_38 as cr
# 이브이알스튜디오
# URL : http://www.38.co.kr/html/forum/board/?o=v&code=379660&no=268&page=4
# 종목코드 : 379660
# 게시글 number: 268~416

hob_df = cr.make_df(268, 417, '379660')  # startpagenum, endpagenum, 종목코드
hob_df.to_csv('38이브이알스튜디오.csv')