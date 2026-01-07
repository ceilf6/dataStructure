def count_matrices(L, N):
    count = 0
    matrix = [[0]*N for _ in range(N)]
    row_sum = [0]*N
    col_sum = [0]*N

    def dfs(r, c):
        nonlocal count
        if r == N:
            if all(rs == L for rs in row_sum) and all(cs == L for cs in col_sum):
                count += 1
            return

        nr, nc = (r, c + 1) if c + 1 < N else (r + 1, 0)
        max_val = min(L - row_sum[r], L - col_sum[c])
        for val in range(max_val + 1):
            matrix[r][c] = val
            row_sum[r] += val
            col_sum[c] += val
            if row_sum[r] <= L and col_sum[c] <= L:
                dfs(nr, nc)
            row_sum[r] -= val
            col_sum[c] -= val

    dfs(0, 0)
    return count


ans=[[0]*3 for i in range(8)]

for i in range(2,10):
    for j in range(2,5):
        ans[i-2][j-2]=count_matrices(i,j)
print(ans)
