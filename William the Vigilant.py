# Code by : Sam._.072

n, q = map(int, input().split())
s = input()
z = s.count('abc')
s = list(s)
for _ in range(q):
    t = input().split()
    i , c = int(t[0])-1,t[1]
    for j in range(max(0,i-2),i+1):
        if s[j:j+3]==['a','b','c']:
            z -= 1
    s[i] = c
    for j in range(max(0,i-2),i+1):
        if s[j:j+3]==['a','b','c']:
            z += 1
    print(z)



    
    

