def water_jug_dfs():
    from collections import deque
    capacity_x = int(input("Enter the capacity of jug 1:"))
    capacity_y = int(input("Enter the capacity of jug 2:"))
    initial_state = (0, 0)
    goal_state = (lambda x: (x, 2))
    stack = [initial_state]
    visited = set()
    visited.add(initial_state)
    parent = {initial_state: None}
    def get_neighbors(state):
        a, b = state
        neighbors = []
        neighbors.append((capacity_x, b))  
        neighbors.append((a, capacity_y))  
        neighbors.append((0, b))  
        neighbors.append((a, 0))
        transfer_to_y = min(a, capacity_y - b)
        neighbors.append((a - transfer_to_y, b + transfer_to_y))
        transfer_to_x = min(b, capacity_x - a)
        neighbors.append((a + transfer_to_x, b - transfer_to_x))
        return neighbors
    while stack:
        current_state = stack.pop()
        if goal_state(current_state[0]) == current_state:
            path = []
            while current_state:
                path.append(current_state)
                current_state = parent[current_state]
            return path[::-1]
        for neighbor in get_neighbors(current_state):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current_state
                stack.append(neighbor)
    return None
path = water_jug_dfs()
if path:
    print("Path to solution:")
    for state in path:
        print(state)
else:
    print("No solution found.")
