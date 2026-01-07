n=int(input())

a=list(map(int,input().split()))

import bisect as bi

def f(pos):
    value=a[pos]

    i=pos+1

    summ=0
    flag=2
    while i<len(a):
        if flag==2:
            if a[i]>value:
                summ+=a[i]
                flag=3
        else:
            if a[i]<value:
                summ+=a[i]
                flag=2
        i+=1
    print(summ,end=' ')

for i in range(len(a)):
    f(i)
