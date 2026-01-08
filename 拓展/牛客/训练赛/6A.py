n,a,b,c=map(int,input().split())

summ=0
while 1:
    if n>=a:
        n-=a
        summ+=1
    elif n>=b:
        n-=b
        summ+=1
    elif n>=c:
        n-=c
        summ+=1
    else:
        break

print(summ)
