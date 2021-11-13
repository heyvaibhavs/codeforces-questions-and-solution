# Code by : Sam._.072

s = input()
s1 = s[::-1]
h, i, c = 0, 0, 0
while i < len(s):
    if s1[i:i+5] == 'latem':
        c+=1
        i+=5
    elif s1[i:i+5] == 'yvaeh':
        h+=c
        i+=5
    else:
        i+=1
print(h)
