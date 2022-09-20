import cr_38 as cr
# 현대엔지니어링
# URL : http://forum.38.co.kr/html/forum/board/?o=v&code=064540
# 종목코드 : 064540
# 게시글 number: 105794~106866

hob_df = cr.make_df(105794, 106867, '064540')  # startpagenum, endpagenum, 종목코드
hob_df.to_csv('38현대엔지니어링.csv')