s=input()
h,m=int(s[:2]),int(s[3:])
l=[1,2,3,4,5,10,11,12,13,14,15,20,21,22,23]
r=[10,20,30,40,50,1,11,21,31,41,51,2,12,22,32]
for i in range(15):
    if h==23 and m>32:
        print(60-m)
        exit()
    elif l[i]==h and m<=r[i]:
        print(r[i]-m)
        exit()
    elif l[i]==h and m>r[i]:
        print((l[i+1]-h-1)*60+60-m+r[i+1])
        exit()
    elif h>=6 and h<=9:
        print((10-h-1)*60+60-m+1)
        exit()
    elif h>=16 and h<=19:
        print((20-h-1)*60+60-m+2)
        exit()