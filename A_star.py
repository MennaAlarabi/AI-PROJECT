import heapq
import time

class Node:
    def __init__(self, row, col, g=float('inf'), h=0, parent=None):
        self.row, self.col = row, col
        self.g, self.h = g, h
        self.f = g + h
        self.parent = parent
    
    def __lt__(self, other): return self.f < other.f
    def __eq__(self, other): return (self.row, self.col) == (other.row, other.col)
    def __hash__(self): return hash((self.row, self.col))

def manhattan_distance(a, b):
    return abs(a.row - b.row) + abs(a.col - b.col)

def generate_maze():
    maze = [[0]*50 for _ in range(50)]
    for i in range(50):
        maze[i][0] = maze[i][49] = 1
        maze[0][i] = maze[49][i] = 1

    for i in range(3, 47, 4):
        for j in range(2, 48):
            if j % 8 != 4: maze[i][j] = 1
    for j in range(4, 46, 6):
        for i in range(2, 48):
            if i % 6 != 3: maze[i][j] = 1

    for j in range(1, 49): maze[48][j] = 0
    for i in range(1, 49): maze[i][48] = 0
    return maze

def get_neighbors(node, maze, rows, cols):
    neighbors = []
    for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
        r, c = node.row+dr, node.col+dc
        if 0 <= r < rows and 0 <= c < cols and maze[r][c]==0:
            neighbors.append(Node(r,c))
    return neighbors

def reconstruct_path(node):
    path = []
    while node: 
        path.append((node.row, node.col))
        node = node.parent
    return path[::-1]

def a_star(maze, start_pos, end_pos):
    start_time = time.time()
    rows, cols = len(maze), len(maze[0])
    start = Node(*start_pos, g=0)
    end = Node(*end_pos)
    start.h = manhattan_distance(start, end)
    start.f = start.g + start.h

    open_set, closed_set = [start], set()
    g_scores = {(start.row, start.col): 0}
    nodes_explored = 0

    while open_set:
        current = heapq.heappop(open_set)
        if (current.row, current.col) in closed_set: continue
        if current == end:
            return reconstruct_path(current), nodes_explored, time.time()-start_time

        closed_set.add((current.row, current.col))
        nodes_explored += 1

        for neighbor in get_neighbors(current, maze, rows, cols):
            pos = (neighbor.row, neighbor.col)
            if pos in closed_set: continue
            tentative_g = current.g + 1
            if pos not in g_scores or tentative_g < g_scores[pos]:
                g_scores[pos] = tentative_g
                neighbor.g, neighbor.h, neighbor.f = tentative_g, manhattan_distance(neighbor, end), tentative_g + manhattan_distance(neighbor, end)
                neighbor.parent = current
                heapq.heappush(open_set, neighbor)

    return None, nodes_explored, time.time()-start_time

def main():
    ROWS, COLS = 50, 50
    START, END = (1,1), (ROWS-2, COLS-2)
    maze = generate_maze()
    path, explored, exec_time = a_star(maze, START, END)
    print(f"Path Length: {len(path)-1 if path else 0}")
    print(f"Nodes Explored: {explored}")
    print(f"Execution Time: {exec_time:.6f}")

if __name__ == "__main__":
    main()
