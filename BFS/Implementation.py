from collections import deque
import random

def generate_maze(rows=50, cols=50, wall_prob=0.3):
    maze = [[0 if random.random() > wall_prob else 1 for _ in range(cols)] for _ in range(rows)]
    maze[0][0] = 0          # Start
    maze[rows-1][cols-1] = 0  # Goal
    return maze

def bfs_maze(maze):
    rows, cols = len(maze), len(maze[0])
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    
    queue = deque([(0, 0, [(0, 0)])])
    visited = {(0, 0)}
    
    while queue:
        row, col, path = queue.popleft()
        
        if (row, col) == (rows-1, cols-1):
            return {
                "found": True,
                "path": path,
                "path_length": len(path),
                "nodes_explored": len(visited)
            }
        
        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if (0 <= nr < rows and 0 <= nc < cols and
                maze[nr][nc] == 0 and (nr, nc) not in visited):
                
                visited.add((nr, nc))
                queue.append((nr, nc, path + [(nr, nc)]))
    
    return {
        "found": False,
        "path": [],
        "path_length": 0,
        "nodes_explored": len(visited)
    }


maze = generate_maze()
result = bfs_maze(maze)

print("Path Found:", result["found"])
print("Path Length:", result["path_length"])
print("Nodes Explored:", result["nodes_explored"])
