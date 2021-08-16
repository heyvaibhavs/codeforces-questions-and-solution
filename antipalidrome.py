s=input()
if len(set(s))==1:
    print(0)
else:
    n=len(s)
    for i in range(n//2):
        if s[i]!=s[n-1-i]:
            print(len(s))
            exit()
    print(len(s)-1)