def count_matrices(L, N):
    count = 0
    row_sum = [0] * N
    col_sum = [0] * N

    def dfs(r, c):
        nonlocal count
        if r == N:
            count += 1
            return

        # Calculate next position
        if c + 1 < N:
            nr, nc = r, c + 1
        else:
            nr, nc = r + 1, 0

        # Check if current cell is the last in its row or column
        if c == N - 1:  # Last in row
            required_val = L - row_sum[r]
            if required_val < 0 or col_sum[c] + required_val > L:
                return
            original_row = row_sum[r]
            original_col = col_sum[c]
            row_sum[r] += required_val
            col_sum[c] += required_val
            dfs(nr, nc)
            row_sum[r] = original_row
            col_sum[c] = original_col
        elif r == N - 1:  # Last in column
            required_val = L - col_sum[c]
            if required_val < 0 or row_sum[r] + required_val > L:
                return
            original_row = row_sum[r]
            original_col = col_sum[c]
            row_sum[r] += required_val
            col_sum[c] += required_val
            dfs(nr, nc)
            row_sum[r] = original_row
            col_sum[c] = original_col
        else:
            max_val = min(L - row_sum[r], L - col_sum[c])
            for val in range(max_val + 1):
                row_sum[r] += val
                col_sum[c] += val
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
