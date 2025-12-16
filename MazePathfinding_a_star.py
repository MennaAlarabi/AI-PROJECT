import heapq
import time

class Node:
    def __init__(self, row, col, g=float('inf'), h=0, parent=None):
        self.row = row
        self.col = col
        self.g = g  
        self.h = h  
        self.f = g + h 
        self.parent = parent
    
    def __lt__(self, other):
        return self.f < other.f
    
    def __eq__(self, other):
        return self.row == other.row and self.col == other.col
    
    def __hash__(self):
        return hash((self.row, self.col))

def manhattan_distance(node1, node2):
    return abs(node1.row - node2.row) + abs(node1.col - node2.col)

def generate_maze():

    maze = [[0 for _ in range(50)] for _ in range(50)]
    
    for i in range(50):
        maze[i][0] = 1
        maze[i][49] = 1
    for j in range(50):
        maze[0][j] = 1
        maze[49][j] = 1
    
    for i in range(3, 47, 4):
        for j in range(2, 48):
            if j % 8 != 4:  
                maze[i][j] = 1
    
    for j in range(4, 46, 6):
        for i in range(2, 48):
            if i % 6 != 3: 
                maze[i][j] = 1
    
    for j in range(1, 49):
        maze[48][j] = 0
    
    for i in range(1, 49):
        maze[i][48] = 0
    
    return maze

def get_neighbors(node, maze, rows, cols):
    neighbors = []
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] 
    
    for dr, dc in directions:
        new_row = node.row + dr
        new_col = node.col + dc
        
        if (0 <= new_row < rows and 
            0 <= new_col < cols and 
            maze[new_row][new_col] == 0):
            neighbors.append(Node(new_row, new_col))
    
    return neighbors

def reconstruct_path(node):
    path = []
    current = node
    while current is not None:
        path.append((current.row, current.col))
        current = current.parent
    return path[::-1]

def a_star(maze, start_pos, end_pos):

    start_time = time.time()
    
    rows = len(maze)
    cols = len(maze[0])
    
    start_node = Node(start_pos[0], start_pos[1], g=0)
    end_node = Node(end_pos[0], end_pos[1])
    start_node.h = manhattan_distance(start_node, end_node)
    start_node.f = start_node.g + start_node.h
    
    open_set = []
    heapq.heappush(open_set, start_node)
    closed_set = set()
    
    g_scores = {(start_node.row, start_node.col): 0}
    
    nodes_explored = 0
    
    while open_set:
        current = heapq.heappop(open_set)
        current_pos = (current.row, current.col)
        
        if current.row == end_node.row and current.col == end_node.col:
            execution_time = time.time() - start_time
            path = reconstruct_path(current)
            return path, nodes_explored, execution_time
        
        if current_pos in closed_set:
            continue
        
        closed_set.add(current_pos)
        nodes_explored += 1
        
        neighbors = get_neighbors(current, maze, rows, cols)
        
        for neighbor in neighbors:
            neighbor_pos = (neighbor.row, neighbor.col)
            
            if neighbor_pos in closed_set:
                continue
            
            tentative_g = current.g + 1
            
            if neighbor_pos not in g_scores or tentative_g < g_scores[neighbor_pos]:
                g_scores[neighbor_pos] = tentative_g
                neighbor.g = tentative_g
                neighbor.h = manhattan_distance(neighbor, end_node)
                neighbor.f = neighbor.g + neighbor.h
                neighbor.parent = current
                heapq.heappush(open_set, neighbor)
    
    execution_time = time.time() - start_time
    return None, nodes_explored, execution_time


def main():
    ROWS = 50
    COLS = 50
    START = (1, 1)
    END = (ROWS-2, COLS-2)
    
    maze = generate_maze()
    
    path, nodes_explored, execution_time = a_star(maze, START, END)
    
    if path:
        print(f"Path Length: {len(path) - 1}")
        print(f"Nodes Explored: {nodes_explored}")
        print(f"Execution Time: {execution_time:.6f}")
    else:
        print("Path Length: 0")
        print(f"Nodes Explored: {nodes_explored}")
        print(f"Execution Time: {execution_time:.6f}")

if __name__ == "__main__":
    main()