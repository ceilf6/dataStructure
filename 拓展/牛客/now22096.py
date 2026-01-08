while True:#题目要求有多次输入！！！
    try:
        n=int(input())
        '''
        for i in range(n+1):
            for j in range(i):
                print(j+1,end=' ')
            print()
        '''
        '''
        dp=[[0]*21 for _ in range(21)]
        dp[0][0]=1
        def dpp(n):
            for i in range(n-1):
                dp[n-1][i]=dp[n-2][i]
            dp[n-1][n-1]=dp[n-1][n-2]+1

        for i in range(n):
            dpp(i)

        print('\n'.join(' '.join(map(str, row)) for row in dp))
        '''
        # 初始化二维数组
        dp = [[0] * (i + 1) for i in range(n)]

        # 填充二维数组
        for i in range(n):
            for j in range(i + 1):
                dp[i][j] = j + 1

        # 打印数组
        output = '\n'.join(' '.join(map(str, row)) for row in dp)
        print(output)
    except:
        break

