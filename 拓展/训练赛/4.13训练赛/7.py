a1,a2,n=map(int,input().split())

q=[a1,a2]

now=1
while len(q)<n:
    new=q[now-1]*q[now]

    if new>=10:
        qnew=[]
        while new:
            qnew=[new%10]+qnew
            new//=10
    else:
        qnew=[new]
    q=q+qnew
    now+=1


for i in range(n-1):
    print(q[i],end=' ')

print(q[n-1])
