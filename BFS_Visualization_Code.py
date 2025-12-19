import matplotlib.pyplot as plt

def visualize_maze(maze, path):
    rows, cols = len(maze), len(maze[0])
    plt.figure(figsize=(cols/5, rows/5))
    
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 1:
                color = 'black'      # Walls
            elif (r, c) in path:
                color = 'darkred'    # Final Path
            else:
                color = 'white'      # Free cells
            
            plt.fill_between(
                [c, c+1],
                [rows-r-1]*2,
                [rows-r]*2,
                color=color,
                edgecolor='gray'
            )
    
    if path:
        sr, sc = path[0]
        gr, gc = path[-1]
        plt.scatter(sc+0.5, rows-sr-0.5, color='green', s=100, marker='s', label='Start')
        plt.scatter(gc+0.5, rows-gr-0.5, color='blue', s=100, marker='X', label='Goal')
    
    plt.xticks([])
    plt.yticks([])
    plt.legend()
    plt.title("BFS Maze Pathfinding (50x50)")
    plt.show()

# Call visualization
if result["found"]:
    visualize_maze(maze, result["path"])
