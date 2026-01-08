n,k,s=map(int,input().split())

st=[]
for i in range(n):
    st.append(list(map(int,input().split())))

st=sorted(st,key=lambda x:(x[0],x[1]))
key=[x[0] for x in st]
import bisect

idx=bisect.bisect_left(key,175)
st=st[idx:]

ans=0

for i in range(k):
    now=set()
    j=0
    while j<=len(st)-1:
        if st[j][0] not in now:
            ans+=1
            now.add(st[j][0])
            del st[j]
            j-=1
        else:
            if st[j][1]>=s:
                ans+=1
                del st[j]
                j-=1
        j+=1
    #print(now)



print(ans)

