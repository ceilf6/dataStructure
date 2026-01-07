def count_game_paths(n, m, A):
    from functools import lru_cache
    
    # 记忆化搜索
    @lru_cache(None)
    def dfs(round, energy, height):
        if round == n or energy == 0:
            return {(round, height)}  # 记录游戏终止时的回合和高度
        
        results = set()
        for c in range(1, energy + 1):  # C_i 至少为1，最多为当前剩余能量
            new_height = height + A[round] * c
            results |= dfs(round + 1, energy - c, new_height)
        
        return results

    paths = dfs(0, m, 0)
    return len(paths)  # 统计所有不同的路径数

# 示例输入
n = 9
m = 15
A = [3,2, 5, 7, 1, 4, 6, 8, 3]  # 每一回合的小蓝状态值

# 计算不同路径数
print(count_game_paths(n, m, A))
