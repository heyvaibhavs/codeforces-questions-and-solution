# problem name : Mr. Kitayuta's Gift
# problem link : https://codeforces.com/problemset/problem/505/A
# Rating : 1100

def palindrome(s):
    i=0
    j=len(s)-1
    while i < j :
        if s[i]!=s[j]:
            return False
        i+=1
        j-=1
    return True

s=input()
i,j=0,len(s)-1
z=0
n=len(s)
while i < j:
    # print(i,j)
    if s[i]!=s[j]:
        if palindrome(s[i+1:j+1]):
            s=s[:j+1]+s[i]+s[j+1:]
            z=-1
        elif palindrome(s[i:j]):
            s=s[:i]+s[j]+s[i:]
            z=-1
        else:
            z=2
        break
    i+=1
    j-=1

# print(z)
if z==0:
    if n%2==0:
        print(s[:n//2]+"x"+s[n//2:])
    else:
        print(s[:n//2]+s[n//2]+s[n//2:])
elif z==2:
    print("NA")
else:
    print(s)