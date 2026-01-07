t=int(input())

for i in range(t):
    n,k=map(int,input().split())

    a=list(map(int,input().split()))
    b=list(map(int,input().split()))

    su=[]

    for j in range(n):
        if b[j]!=-1:
            su.append(a[j]+b[j])

    if su:
        if su[0]!=sum(su)/len(su):
            print(0)
            continue

        else:
            mn=min(a)
            mx=max(a)
            if mx<=mn+k and mx<=su[0]<=mn+k:
                print(1)
            else:
                print(0)



    else:
        mx=max(a)
        mn=min(a)
        if mx>mn+k:
            print(0)
        else:
            print(k+mn-mx+1)
