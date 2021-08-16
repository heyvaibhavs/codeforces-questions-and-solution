l=[0,1]
j=1
sum=0
for i in range(20):
    l.append(l[j]+l[j-1])
    j=j+1
print(l[-1])    