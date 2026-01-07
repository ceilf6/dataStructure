N=int(input())

l=list(map(int,input().split()))

n=int(input())

# 排序：信息利用率

for i in range(1,N+1):
    l[i-1]=[l[i-1],i]
#print(l)

l=sorted(l,key=lambda x:(x[0],-x[1]),reverse=True)

for i in range(n):
    print(l[i][1],end=' ')
