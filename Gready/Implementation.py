import heapq
import random

def generate_maze(rows=50, cols=50, wall_prob=0.3, seed=123):
    random.seed(seed)
    maze = [[0 if random.random() > wall_prob else 1 for _ in range(cols)] for _ in range(rows)]
    maze[0][0] = 0          
    maze[rows-1][cols-1] = 0  
    return maze

def heuristic(pos, goal):
    
    return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])

def greedy_maze(maze):
    rows, cols = len(maze), len(maze[0])
    start = (0, 0)
    goal = (rows-1, cols-1)
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    
    pq = [(heuristic(start, goal), start, [(0, 0)])]  
    visited = {start}  
    
    while pq:
        h_score, (row, col), path = heapq.heappop(pq)
        
        if (row, col) == goal:
            return {
                "found": True,
                "path": path,
                "path_length": len(path),
                "nodes_explored": len(visited)
            }
        
        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            
            if (0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 0 and (nr, nc) not in visited):
                visited.add((nr, nc))
                new_path = path + [(nr, nc)]
                heapq.heappush(pq, (heuristic((nr, nc), goal), (nr, nc), new_path))
    
    return {
        "found": False,
        "path": [],
        "path_length": 0,
        "nodes_explored": len(visited)
    }


maze = generate_maze(rows=50, cols=50, wall_prob=0.25, seed=123)
result = greedy_maze(maze)

print("Path Found:", result["found"])
print("Path Length:", result["path_length"])
print("Nodes Explored:", result["nodes_explored"])

