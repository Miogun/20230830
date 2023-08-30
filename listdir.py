import os
import os.path

dir = os.path.join('.')
print(dir)

files = os.listdir(dir)
print(files)

for file in files:
    current = os.path.join(dir, file)
    typename = 'FILE' if os.path.isfile(current) else 'DIR'
    # typename = 'FILE'
    # if not os.path.isfile(os.path.join(dir,file)):
    #     typename = 'DIR'

    #     typename = 'FILE'
    # else:
    #     typename = 'DIR'    
    size = str(os.path.getsize(current)) + 'B'
    abspath = os.path.abspath(current)
    print("{:<4} {:<10} {}".format(typename, size, abspath))


    