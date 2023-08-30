from myclass import Person
from pickle import dump 

try:
    p = [Person('홍길동', 20),Person('심청이',16)]
    with open('data.txt','wb') as fp:
        for person in p:
            dump(person, fp)
            # print(person.name, '을 파일에 저장하였습니다.')
        # dump(p,fp)
    print("객체 저장이 완료되었습니다.")
except Exception as e:
    print(e)
        