t=int(input())

for i in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))

    su=[]

    for j in range(n):
        if b[j]!=-1:
            su.append(a[j]+b[j])
            
    if su:
        if su[0] != sum(su) / len(su):
            print(0)
            continue
        # 已确定target，逐个检验缺失的b是否能填出合法值
        target = su[0]
        for j in range(n):
            if b[j] == -1:
                candidate = target - a[j]
                if candidate < 0 or candidate > k:
                    print(0)
                    break
        else:
            print(1)
    
    else:
        mx = max(a)
        mn = min(a)
        if mx > mn + k:
            print(0)
        else:
            print(max(0,k + mn - mx + 1))
