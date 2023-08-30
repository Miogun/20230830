from myclass import Person
from pickle import load
import os.path

filepath = os.path.join('data','data.dat')
# POSIX filepath = 'data\data.dat'

try:
    p = [Person('홍길동', 20),Person('심청이',16)]
    with open(filepath,'wb') as fp:
        for person in p:
            dump(person, fp)
            # print(person.name, '을 파일에 저장하였습니다.')
        # dump(p,fp)
    print("객체 저장이 완료되었습니다.")
    
    # with open(filepath,'wb') as fp:
    #     for p in fp:
    #         persons.append(p)
    #     # while True:
    #     #     p = load(fp)
    #     #     persons.append(p)
            
except:
    print("모든 객체를 읽어 들였습니다.")
finally:
    print(persons)
            
            # try:
#     with open('data.txt','r',encoding='utf-8') as fp:
#         fp.write()
#     print(lines)
# except Exception as e:
#     print(e)

# # import sys

# lines = []
# # iter(lines) -> line.__iter__() -> list iterator
# try:
#     with open('data.txt','r',encoding='utf-8') as fp:
#         for line in fp:
#             lines.append(line)
#     print(lines)
#         # while True:
#         #     line = fp.readline()
#         #     if not line:
#         #         break
            
#         # for line in fp:
#         # fp로부터 fp.readline()을 수행하고
#         # 읽어들인 데이터가 있다면 라인에 저장하고
#         # for 블럭 수행
#         # 읽어들인 데이터가 없다면 for블록을 종료
#         # data = print(fp.read())
#     # fp = open("data.txt","a",encoding="utf-8")
#         # subject = '파이썬'
#         # print(f"{subject}는 쉬운가요?",file=fp)
#     # # fp.writelines("여기에 데이터를")
#     # fp.close()
#     # print(data)
# except Exception as e:
#     print(e)