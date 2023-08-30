import os
import os.path

dir = os.path.join('.','data')
# if not os.path.exists(dir):
try:
    os.mkdir(dir)
except:
    pass
