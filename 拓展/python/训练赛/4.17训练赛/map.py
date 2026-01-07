def find_matching_order(N, half_paper, M, scraps):
    # 利用map函数处理输入，转换成适合比较的数据
    half_paper_set = set(half_paper)  # 用集合提高查找效率

    scrap_segments = []
    for scrap in scraps:
        scrap_segments.append(tuple(scrap[1:]))  # 只提取高度信息

    # 先定义一个函数来找出匹配的碎纸条
    def match_scrap(scrap):
        for i in range(len(half_paper) - len(scrap) + 1):
            if half_paper[i:i + len(scrap)] == list(scrap):
                return i
        return -1

    # 通过map进行处理，返回每个纸条在半张纸中的匹配位置
    match_positions = list(map(match_scrap, scrap_segments))

    # 输出拼接顺序
    order = sorted(range(1, M + 1), key=lambda x: match_positions[x - 1])
    return order

# 输入处理部分
N = int(input())  # 半张纸的断口角点个数
half_paper = list(map(int, input().split()))  # 半张纸的折线高度

M = int(input())  # 碎纸条数量
scraps = [list(map(int, input().split())) for _ in range(M)]  # 每个碎纸条的折线角点

# 调用函数
result = find_matching_order(N, half_paper, M, scraps)

# 输出结果
print(' '.join(map(str, result)))
