n=int(input())
if n%7>=2:
    x=2
else:
    x=n%7
if n%7>=6:
    y=n%7-5
else:
    y=0
z=(n//7)*2
print(z+y,z+x)