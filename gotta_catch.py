s=input()
l=7*[0]
for i in s:
    if i=="B":
        l[0]+=1
    elif i=='a':
        l[1]+=1
    elif i=='b':
        l[2]+=1
    elif i=='l':
        l[3]+=1
    elif i=='r':
        l[4]+=1
    elif i=='u':
        l[5]+=1
    elif i=='s':
        l[6]+=1
l[1]=l[1]//2
l[5]=l[5]//2
print(min(l))