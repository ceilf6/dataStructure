n = int(input("输入元素的总个数 n: "))
m = int(input("输入要选择的元素个数 m: "))
a = list(range(1, n+1))  # 元素列表，例如 [1,2,3,4,5]

def dfs(start, path):
    # 当路径长度达到 m 时，输出结果
    if len(path) == m:
        print(" ".join(map(str, path)))
        return
    # 遍历从 start 到 n-1 的元素
    for i in range(start, n):
        # 选择当前元素 a[i]，并递归处理后续位置
        dfs(i + 1, path + [a[i]])

dfs(0, [])  # 从第0个元素开始，初始路径为空
