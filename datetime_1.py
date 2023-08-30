# from datetime import datetime

# strtime = datetime.now().strftime('%Y년 %m월 %d일')
# # %H시 %M분 %S초
# print(strtime)

from datetime import datetime, timedelta

afterdatetime = datetime.now() + timedelta(days=100, seconds=0)

print(afterdatetime.strftime('%Y년 %m일 %d일'))

# '2023년 8월 21일 12시 30분 35초'

# timedelta를 사용한 시간 구하기의 단점은 날짜와 초 단위로만
