from collections import deque

def word_ladder(begin_word, end_word, word_list):
    """
    双向BFS解决单词接龙问题
    :param begin_word: 起始单词
    :param end_word: 目标单词
    :param word_list: 可用单词列表
    :return: 最短转换序列长度（无法转换返回0）
    """
    # 预处理：将单词列表转为集合提高查询效率
    word_set = set(word_list)
    if end_word not in word_set:
        return 0
    
    # 生成邻居的函数（核心逻辑）
    def get_neighbors(word):
        neighbors = []
        chars = list(word)
        for i in range(len(chars)):          # 遍历每个字符位置
            original = chars[i]
            for c in 'abcdefghijklmnopqrstuvwxyz':  # 尝试所有字母
                if c == original:
                    continue
                chars[i] = c
                new_word = ''.join(chars)
                if new_word in word_set:     # 检查是否合法
                    neighbors.append(new_word)
            chars[i] = original            # 恢复原始字符
        return neighbors
    
    # 双向BFS初始化
    visited_start = {begin_word: 1}        # 记录起点方向的单词和步数
    visited_end = {end_word: 1}            # 记录终点方向的单词和步数
    q_start = deque([begin_word])
    q_end = deque([end_word])
    
    while q_start and q_end:
        # 相遇检测（每次扩展前检查）
        intersection = visited_start.keys() & visited_end.keys()
        if intersection:
            return visited_start[intersection.pop()] + visited_end[intersection.pop()] - 1
        
        # 总是扩展较小的队列
        if len(q_start) <= len(q_end):
            # 处理起点方向的当前层
            for _ in range(len(q_start)):
                current = q_start.popleft()
                # 生成并处理邻居
                for neighbor in get_neighbors(current):
                    if neighbor not in visited_start:
                        visited_start[neighbor] = visited_start[current] + 1
                        q_start.append(neighbor)
        else:
            # 处理终点方向的当前层
            for _ in range(len(q_end)):
                current = q_end.popleft()
                # 生成并处理邻居（注意是反向搜索）
                for neighbor in get_neighbors(current):
                    if neighbor not in visited_end:
                        visited_end[neighbor] = visited_end[current] + 1
                        q_end.append(neighbor)
    
    # 没有找到连接路径
    return 0

# 测试案例
if __name__ == "__main__":
    # 示例1：标准案例
    begin = "hit"
    end = "cog"
    words = ["hot","dot","dog","lot","log","cog"]
    print(word_ladder(begin, end, words))  # 输出5（hit→hot→dot→dog→cog）

    # 示例2：无解情况
    begin = "hot"
    end = "dog"
    words = ["hot","dog"]
    print(word_ladder(begin, end, words))  # 输出0（无法转换）

    # 示例3：长路径
    begin = "charge"
    end = "comedo"
    words = ["changs","chants","chares","charge","charmed","charmer","charmed",
             "charter","hammed","hammel","hammer","hamper","camper","camped",
             "comped","combed","combee","combed","comber","combed","comedy","comedo"]
    print(word_ladder(begin, end, words))  # 输出9
