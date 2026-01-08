T=input()

l=len(T)
le=0
for i in range(l):
    if T[i]=='1':
        le=i
        break
ri=l-1
for i in range(l-1,-1,-1):
    if T[i]=='1':
        ri=i
        break

T=T[le:ri+1]

#print(T)

l2=len(T)
T2=T[::-1]

#print(T2)

'''
t=int(T,2)^int(T2,2)
lt=len(T)
t=bin(t)[2:].zfill(lt)
print(t)
'''

lef=[]
rig=[]
'''
def expend(p,T):
    left=p
    right=p
    while left>=0 and right<len(T) and T[left]==T[right]:
        left-=1
        right+=1
    return left,right

for i in range(l2-1):
    left,right=expend(i,T)
    lef.append(left)
    rig.append(right)
'''
for i in range(l2-1):
    for j in range(l2-1,i,-1):
        if T[i:j+1]==T2[l2-j-1:l2-i]:
            lef.append(i)
            rig.append(j)



    
if lef:
    maxi=0
    maxl=rig[0]-lef[0]
    for i in range(1,len(lef)):
        if (rig[i]-lef[i])>maxl:
            maxl=rig[i]-lef[i]
            maxi=i

    DT=T[lef[maxi]:rig[maxi]+1]
#print(DT)

    LT=T[:lef[maxi]]+T[rig[maxi]+1:]

#print(LT)

    num=0
    num+=len(LT)
    num+=((DT.count('1')+1)//2)
    print(num)
else:
    print(T2.count('1'))

    
