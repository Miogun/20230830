import os
# print(os.environ)
# env = os.environ

# for key in os.environ:
#     print(key)
    
# print(*os.environ)

# for key, value in os.environ.items():
#     print("{:<30} : {}".format(key,value))
    
print(os.environ['PATH'])
# if 'AAA' in os.environ:
try:
    print(os.environ['AAA'])
except:
    pass