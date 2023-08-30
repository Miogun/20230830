from time import time, localtime, struct_time
from time import strftime, ctime, asctime, strptime

now = localtime(time())
print(asctime(now))
print(ctime(time()))
print(now.tm_year,'년')
print(localtime(time()))
print(strftime("%H시 %M분 %S초",now))
structTime = strptime('2023년 8월 30일 12시 10분 20초', '%Y년 %m월 %d일 %H시 %M분 %S초')
print(structTime)
# from myclass import MyThread
# import time

# myThread = MyThread()
# myThread.daemon = True
# myThread.start()

# i = 0
# while True:
#     if i >= 10:
#         break
#     i += 1
#     print(f"{i} 번째 실행")
#     time.sleep(1)

# # from datetime import datetime
# # from time import sleep

# # while True:
# #     print(datetime.now().strftime('%H시 %M분 %S초'))
# #     sleep