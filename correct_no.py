n=input()
m=input()
if len(m)==len(n):
    f=10*[0]
    for i in n:
        f[ord(i)-48]+=1
    s=""
    for i in range(1,10):
        if f[i]>0:
            s+=str(i)
            f[i]-=1
            break
    for i in range(10):
        for j in range(f[i]):
            s+=str(i)
    if m==s:
        print("OK")
    else:
        print("WRONG_ANSWER")
else:
    print("WRONG_ANSWER")