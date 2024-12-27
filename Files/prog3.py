import os
try:
    fname=input("enter file name")
    f=open(fname,'r')
    print(f.read())
    f.close()
    f=open(fname,'r')
    print(f.read(10))
    f.close()
    f=open(fname,'r')
    i=1
    for x in f:
        print(str(i)+x)
        i=i+1
        os.remove(fname)
except:
    print('selected file not esist')        
