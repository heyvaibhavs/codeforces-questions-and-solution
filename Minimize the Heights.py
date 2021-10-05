def getMinDiff(a, n, k):
    # code here
    a.sort()
    if a[-1]<=k:
        return a[-1]-a[0]
    x=min(a[0]+k,a[-1]-k)
    ans=9999999999
    for i in range(n-2,-1,-1):
        if a[i]<k:
            break
        x=min(x,a[i+1]-k)
        print(x,a[i]+k,ans)
        ans=min(ans,a[i]+k-x)
        print("ans=",ans)
    return ans

n,k=map(int, input().split())
a=list(map(int, input().split()))
print(getMinDiff(a, n, k))
