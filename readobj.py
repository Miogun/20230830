from myclass import Person
from pickle import load
import os.path

persons = []
try:
    with open('data\data.txt','rb') as fp:
        for p in fp:
            persons.append(p)
        # while True:
        #     p = load(fp)
        #     persons.append(p)
            
except:
    print("모든 객체를 읽어 들였습니다.")
finally:
    print(persons)
            