# file is not existed create anew file else  append the data

try:
    fname=input("Enter file name")
    f=open(fname,'x')#if file is present it executes the except 
    print("enter content")
    f.write(input())
    f=open(fname,'r')
    print('After reading')
    print(f.read())
except:
     f=open(fname,'a')
     print('enter content to append')
     f.write('\n'+input())
     f.close()
     f=open(fname,'r')
     print("After apending")
     print(f.read())
finally:
     f.close()