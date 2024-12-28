# before deleting checknweather file is existed or not
import os
fname=input('enter file name')
if os.path.exists(fname):
 os.remove(fname)
 print('file is sucesfully deleted')
else:
 print('file does not exist')