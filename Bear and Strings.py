# Code by : Sam._.072

s = input()
a = []
i, n = 0, len(s)
while i < n:
    if s[i:i+4]=='bear':
        a.append(i+1)
        i+=4
    else:
        i+=1
if len(a) == 0:
    print(0)
    exit()
c = (n - (a[0]+2))*(a[0])
for i in range(1,len(a)):
    c += (a[i]-a[i-1])*(n-a[i]-2)
print(c)