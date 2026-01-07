n=int(input())

a=list(map(int,input().split()))

a.sort()
if a[0]==a[-1]:
    print(0,a[0])

avi=n//2
summ=0
l=0
r=n-1

while a[0]!=a[-1]:
    #av=a[avi]
    av=sum(a)//n

    for i in range(n):
        if a[i]>av:
            k=i
            break
    #m=(l+r)//2

    jia=av-a[k-1]
    jian=a[k]-av
    '''
    for i in range(n//2):
        if a[avi-i]<av:
            jia=av-a[avi-k1]
            print(jia)
            k1=i
            break
    for i in range(1,n//2):
        if a[avi+i]>av:
            k2=i
            jian=a[avi+k2]-av
            print(jian)
            break
    '''

    d=min(jia,jian)
    summ+=d

    for i in range(k):
        a[i]+=d



    for i in range(k,n):
        a[i]-=d


    a.sort()

    if a[0]==av:
        d+=a[-1]-av
        print(d,a[0])
    elif a[-1]==av:
        d+=av-a[0]
        print(d,a[-1])

    

    
