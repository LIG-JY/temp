import cr_38 as cr
# 엑스엘게임즈
# URL : http://forum.38.co.kr/html/forum/board/?o=v&code=225630&no=1&page=6
# 종목코드 : 225630
# 게시글 number: 1~227

hob_df = cr.make_df(1, 228, '225630')  # startpagenum, endpagenum, 종목코드
hob_df.to_csv('38엑스엘게임즈.csv')