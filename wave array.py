def countEleLessThanOrEqual(arr1,n1,arr2,n2):
    arr=arr1[:]
    arr1.sort()
    arr2.sort()
    l=[]
    for i in range(n1):
        l.append(0)
    j,c,i=0,0,0
    while i <n2:
        if arr2[i]<=arr1[j]:
            c+=1
            i+=1
        else:
            l[arr.index(arr1[j])]=c
            j+=1
    for i in range(j,n1):
        l[arr.index(arr1[i])]=c
    for i in l:
        print(i,end=" ")




arr1=[1,2,3,4,7,9]
arr2=[0,1,2,1,1,4]
countEleLessThanOrEqual(arr1,len(arr1),arr2,len(arr2))