import bisect

n=int(input())

a=list(map(int,input().split()))

a.sort()

'''
summ=0
r=0
if a[0]==0:
    while r<n:
        i=r
        while i<n-1:#找空
            if a[i]!=a[i+1]-1:
                mex=a[i]+1
            i+=1
        if i==n-2:
            print(1)
            break
        r=bisect.bisect_right(a,mex)
        summ+=1


else:
    print(-1)
'''
'''
if a[0]!=0 and a[-1]!=0:
    print(-1)
elif a[0]==a[-1]:
    print(0)
else:
    summ=0
    while a[0]!=a[-1]:
        kong=-1
        for i in range(n-1):
            if a[i]!=a[i+1]-1 and a[i]!=a[i+1]:
                kong=a[i]+1
                break
        #print(a,kong)
        if kong==-1:
            summ+=1
            break
        else:
            for j in range(n):
                a[j]=max(0,a[j]-kong)
            summ+=1
    print(summ)
'''
if a[0]!=0 and a[-1]!=0:
    print(-1)
elif a[0]==a[-1]:
    print(0)
else:
    k=[]
    for i in range(n-1):
        if a[i]!=a[i+1]-1 and a[i]!=a[i+1]:
            for j in range(a[i]+1,a[i+1]):
                k.append(j)

    summ=0
    i=0
    while a[-1]>0 and i<len(k):
        for j in range(n):
            a[j]-=k[i]
        for z in range(i+1,len(k)):
            k[z]=k[z]-k[i]
        i+=1
    print(i+1)


        
    
