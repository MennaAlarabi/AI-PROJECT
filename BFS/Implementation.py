from collections import deque

rows, cols = 50, 50
maze = [[0 for _ in range(cols)] for _ in range(rows)]

maze[0][0] = 0
maze[49][49] = 0

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

result = bfs_maze(maze)

print("Path Found:", result["found"])
print("Path Length:", result["path_length"])
print("Nodes Explored:", result["nodes_explored"])
