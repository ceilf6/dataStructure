n=int(input())

a=list(map(int,input().split()))


b=[]
b.append(6)
b.append(10)

for i in range(1,100):
    b.append(8*(i**2)-7*i+26)

print(b)

summ=n

for i in a:
    if i==1:
        summ=summ
    elif i%2==1:
        summ-=1
    elif i in b:
        summ-=1

print(summ)
