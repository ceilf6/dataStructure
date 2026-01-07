sc=[25,21,18,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0]

#print(len(sc))

N=int(input())

s=[[i,0] for i in range(30)]

# 不要输出为参赛的队伍！
vis=[0]*30

for _ in range(N):
    for __ in range(20):
        a,b=map(int,input().split())
        vis[a-1]=1
        s[a-1][1]+=sc[b-1]

s=sorted(s,key=lambda x:(x[1],-x[0]),reverse=True)
                    # 通过元组第二元素 - 实现同分数的小的前

#print(s)

for i in range(30):
    if not vis[s[i][0]]:
        continue #注意不是break！因为可能有人参加了但是是0分
    print(s[i][0]+1,s[i][1])
