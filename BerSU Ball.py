# Code by : Sam._.072

n = int(input())
boys = list(map(int, input().split()))
m = int(input())
girls = list(map(int, input().split()))
f = 101*[0]
for i in girls:
    f[i] += 1
c=0
boys.sort()
for i in boys:
    if i==1:
        if f[i]>0:
            c+=1
            f[i]-=1
        elif f[i+1]>0:
            c+=1
            f[i+1]-=1
    elif i==100:
        if f[i-1]>0:
            c+=1
            f[i-1]-=1
        elif f[i]>0:
            c+=1
            f[i]-=1
    elif f[i-1]>0:
        c+=1
        f[i-1]-=1
    elif f[i]>0:
        c+=1
        f[i]-=1
    elif f[i+1]>0:
        c+=1
        f[i+1]-=1
    # print(f)

print(c)