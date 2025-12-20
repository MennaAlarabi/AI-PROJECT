# Maze Pathfinding

## Problem Description
Maze Pathfinding is a search problem in Artificial Intelligence where an agent must find a valid path from a given start cell to a goal cell within a maze.
The maze is represented as a 2D grid containing free cells and blocked cells (walls).
At each step, the agent can move in four directions (up, down, left, right) as long as the move is valid.
The agent cannot pass through obstacles or move outside the maze boundaries.
Each movement has a uniform cost, and the objective is to reach the goal with the minimum total path cost.


## Problem Domain
Maze Pathfinding is a problem in the domain of robotics and artificial intelligence search. It involves an agent navigating a two-dimensional maze composed of free cells and blocked cells (obstacles).  
The agent starts from a specified initial position and aims to reach a predefined goal position by moving in four possible directions while avoiding obstacles and staying within the maze boundaries. Each movement has a uniform cost, and the objective is to find the shortest valid path from the start to the goal using search algorithms.


## Implementation Approach
- **State Representation:**  
   Each state is represented by the agent’s current position in the maze as a pair of coordinates: `(row, column)`  
   This representation uniquely identifies the agent’s location within the maze.

- **Initial State:**  
  The initial state corresponds to the starting position of the agent in the maze, defined by the given start cell.

- **Goal State:**  
  The goal state is reached when the agent arrives at the target cell specified in the maze.

- **Successor Function:**  
  The successor function generates all valid neighboring states by moving the agent one step in the four possible directions `(up, down, left, right)`  
  A successor is considered valid if it lies within the maze boundaries and does not correspond to a blocked cell.

- **Cost Function:**  
  Each movement between adjacent cells has a uniform cost of 1.  
  The total path cost is calculated as the sum of the costs of all actions taken from the initial state to the goal state.

- **Heuristic Function:**  
  The heuristic function used is the Manhattan Distance, which estimates the cost from the current state to the goal state.  
  It is computed as: 
    `h(n) = |x_{current} - x_{goal}| + |y_{current} - y_{goal}|`  
  This heuristic is admissible and helps guide the search efficiently toward the goal.


## Algorithms Implemented

### Uninformed Search Algorithms
- **Breadth-First Search (BFS)**: Explores the maze level by level, guaranteeing the shortest path when all moves have equal cost, but may explore many unnecessary states.
  
- **Depth-First Search (DFS)**: Explores the maze by going as deep as possible along one path before backtracking, does not guarantee the shortest path, and may get stuck exploring long or infinite paths.

### Informed (Heuristic-Based) Search Algorithms
- **A * Search**: Combines the path cost from the start and a heuristic estimate to efficiently find an optimal path to the goal.

- **Greedy Best-First Search**: Selects the next state based only on the heuristic value, aiming to reach the goal quickly but without guaranteeing optimality.

                      

## Expected Results
For a **50 × 50 maze** with multiple obstacles, the expected performance is as follows:

| Algorithm         | Path Length | Nodes Explored  | Optimal |
| ----------------- | ----------- | --------------  | ------- |
| BFS               | 99          | 1714            | Yes     |
| DFS               | 201         | 636             | No      |
| A*                | 99          | 1039            | Yes     |
| Gready Best-First | 107         | 206             | No      |  

A* search is expected to outperform uninformed search algorithms by exploring significantly fewer nodes while still producing an optimal path.
