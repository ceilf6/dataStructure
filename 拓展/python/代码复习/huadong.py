def f_max(F,k):
    q=deque()
    res=[]

    for cur in range(len(F)):
        while q and F[cur]>=F[q[-1]]:
            q.pop()
        q.append(cur)

        if cur-q[0]>=k:
            q.popleft()

        if cur>=k-1:
            res.append(F[q[0]])
            
    return res
