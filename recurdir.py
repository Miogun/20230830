from os import walk
from os.path import isfile, getsize, abspath, join

dir = join('.')
files = walk(dir)
# print(files)

for root, dirs, files in files:
    print(abspath(join(root)))
    for file in files:
        print("디렉토리 : {} , 파일 경로 : {}".format(dir,abspath(join(root,file))))
