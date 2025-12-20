import numpy as np
import random

# ===== Generate Maze 50x50 with guaranteed path =====
def generate_maze_with_path(rows=50, cols=50, seed=123):
    random.seed(seed)
    maze = np.ones((rows, cols), dtype=int)

    # Guaranteed path
    r = c = 0
    maze[r, c] = 0
    while r < rows-1 or c < cols-1:
        if r < rows-1 and c < cols-1:
            if random.choice([True, False]):
                r += 1
            else:
                c += 1
        elif r < rows-1:
            r += 1
        else:
            c += 1
        maze[r, c] = 0

    # Open some walls
    for i in range(rows):
        for j in range(cols):
            if maze[i, j] == 1 and random.random() > 0.4:
                maze[i, j] = 0

    return maze


# ===== DFS Search + Nodes Explored =====
def search_maze_dfs(maze):
    rows, cols = maze.shape
    stack = [(0, 0, [(0, 0)])]
    visited = {(0, 0)}
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    nodes_explored = 0

    while stack:
        row, col, path = stack.pop()
        nodes_explored += 1

        if (row, col) == (rows-1, cols-1):
            return {
                "path": path,
                "nodes_explored": nodes_explored
            }

        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if (0 <= nr < rows and 0 <= nc < cols and
                (nr, nc) not in visited and maze[nr, nc] == 0):
                stack.append((nr, nc, path + [(nr, nc)]))
                visited.add((nr, nc))

    return {
        "path": None,
        "nodes_explored": nodes_explored
    }


# ===== Run =====
maze = generate_maze_with_path(50, 50, seed=123)
result = search_maze_dfs(maze)

path = result["path"]
print("Path exists:", path is not None)

if path:
    print("DFS path length:", len(path))
    print("Nodes explored:", result["nodes_explored"])
else:
    print("No path found")
