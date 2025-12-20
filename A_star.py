import random
import heapq
import time
import sys

sys.setrecursionlimit(10000)

def initialize_maze(width, height):
    maze = [['#']*width for _ in range(height)]
    return maze

def carve_passages_from(x, y, maze):
    directions = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    random.shuffle(directions)
    for (nx, ny) in directions:
        if nx >= 0 and nx < len(maze[0]) and ny >= 0 and ny < len(maze) and maze[ny][nx] == '#':
            maze[ny][nx] = ' '
            carve_passages_from(nx, ny, maze)

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(maze, start, goal):
    rows = len(maze)
    cols = len(maze[0])
    
    counter = 0
    open_set = [(0, counter, start, [start])]
    visited = set()
    nodes_explored = 0
    
    while open_set:
        _, _, current, path = heapq.heappop(open_set)
        
        if current in visited:
            continue
            
        visited.add(current)
        nodes_explored += 1
        
        if current == goal:
            return path, nodes_explored
        
        y, x = current
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ny, nx = y + dy, x + dx
            neighbor = (ny, nx)
            
            if (0 <= ny < rows and 0 <= nx < cols and 
                maze[ny][nx] == ' ' and neighbor not in visited):
                
                new_path = path + [neighbor]
                g_score = len(new_path)
                h_score = heuristic(neighbor, goal)
                f_score = g_score + h_score
                
                counter += 1
                heapq.heappush(open_set, (f_score, counter, neighbor, new_path))
    
    return None, nodes_explored

dynamic_maze = initialize_maze(50, 50)

carve_passages_from(1, 1, dynamic_maze)

start = (1, 1)
goal = (48, 48)

dynamic_maze[start[0]][start[1]] = ' '
dynamic_maze[goal[0]][goal[1]] = ' '

start_time = time.time()
path, nodes_explored = astar(dynamic_maze, start, goal)
end_time = time.time()

execution_time = end_time - start_time

if path:
    print("- Path Found")
    print(f"- Path Length: {len(path)}")
else:
    print("- Path Not Found")
    print(f"- Path Length: 0")

print(f"- Nodes Explored: {nodes_explored}")
print(f"- Execution Time: {execution_time:.6f} seconds")
