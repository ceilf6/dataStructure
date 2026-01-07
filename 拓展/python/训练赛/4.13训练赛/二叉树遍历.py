n=int(input())
a=list(map(int,input().split()))
b=[0]*n
x=0
def f(i):
    global x
    if i>=n:return
    f(i*2+1)
    f(i*2+2)
    b[i]=a[x]
    x+=1
    print(b)
f(0)
print(b)
