import matplotlib.pyplot as plt
import numpy as np
import random

# ===== Generate Maze 50x50 with guaranteed path =====
def generate_maze_with_path(rows=50, cols=50, seed=123):
    random.seed(seed) 
    maze = np.ones((rows, cols), dtype=int)

    # Guaranteed path from start to goal
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

    # Randomly remove walls
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

# ===== Visualization =====
def visualize_maze(maze, path):
    rows, cols = maze.shape
    plt.figure(figsize=(cols/5, rows/5))

    for r in range(rows):
        for c in range(cols):
            if maze[r, c] == 1:
                color = 'black'
            elif (r, c) in path:
                color = 'purple'
            else:
                color = 'white'

            plt.fill_between(
                [c, c+1],
                [rows-r-1]*2,
                [rows-r]*2,
                color=color,
                edgecolor='gray'
            )

    start_r, start_c = path[0]
    goal_r, goal_c = path[-1]

    plt.scatter(start_c+0.5, rows-start_r-0.5,
                color='darkblue', s=100, marker='s', label='Start')
    plt.scatter(goal_c+0.5, rows-goal_r-0.5,
                color='darkgreen', s=100, marker='X', label='Goal')

    plt.xticks([])
    plt.yticks([])
    plt.title("DFS Maze Pathfinding (50x50)")
    plt.legend(loc='lower left')
    plt.show()

# ===== Run Everything =====
maze = generate_maze_with_path(50, 50, seed=123)

result = search_maze_dfs(maze)
path = result["path"]

print(f"Path exists: {path is not None}")

if path:
    print(f"DFS path length: {len(path)} steps")
    print("Nodes Explored:", result["nodes_explored"])
    visualize_maze(maze, path)
else:
    print("No path found!")
