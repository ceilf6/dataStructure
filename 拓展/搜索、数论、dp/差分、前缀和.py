n=int(input("输入数的个数"))

print("输入%d个数，每个数用空格区分"%(n))

a=list(map(int,input().split()))

print("输入第几个数到第几个数增加多少")

l,r,x=map(int,input().split())

d=[0]*n
d[0]=a[0]

for i in range(1,n):
    d[i]=a[i]-a[i-1]

d[l-1]+=x
if r<n:
    d[r]-=x


s=[0]*n
s[0]=d[0]

for j in range(1,n):
    s[j]=s[j-1]+d[j]

for k in range(n):
    print(s[k])
