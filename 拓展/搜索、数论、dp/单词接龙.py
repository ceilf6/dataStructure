from collections import deque

def bidirectional_bfs(start, target, get_neighbors):
    """
    双向BFS模板
    :param start: 起始状态
    :param target: 目标状态
    :param get_neighbors: 函数，输入状态返回相邻状态列表
    :return: 最短路径长度（找不到返回-1）
    """
    if start == target:
        return 0
    
    # 初始化双队列和访问字典
    visited_start = {start: 0}  # 记录起点方向各状态的步数
    visited_end = {target: 0}   # 记录终点方向各状态的步数
    queue_start = deque([start])
    queue_end = deque([target])
    
    while queue_start and queue_end:
        # 选择较小的队列进行扩展（优化搜索效率）
        if len(queue_start) <= len(queue_end):
            # 处理起点方向的队列
            for _ in range(len(queue_start)):
                current = queue_start.popleft()
                current_step = visited_start[current]
                
                # 生成相邻状态
                for neighbor in get_neighbors(current):
                    if neighbor not in visited_start:
                        visited_start[neighbor] = current_step + 1
                        queue_start.append(neighbor)
                        
                        # 相遇检测
                        if neighbor in visited_end:
                            return visited_start[neighbor] + visited_end[neighbor]
        else:
            # 处理终点方向的队列
            for _ in range(len(queue_end)):
                current = queue_end.popleft()
                current_step = visited_end[current]
                
                # 生成相邻状态
                for neighbor in get_neighbors(current):
                    if neighbor not in visited_end:
                        visited_end[neighbor] = current_step + 1
                        queue_end.append(neighbor)
                        
                        # 相遇检测
                        if neighbor in visited_start:
                            return visited_start[neighbor] + visited_end[neighbor]
    
    return -1  # 未找到路径


def get_nei(word):
    neis=[]
    for i in range(len(word)):
        nword=word.copy()
        for j in range(97,123):
            if chr(j)!=word[i]
                nword.replace(word[i],chr(j),1)
            if nword in words:
                neis.append(nword)
    return neis







# 实现相邻节点生成函数
def get_word_neighbors(word):
    """生成所有只差一个字母的有效单词"""
    neighbors = []
    chars = list(word)
    for i in range(len(chars)):
        original = chars[i]
        for c in 'abcdefghijklmnopqrstuvwxyz':
            if c != original:
                chars[i] = c
                new_word = ''.join(chars)
                if new_word in valid_words:  # 假设valid_words是有效单词集合
                    neighbors.append(new_word)
        chars[i] = original
    return neighbors

# 调用双向BFS
shortest_path = bidirectional_bfs(
    start = "hit",
    target = "cog",
    get_neighbors = get_word_neighbors
)
