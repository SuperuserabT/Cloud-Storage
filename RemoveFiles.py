import os
import time
import shutil

path = input('Enter the name of the directory to be deleted.')

time.time()
os.path.exists(path)
os.walk(path)
os.path.join(path, 'RemoveFiles.py')
os.stat(path)


ctime = os.stat(path).st_ctime

if ctime > 500000000:
    os.remove(path)

return ctime