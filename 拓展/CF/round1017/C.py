from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]

    p = [0] * (2 * n + 1)

    for k in range(2, 2 * n + 1):  #枚举对角线编号
        counter = Counter()
        # i + j == k - 2 
        for i in range(n):
            j = k - i - 2
            if 0 <= j < n:
                counter[grid[i][j]] += 1
        if counter:  # 确保有元素再取众数
            p[k] = counter.most_common(1)[0][0]

    p=p[2:]
    
    q=[i for i in range(1,2*n+1)]

    for j in q:
        if j not in p:
            print(j,end=' ')

    print(' '.join(map(str,p)))
