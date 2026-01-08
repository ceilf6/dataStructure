n=int(input())

a=list(map(int,input().split()))

b=[]
su=3
for i in range(3,10**3):
    su+=i
    if su%2==0:
        b.append(su)

summ=n
for i in a:
    if i==1:
        i=i
    elif i%2==1:
        summ-=1
    else:
        if i in b:
            summ-=1

print(b)
