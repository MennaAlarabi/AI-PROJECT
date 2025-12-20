import matplotlib.pyplot as plt
import heapq
import random

def generate_maze(rows=50, cols=50, wall_prob=0.3, seed=123):
   
    random.seed(seed)
    maze = [[0 if random.random() > wall_prob else 1 for _ in range(cols)] for _ in range(rows)]
    maze[0][0] = 0 
    maze[rows-1][cols-1] = 0  
    return maze

def heuristic(position, goal):
    
    return abs(position[0] - goal[0]) + abs(position[1] - goal[1])

def greedy_search_maze(maze):
    if not maze or not maze[0] or maze[0][0] == 1:
        return False, []
    
    rows, cols = len(maze), len(maze[0])
    if maze[rows-1][cols-1] == 1:
        return False, []
    
    start = (0, 0)
    goal = (rows-1, cols-1)
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    
    pq = [(heuristic(start, goal), start, [(0, 0)])]  
    visited = {start}
    
    while pq:
        f_score, (row, col), path = heapq.heappop(pq)
        
        if (row, col) == goal:
            return True, path
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            if (0 <= new_row < rows and 0 <= new_col < cols and 
                maze[new_row][new_col] == 0 and (new_row, new_col) not in visited):
                
                visited.add((new_row, new_col))
                new_f_score = heuristic((new_row, new_col), goal)
                new_path = path + [(new_row, new_col)]
                heapq.heappush(pq, (new_f_score, (new_row, new_col), new_path))
    
    return False, []

def visualize_maze(maze, path):
    rows, cols = len(maze), len(maze[0])
    plt.figure(figsize=(cols/5, rows/5))  
    
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 1:
                color = 'purple'   
            elif (r,c) in path:
                color = 'orange'   
            else:
                color = 'pink'     
            plt.fill_between([c, c+1], [rows-r-1]*2, [rows-r]*2, color=color, edgecolor='gray')
    
    start_r, start_c = path[0]
    goal_r, goal_c = path[-1]
    plt.scatter(start_c+0.5, rows-start_r-0.5, color='blue', s=100, marker='s', label='Start')  
    plt.scatter(goal_c+0.5, rows-goal_r-0.5, color='green', s=100, marker='X', label='Goal')   
    
    plt.xticks([])
    plt.yticks([])
    plt.title("Greedy Best-First Search Maze Pathfinding (50x50)")
    plt.legend(loc='upper right')
    plt.show()


maze = generate_maze(50, 50, wall_prob=0.25, seed=123)
result, path = greedy_search_maze(maze)

print(f"Path exists: {result}")
if result:
    print(f"Path length: {len(path)} steps")
    visualize_maze(maze, path)
else:
    print("No path found in this maze!")

