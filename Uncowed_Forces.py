m=list(map(int,input().split()))
w=list(map(int,input().split()))
y,z=map(int,input().split())
c,x=0,[500,1000,1500,2000,2500]
for i in range(5):
    c+=max(0.3*x[i],(1-m[i]/250)*x[i]-50*w[i])
c+=y*100 - z*50
print(int(c))

