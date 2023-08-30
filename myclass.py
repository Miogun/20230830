from threading import Thread
from datetime import datetime
from time import sleep

class MyThread(Thread):
    def run(self):
        while True:
            print(datetime.now().strftime('%H시 %M분 %S초'))
            sleep(1)



# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#     #     pass
#         return f"__str__ : 이름: {self.name}, 연령 : {self.age}"   
#     def __repr__(self):
#         return f"Person('{self.name},{self.age})"       
#         # return f"__repr__ : 이름: {self.name}, 연령 : {self.age}"

# # value = eval('10 * 20')
# # print(value)    
# # p = Person('홍길동',20)

# # p1 = eval(p.__repr__())

# # print(id(p1))

# # a = int(10)
# # print(type(a))
# # print(isinstance(a,int))