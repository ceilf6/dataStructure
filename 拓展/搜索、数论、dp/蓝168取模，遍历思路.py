n,k=map(int,input().split())

n2=list(map(int,input().split()))

n3=[[0]*3 for i in range(k)]


n2.sort(reverse=True)  #题目要求和最大，那么数字大的优先取

ans=0 #别忘记初始化

'''
# 用于存储每个余数模 k 下最多三个最大的值
n3 = [[] for _ in range(k)]
for num in n2:
    mod = num % k
    if len(n3[mod]) < 3:  # 每个余数最多存储 3 个数
        n3[mod].append(num)
'''

for i in range(n):
    p=n2[i]%k
    if n3[p][0]:
        if n3[p][1]:
            if n3[p][2]:
                pass  #即便你不想在 if 条件下执行任何操作，也需要用 pass 占位符来保持语法正确。
            else:   #还有一个办法就是用if not
                n3[p][2]=n2[i]
        else:
            n3[p][1]=n2[i]
    else:
        n3[p][0]=n2[i]


for i in range(k):
    for j in range(k):
        q=(k-(i+j)%k)%k

        ans=max(ans,n3[i][0]+n3[j][i==j]+n3[q][(q==i)+(q==j)])#注意是p去比较

print(ans)
    
