# Code by : Sam._.072
import math
n, s = map(int, input().split())
if n==1 and s==0:
    print(0,0)
elif s>9*n or s<1:
    print(-1,-1)
else:
    x=''
    for i in range(s//9):
        x+='9'
    if s%9!=0:
        x+=str(s-(s//9)*9)
    if n==len(x):
        y=x[::-1]
        print(y,x)
    else:
        y=''
        t=len(x)
        while t<n:
            t+=1
            x+='0'
        z=0
        if x[-1]=='0':
            y+='1'
            for i in range(len(x)-2,-1,-1):
                if z==0 and x[i]!='0':
                    y+=chr(ord(x[i])-1)
                    z=-1
                else:
                    y+=x[i]
        else:
            y+=chr(ord(x[i])-1)
            for i in range(len(x)-2,-1,-1):
                y+=x[i]
        print(y,x)

                

