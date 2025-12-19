import matplotlib.pyplot as plt
from collections import deque
import random

def generate_maze(rows=50, cols=50, wall_prob=0.3):
    maze = [[0 if random.random() > wall_prob else 1 for _ in range(cols)] for _ in range(rows)]
    maze[0][0] = 0 
    maze[rows-1][cols-1] = 0  
    return maze

def search_maze_optimized(maze):
    if not maze or not maze[0] or maze[0][0] == 1:
        return False, []

    rows, cols = len(maze), len(maze[0])
    if maze[rows-1][cols-1] == 1:
        return False, []

    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    queue = deque([(0,0,[(0,0)])])
    visited = {(0,0)}

    while queue:
        row, col, path = queue.popleft()
        for dr, dc in directions:
            new_row, new_col = row+dr, col+dc
            if (0 <= new_row < rows and 0 <= new_col < cols and
                (new_row,new_col) not in visited and maze[new_row][new_col]==0):
                new_path = path + [(new_row,new_col)]
                if new_row==rows-1 and new_col==cols-1:
                    return True, new_path
                queue.append((new_row,new_col,new_path))
                visited.add((new_row,new_col))

    return False, []

def visualize_maze(maze, path):
    rows, cols = len(maze), len(maze[0])
    plt.figure(figsize=(cols/5, rows/5))  

    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 1:
                color = 'black'
            elif (r,c) in path:
                color = 'darkred'
            else:
                color = 'white'
            plt.fill_between([c, c+1], [rows-r-1]*2, [rows-r]*2, color=color, edgecolor='gray')

    start_r, start_c = path[0]
    goal_r, goal_c = path[-1]
    plt.scatter(start_c+0.5, rows-start_r-0.5, color='green', s=100, marker='s', label='Start')
    plt.scatter(goal_c+0.5, rows-goal_r-0.5, color='blue', s=100, marker='X', label='Goal')

    plt.xticks([])
    plt.yticks([])
    plt.title("Maze Visualization with BFS Shortest Path (50x50)")
    plt.legend(loc='upper right')
    plt.show()

maze = generate_maze(50,50)

result, path = search_maze_optimized(maze)
print(f"Path exists: {result}")
if result:
    print(f"Shortest path length: {len(path)} steps")
    visualize_maze(maze, path)
