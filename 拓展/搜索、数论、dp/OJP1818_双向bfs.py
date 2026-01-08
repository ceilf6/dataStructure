from collections import deque

primes = {2, 3, 5, 7, 11, 13, 17}

def count_i(s):
    inv = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] > s[j]:
                inv += 1
    return inv

def get_neighbors(state):
    neighbors = []
    state_list = list(state)
    for i in range(9):
        row, col = i // 3, i % 3
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = row + dr, col + dc
            if 0 <= nr < 3 and 0 <= nc < 3:
                j = nr * 3 + nc
                a, b = int(state[i]), int(state[j])
                if (a + b) in primes:
                    new_state = state_list.copy()
                    new_state[i], new_state[j] = new_state[j], new_state[i]
                    neighbor = ''.join(new_state)
                    neighbors.append(neighbor)
    return neighbors

def bidirectional_bfs(start, target):
    if start == target:
        return 0
    visited_start = {start: 0}
    visited_end = {target: 0}
    queue_start = deque([start])
    queue_end = deque([target])
    
    while queue_start and queue_end:
        if len(queue_start) <= len(queue_end):
            current_level = list(queue_start)
            queue_start.clear()
            for state in current_level:
                current_steps = visited_start[state]
                for neighbor in get_neighbors(state):
                    if neighbor not in visited_start:
                        visited_start[neighbor] = current_steps + 1
                        queue_start.append(neighbor)
                        if neighbor in visited_end:
                            return visited_start[neighbor] + visited_end[neighbor]
        else:
            current_level = list(queue_end)
            queue_end.clear()
            for state in current_level:
                current_steps = visited_end[state]
                for neighbor in get_neighbors(state):
                    if neighbor not in visited_end:
                        visited_end[neighbor] = current_steps + 1
                        queue_end.append(neighbor)
                        if neighbor in visited_start:
                            return visited_end[neighbor] + visited_start[neighbor]
    return -1

T = int(input())
target_state = '123456789'
inv_target = count_i(target_state)
for _ in range(T):
    initial = []
    for _ in range(3):
        initial.extend(input().strip().split())
    initial = ''.join(initial)
    inv_initial = count_i(initial)
    if (inv_initial % 2) != (inv_target % 2):
        print(-1)
    else:
        print(bidirectional_bfs(initial, target_state))
