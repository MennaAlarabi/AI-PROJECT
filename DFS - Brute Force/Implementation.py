import random
import sys
from collections import deque
sys.setrecursionlimit(10000)

def generate_maze(rows=50, cols=50, wall_prob=0.25):
    random.seed(42)
    while True:
        maze = [[0 if random.random() > wall_prob else 1 for _ in range(cols)] for _ in range(rows)]
        maze[0][0] = 0
        maze[rows-1][cols-1] = 0
        
        queue = deque([(0,0)])
        visited = set([(0,0)])
        found = False
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        
        while queue:
            r,c = queue.popleft()
            if r==rows-1 and c==cols-1:
                found = True
                break
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 0<=nr<rows and 0<=nc<cols and maze[nr][nc]==0 and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    queue.append((nr,nc))
        if found:
            return maze

def search_maze_dfs(maze):
    rows, cols = len(maze), len(maze[0])
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    visited = [[False]*cols for _ in range(rows)]
    path = []
    nodes_explored = 0
    found_path = False

    def dfs(r,c):
        nonlocal nodes_explored, found_path
        nodes_explored += 1
        visited[r][c] = True
        path.append((r,c))

        if r == rows-1 and c == cols-1:
            found_path = True
            return True

        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and maze[nr][nc]==0:
                if dfs(nr,nc):
                    return True

        path.pop()
        return False

    dfs(0,0)
    return found_path, path, nodes_explored

maze = generate_maze(50,50, wall_prob=0.40)
found, path, nodes = search_maze_dfs(maze)

print(f"Path exists: {found}") 
print(f"Nodes explored: {nodes}")
if found:
    print(f"Path length: {len(path)} steps")
