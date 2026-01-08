import sys
sys.setrecursionlimit(1000000)

n = int(input())
words = [input().strip() for _ in range(n)]
start_char = input().strip()

def get_overlap(pre, post):
    max_k = 0
    max_possible = min(len(pre), len(post)) - 1
    for k in range(max_possible, 0, -1):
        if pre[-k:] == post[:k]:
            max_k = k
            break
    return max_k

# 预处理pinum数组，保存增量（j的长度 - k）
pinum = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        k = get_overlap(words[i], words[j])
        if k > 0:
            pinum[i][j] = len(words[j]) - k
print(pinum)
max_len = 0

def dfs(last_idx, current_len, used):
    global max_len
    if current_len > max_len:
        max_len = current_len
    for j in range(n):
        if used[j] < 2 and pinum[last_idx][j] > 0:
            used[j] += 1
            dfs(j, current_len + pinum[last_idx][j], used)
            used[j] -= 1

# 遍历所有可能的起始单词
for i in range(n):
    if words[i][0] == start_char:
        used = [0] * n
        used[i] += 1
        dfs(i, len(words[i]), used.copy())

print(max_len)
