# 看到就觉得是完全背包，但是其实根本不用！！

n=int(input())

cnt=0
i=0
r=[13,7,3,1]
while n:
    d=n//r[i]
    #i+=1
    cnt+=d
    n=n%r[i]
    i+=1

print(cnt)
