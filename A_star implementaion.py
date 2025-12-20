import heapq
import random

def generate_maze(rows=50, cols=50, wall_prob=0.3, seed=123):
    """Generate maze with seed for reproducibility"""
    random.seed(seed)
    maze = [[0 if random.random() > wall_prob else 1 for _ in range(cols)] for _ in range(rows)]
    maze[0][0] = 0          
    maze[rows-1][cols-1] = 0  
    return maze

def heuristic(pos, goal):
    """Manhattan distance heuristic"""
    return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])

def astar_maze(maze):
    rows, cols = len(maze), len(maze[0])
    start = (0, 0)
    goal = (rows-1, cols-1)
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    
    pq = [(heuristic(start, goal), 0, 0, 0, [(0, 0)])]
    visited = {start: 0}  
    
    while pq:
        f_score, g_score, row, col, path = heapq.heappop(pq)
        
        if (row, col) == goal:
            return {
                "found": True,
                "path": path,
                "path_length": len(path),
                "nodes_explored": len(visited)
            }
        
        if visited.get((row, col), float('inf')) < g_score:
            continue
        
        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            
            if (0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 0):
                new_g_score = g_score + 1
                
                if (nr, nc) not in visited or new_g_score < visited[(nr, nc)]:
                    visited[(nr, nc)] = new_g_score
                    new_f_score = new_g_score + heuristic((nr, nc), goal)
                    new_path = path + [(nr, nc)]
                    heapq.heappush(pq, (new_f_score, new_g_score, nr, nc, new_path))
    
    return {
        "found": False,
        "path": [],
        "path_length": 0,
        "nodes_explored": len(visited)
    }

maze = generate_maze(rows=50, cols=50, wall_prob=0.25, seed=123)
result = astar_maze(maze)

print("Path Found:", result["found"])
print("Path Length:", result["path_length"])
print("Nodes Explored:", result["nodes_explored"])
