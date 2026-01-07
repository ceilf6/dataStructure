n=int(input())

yanse=list(map(int,input().split()))

q=int(input())
for i in range(q):
    flag=1
    l=list(map(int,input().split()))
    for i in range(n):
        if l[i]!=0:
            if l[i]!=yanse[i]:
                flag=0;break
    if flag:
        print("Da Jiang!!!")
    else:
        print("Ai Ya")
