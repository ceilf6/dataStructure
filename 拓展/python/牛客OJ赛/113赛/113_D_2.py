n=int(input())

a=list(map(int,input().split()))
a.sort()
if a[0]==0 and a[0]!=a[-1]:
    z=0
    vis=[]
    for i in a:
        if i not in vis:
            vis.append(i)
            z+=1
    print(max(a)+2-z)
elif a[0]==0:#特判
    print(-1)
elif a[0]==a[-1]:
    print(0)
