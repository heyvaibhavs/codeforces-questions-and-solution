# problem name : Who's Sentence is it ?
# problem link : https://codeforces.com/problemset/problem/312/A
# Rating : 1100

n=int(input())
for i in range(n):
    s=input()
    s1=s[-5:]
    s2=s[:5]
    if s1=='lala.' and s2!='miao.':
        print("Freda's")
    elif s1!='lala.' and s2=='miao.':
        print("Rainbow's")
    else:
        print("OMG>.< I don't know!")


