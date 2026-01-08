n=int(input())

a=[0]*n
b=[0]*n
c=[[0,i] for i in range(n)]

for i in range(n):
    a[i],b[i]=map(int,input().split())
    c[i][0]=a[i]-b[i]

c2=sorted(c,key=lambda x:x[0])


mu=[]
nn=0
for i in range(len(c2)-1,-1,-1):
    mu.append(c2[i][1])
    nn+=1
    if nn==n//2:
        break

summ=0
#print(mu)

for i in range(len(a)):
    if i in mu:
        summ+=a[i]
        #print(a[i])
    else:
        summ+=b[i]
        #print(b[i])

print(summ)
