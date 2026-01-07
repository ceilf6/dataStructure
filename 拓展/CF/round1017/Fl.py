def solve():
    t = int(input()) 
    for _ in range(t):
        n, m, k = map(int, input().split()) 
        grid = [[0] * m for _ in range(n)]  
        

        num = 1  
        for i in range(n):
            for j in range(m):
                grid[i][j] = num
                num += 1
                if num > k:  
                    num = 1
        

        for row in grid:
            print(" ".join(map(str, row)))

solve()
