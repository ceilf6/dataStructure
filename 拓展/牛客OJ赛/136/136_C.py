n,m=map(int,input().split())
s=input()
c=list(map(int,input().split()))

up=[]
for i in range(n-1):
    if s[i]<s[i+1]:
        up.append(i+1)

#print(up)

last=0
di=0
flag=0
ans=s
for i in up:
    if flag:
        break
    c2=sorted(c[last:i])
    #print(c2)
    a=s[i-1]
    for j in range(last,i):#前缀和？
        if c2[j-last]>m:
            flag=1
            break
        ans=ans[:j+di]+a+ans[j+di:]
        di+=1
        m-=c2[j-last]
    last=i+1


print(ans)




n,m=map(int,input().split())
s=input()
a=list(map(int,input().split()))
re=[]
i=0
while i<n:
    j=i+1
    while j<n and s[i]==s[j]:
        j+=1
    for k in range(i,j):
        if j<n and s[k]<s[j] and m>=a[k]:
            m-=a[k]
            re.append(s[k]*2)
        else:
            re.append(s[k])
    i=j
print(''.join(re))
            
