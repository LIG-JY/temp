import cr_38 as cr
# 현대오일뱅크
# URL : http://www.38.co.kr/html/forum/board/?code=004050
# 종목코드 : 004050
# 게시글 number: 2018~2517

hob_df = cr.make_df(2018, 2518, '004050')  # startpagenum, endpagenum, 종목코드
hob_df.to_csv('38현대오일뱅크.csv')
