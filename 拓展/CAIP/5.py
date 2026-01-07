N=int(input())

ma=[]

for i in range(N):
    ma.append(list(map(int,input().split())))

# 注意题目说明了：贪心就好了：找当前地图中最大的矩形：二维滑动窗口？
# 注意坐标是从 1 开始的，切横着是 x
# 每次清完上面的会掉下来，然后上面空缺的会用黑洞弥补

# 从左上往右下走？这点从分数相当时的矩形选择就可以感觉到

def fmax():
    max_score = 0
    best_rect = (0, 0, 0, 0)
    
    # 遍历所有可能的矩形
    for x1 in range(N):
        for y1 in range(N):
            for x2 in range(x1, N):
                for y2 in range(y1, N):
                    # 检查矩形内是否有黑洞
                    has_black_hole = False
                    score = 0
                    
                    for i in range(x1, x2 + 1):
                        for j in range(y1, y2 + 1):
                            if ma[j][i] == 0:  # 黑洞
                                has_black_hole = True
                                break
                            score += ma[j][i]
                        if has_black_hole:
                            break
                    
                    # 如果有黑洞，分数为0
                    if has_black_hole:
                        score = 0
                    
                    # 更新最大分数，按照题目要求的优先级
                    if score > max_score or (score == max_score and 
                        (x1 < best_rect[0] or 
                         (x1 == best_rect[0] and y1 < best_rect[1]) or
                         (x1 == best_rect[0] and y1 == best_rect[1] and x2 < best_rect[2]) or
                         (x1 == best_rect[0] and y1 == best_rect[1] and x2 == best_rect[2] and y2 < best_rect[3]))):
                        max_score = score
                        best_rect = (x1, y1, x2, y2)
    
    return best_rect[0], best_rect[1], best_rect[2], best_rect[3], max_score

def eliminate_and_fall(x1, y1, x2, y2):
    """消除矩形并让上方方块掉落"""
    # 消除矩形内的方块
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            ma[j][i] = 0
    
    # 让上方方块掉落
    for i in range(x1, x2 + 1):
        # 从下往上移动方块
        for j in range(y2, -1, -1):
            # 找到上方最近的非零方块
            for k in range(j - 1, -1, -1):
                if ma[k][i] != 0:
                    ma[j][i] = ma[k][i]
                    ma[k][i] = 0
                    break
            else:
                # 如果上方没有方块了，用黑洞填补
                ma[j][i] = 0

total_score = 0

while True:
    x1, y1, x2, y2, res = fmax()
    if res <= 0:
        break
    print(f'({x1+1}, {y1+1}) ({x2+1}, {y2+1}) {res}')
    total_score += res
    eliminate_and_fall(x1, y1, x2, y2)

print(total_score)
