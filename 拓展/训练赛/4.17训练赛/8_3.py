from collections import defaultdict

n,k,s=map(int,input().split())
group=defaultdict(list)

for _ in range(n):
    t,p=map(int,input().split())
    if t>=175:
        group[t].append(p)

# 排序所有组内 PAT 分数，按升序
for score in group:
    group[score].sort()
    
#print(group)

# 所有分数从小到大
ssc=sorted(group.keys())
ans=0

#print(ssc)

ls=len(ssc)
for i in range(k):
    now=set()
    for j in range(ls):
        print(ssc[j])
        if group[ssc[j]]:
            ans+=1
            del group[ssc[j]][0]
        '''
        for z in range(-1,-len(group[ssc[j]])-1,-1):
        '''
        z=-1
        while z>=-len(group[ssc[j]]):
            if group[ssc[j]][z]>=s:
                ans+=1
                del group[ssc[j]][z]
                z+=1
            else:
                break
            z-=1





'''    
for _ in range(k):
    for score in sorted_scores:
        if not group[score]:
            continue
        # 每批最多先推荐一人（无论 pat 是否达标）
        ans+=1
        group[score].pop(0)
        # 然后额外推荐所有 pat 达标的（直到遇到不达标为止，因为是升序）
        while group[score] and group[score][0]>=s:
            group[score].pop(0)
            ans+=1
'''
print(ans)
