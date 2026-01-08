def an():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    a = list(map(int, data[1:]))
    '''
    n=int(input())

    a=list(map(int,input().split()))
    '''
    a.sort()
    m = a[0]
    M = a[-1]
    if m == M:
        print(0, m)
        return

    low_k = 0
    high_k = M - m
    ans_k = high_k
    ans_x = M 
    
    while low_k <= high_k:
        mid_k = (low_k + high_k) // 2
        C = (mid_k + 1) // 2 #加
        D = mid_k // 2#减
        
        c_low = max(num - D for num in a)
        c_high = min(num + C for num in a)
        
        if c_low <= c_high:
            ans_k = mid_k
            ans_x = c_low
            high_k = mid_k - 1
        else:
            low_k = mid_k + 1
    
    print(ans_k, ans_x)

an()
