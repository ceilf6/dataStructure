T=int(input())

for i in range(T):
    n,m=map(int,input().split())

    s=input()
    t=input()

    l=[]
    r=[]

    for i in range(n-m+1):
        if s[i]==t[0]:
            flag=1
            for j in range(1,m):
                if s[i+j]!=t[j]:
                    flag=0
                    break
            if flag:
                l.append(i)
                r.append(i+m)

    #print(l)
    ans=0

    i=0

    while i<len(l):
        for j in range(i+1,len(l)):
            if l[j]-l[i]>=m:
                ans+=1
                i=j
                break
        else:
            ans+=1
            break
        

    print(ans)
