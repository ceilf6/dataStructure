n=int(input())
l=list(map(int,input().split()))

a=[l[0]]
b=[]
ans=[]
for i in range(1,n):
    if l[i]<a[-1]:
        a.append(l[i])
    else:
        if not b or l[i]>b[-1]:
            b.append(l[i])
        else:
            ans.append(a)
            a=[]
            while b and b[-1]>l[i]:
                a.append(b.pop())
            a.append(l[i])

ans.append(a)
ans.append(b)

maxx=0
for i in range(len(ans)):
    if len(ans[i])>maxx:
        maxx=len(ans[i])
print(len(ans),maxx)
