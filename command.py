import os

# result = os.system('ls -l')
# print(result)

linenum = 1
with os.popen('ls -l','r') as pp:
    for line in pp:
        encoded = line.encode(encoding='utf-8')
        decoded = encoded.decode(encoding='cp949')
        print("{:>3} : {}".format(linenum,line))
        linenum += 1
    # results = pp.read()

# print(results)

# linenum = 1
# for line in results:
#     print("{:>3} : {line}".format(linenum, line))
#     linenum += 1