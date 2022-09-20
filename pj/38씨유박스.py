import cr_38 as cr
# 씨유박스
# URL : http://www.38.co.kr/html/forum/board/?o=v&code=340810&no=1&page=6
# 종목코드 : 340810
# 게시글 number: 1~254

hob_df = cr.make_df(1, 255, '340810')  # startpagenum, endpagenum, 종목코드
hob_df.to_csv('38씨유박스.csv')
