import heapq

def nth(s,n):
    hq=[1]
    heapq.heapify(hq)
    vis=set()
    vis.add(1)

    count=0
    while hq:
        cur=heapq.heappop(hq)

        count+=1
        if count==n:
            return cur

        for p in s:
            nex=cur*p
            if nex not in vis:
                vis.add(nex)
                heapq.heappush(hq,nex)

s=[3,7,17,29,53]
n=20220
print(nth(s,n))
