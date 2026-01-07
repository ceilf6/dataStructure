def count_inversion(s):
    s = s.replace('.', '')
    nums = list(map(int, s))
    inv_count = 0
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] > nums[j]:
                inv_count += 1
    return inv_count

def is_solvable(start, end):
    inv_start = count_inversion(start)
    inv_end = count_inversion(end)
    return (inv_start % 2) == (inv_end % 2)


def get_neighbors(state):
    pos = state.index('.')
    neighbors = []
    # 上移
    if pos >= 3:
        lst = list(state)
        lst[pos], lst[pos - 3] = lst[pos - 3], lst[pos]
        neighbors.append(''.join(lst))
    # 下移
    if pos + 3 < 9:
        lst = list(state)
        lst[pos], lst[pos + 3] = lst[pos + 3], lst[pos]
        neighbors.append(''.join(lst))
    # 左移
    if pos % 3 != 0:
        lst = list(state)
        lst[pos], lst[pos - 1] = lst[pos - 1], lst[pos]
        neighbors.append(''.join(lst))
    # 右移
    if pos % 3 != 2:
        lst = list(state)
        lst[pos], lst[pos + 1] = lst[pos + 1], lst[pos]
        neighbors.append(''.join(lst))
    return neighbors



def bidirectional_bfs(start, end):
    if start == end:
        return 0
    from collections import deque
    queue_start = deque([start])
    queue_end = deque([end])
    visited_start = {start: 0}
    visited_end = {end: 0}
    while queue_start and queue_end:
        # 扩展较小的队列
        if len(queue_start) <= len(queue_end):
            level_size = len(queue_start)
            for _ in range(level_size):
                current = queue_start.popleft()
                for neighbor in get_neighbors(current):
                    if neighbor not in visited_start:#逐层扩散
                        visited_start[neighbor] = visited_start[current] + 1
                        queue_start.append(neighbor)
                        if neighbor in visited_end:
                            return visited_start[neighbor] + visited_end[neighbor]
        else:
            level_size = len(queue_end)
            for _ in range(level_size):
                current = queue_end.popleft()
                for neighbor in get_neighbors(current):
                    if neighbor not in visited_end:
                        visited_end[neighbor] = visited_end[current] + 1
                        queue_end.append(neighbor)
                        if neighbor in visited_start:
                            return visited_end[neighbor] + visited_start[neighbor]
    return -1

def main():
    start = input().strip()
    end = input().strip()
    if not is_solvable(start, end):
        print(-1)
        return
    print(bidirectional_bfs(start, end))

if __name__ == "__main__":
    main()
