from collections import deque

def f_max(F,k):
    q=deque()
    result=[]

    for cur in range(len(F)):
        while q and F[cur]>=F[q[-1]]:
            q.pop()

        q.append(cur)

        while q[0]<=cur-k:
            q.popleft()

        if cur>=k-1:
            result.append(F[q[0]])
    return result

print(f_max([1,3,2,4,5],3))
