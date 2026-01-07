n=int(input())
l=list(map(int,input().split()))

ans=[]
import bisect
def die(a,i):
    b=[]

    for j in range(i,n):
        if l[i]<a[-1]:
            a.append(l[j])
        else:
            if not b or l[j]>b[-1]:
                b.append(l[j])
            else:
                ans.append(a)
                idx=bisect.bisect_left(b,l[j])
                a=b[idx:]
    ans.append(a)
    ans.append(b)
    return ans

print(die([l[0]],1))
