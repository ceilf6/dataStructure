from collections import deque
from collections import defaultdict

edges = defaultdict(list)

n = int(input())
for _ in range(n):
    a, a_flag, b, b_flag = input().split()
    a_flag = int(a_flag)
    b_flag = int(b_flag)
    edges[(a, a_flag)].append((b, b_flag))

shortest_path = None

# Collect all possible nodes
nodes = set()
for key in edges:
    nodes.add(key[0])
    for b, _ in edges[key]:
        nodes.add(b)
nodes = list(nodes)

# Iterate all possible starting nodes and states to find the shortest cycle
for start_node in nodes:
    for start_state in [0, 1]:
        target_state = 1 - start_state
        visited = {}
        queue = deque()
        # Each element: (current_node, current_state, path_edges)
        queue.append((start_node, start_state, []))
        visited[(start_node, start_state)] = True
        found = False
        while queue and not found:
            current_node, current_state, path_edges = queue.popleft()
            # Check if current node and state is the target
            if current_node == start_node and current_state == target_state:
                if shortest_path is None or len(path_edges) < len(shortest_path):
                    shortest_path = path_edges
                found = True
                break
            # Explore all possible edges from current state
            for (next_node, next_state) in edges.get((current_node, current_state), []):
                if (next_node, next_state) not in visited:
                    visited[(next_node, next_state)] = True
                    new_path = path_edges + \
                        [(current_node, current_state, next_node, next_state)]
                    queue.append((next_node, next_state, new_path))
        if found and len(shortest_path) == 0:
            break  # shortest possible path found
    if shortest_path and len(shortest_path) == 0:
        break  # shortest possible is 0 edges (impossible per problem statement)

# Construct the output
output_steps = []
for step in shortest_path:
    a, a_flag, b, b_flag = step
    output_steps.append(f"{a} {a_flag} {b} {b_flag}")

start_node = shortest_path[0][0]
start_state = shortest_path[0][1]
end_state = 1 - start_state

print(f"{' '.join(output_steps)} = {start_node} {start_state} {start_node} {end_state}")
