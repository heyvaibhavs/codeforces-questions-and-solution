# problem name : Ksenia and Pan Scales
# problem link : https://codeforces.com/problemset/problem/382/A
# Rating : 1100

s=input()
y=input()
c1=0
for i in s:
    if i != '|':
        c1 += 1
    else:
        break
c2=len(s)-c1-1
c3=len(y)
if c1 + c3 == c2:
    print(s[:c1]+y+s[c1:])
elif c1 == c2+c3:
    print(s+y)
else:
    c=len(s)+len(y)-1
    if c%2==0 and c1 <=c//2 and c2<=c//2:
        c=c//2
        x=s.index('|')
        if x < c:
            i=0
            s1=s[:x]
            while i < c-x:
                s1 += y[i]
                i+=1
        s2=s[x+1:] + y[i:]
        print(s1+"|"+s2)
    else:
        print("Impossible")