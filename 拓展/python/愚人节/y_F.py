n,m=map(int,input().split())

from collections import defaultdict

nums=defaultdict(int)

ans=defaultdict(list)

pop=defaultdict(list)

n=0
for i in range(n):
    sch,t,idd=map(int,input().split())

    if n<m*0.6 and nums[sch]<3:
        nums[sch]+=1
        n+=1
        ans.append((sch,t,idd))
    elif nums[sch]<3:
        pop.append((sch,t,idd))
'''
nb=int(input())

popb=[]
for i in range(nb):
    popb.append(input())

popc=[]

nc=int(input())
for i in range(nc):
    popc.append(input())

nbb=0
ncc=0
ansc=defaultdict(list)
for sch,t,idd in pop:
    if nbb<m*0.3 and sch in popb and nums[sch]<3:
        ans.append((sch,t,idd))

    if ncc<m*0.1 and sch in popc and nums[sch]<3:
        ansc.append((sch,t,idd))

ans=ans+ansc

print(ans)
'''
