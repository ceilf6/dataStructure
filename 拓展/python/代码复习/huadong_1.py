from collections import deque

def f_max(listt,k):
    q=deque()

    result=[]

    for cur in range(len(listt)):
        while q and listt[cur]>=listt[q[-1]]:
            q.pop()
        q.append(cur)


        while q[0]<=cur-k:
            q.popleft()

        if cur>=k-1:
            result.append(listt[q[0]])
            
    return result

listt=list(map(int,input().split()))
k=int(input())

print(f_max(listt,k))
