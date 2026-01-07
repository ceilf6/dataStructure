from collections import defaultdict

n,m=map(int,input().split())

d=defaultdict(int)

for i in range(n):
    l=list(map(int,input().split()))
    d[tuple(l)]+=1#list不可作为键，转为元组
'''
d=sorted(d.items(),key=lambda x:(x[1],-sum(x[0])))#对items[1]即value进行排序
                                    #如果相同那么看key
                                    #因为要降序所以要-,且是元组，得sum
'''
d=sorted(d.items(),key=lambda x:(-x[1],x[0]))

print(len(d))
'''
for i in range(-1,-len(d)-1,-1):
    print(d[i][1],*d[i][0])
'''
for a,b in d:
    print(b,*a)

