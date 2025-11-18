"""
Question 2: Grid BFS - Robot Movement in a Grid

HOW BFS WORKS IN THIS SOLUTION:
BFS treats grid cells as nodes and explores all reachable neighbors at the current 
distance before moving deeper. We use a queue to process cells level by level, 
ensuring the first time we reach the goal (2,2) we have the minimum number of moves. 
Parent tracking allows us to rebuild the exact move sequence.
"""

from collections import deque


def bfs_grid_path(grid, start, goal):
    """
    Find the shortest path in a grid using BFS.
    
    Args:
        grid (list): 2D matrix where 0 = passable, 1 = blocked
        start (tuple): Starting coordinate (row, col)
        goal (tuple): Goal coordinate (row, col)
    
    Returns:
        tuple: (path as list of coordinates, number of steps)
               Returns (None, 0) if no path exists
    """
    rows, cols = len(grid), len(grid[0])
    
    # Check if start or goal is blocked
    if grid[start[0]][start[1]] == 1 or grid[goal[0]][goal[1]] == 1:
        return None, 0
    
    # Four directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    direction_names = ["UP", "DOWN", "LEFT", "RIGHT"]
    
    # Initialize BFS data structures
    queue = deque([start])
    visited = {start}
    parent = {start: None}
    
    # BFS traversal
    while queue:
        current = queue.popleft()
        
        # Check if we reached the goal
        if current == goal:
            # Reconstruct path
            path = []
            node = goal
            while node is not None:
                path.append(node)
                node = parent[node]
            path.reverse()
            
            steps = len(path) - 1
            return path, steps
        
        # Explore neighbors in 4 directions
        for direction in directions:
            new_row = current[0] + direction[0]
            new_col = current[1] + direction[1]
            neighbor = (new_row, new_col)
            
            # Check bounds
            if 0 <= new_row < rows and 0 <= new_col < cols:
                # Check if cell is passable and not visited
                if grid[new_row][new_col] == 0 and neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = current
                    queue.append(neighbor)
    
    # No path found
    return None, 0


def print_grid_with_path(grid, path):
    """Visualize the grid with the path marked."""
    rows, cols = len(grid), len(grid[0])
    
    # Create a display grid
    display = []
    for i in range(rows):
        row = []
        for j in range(cols):
            if grid[i][j] == 1:
                row.append(" X ")  # Blocked
            else:
                row.append(" . ")  # Empty
        display.append(row)
    
    # Mark the path
    if path:
        for idx, (r, c) in enumerate(path):
            if idx == 0:
                display[r][c] = " S "  # Start
            elif idx == len(path) - 1:
                display[r][c] = " G "  # Goal
            else:
                display[r][c] = f" {idx} "  # Path step number
    
    # Print the grid
    print("+" + "---" * cols + "+")
    for row in display:
        print("|" + "".join(row) + "|")
    print("+" + "---" * cols + "+")
    print()
    print("Legend: S = Start, G = Goal, X = Blocked, . = Empty, Numbers = Path")


def main():
    # Task i: Represent the grid as a matrix
    # 0 = passable cell, 1 = blocked cell
    grid = [
        [0, 0, 0],  # Row 0
        [0, 1, 0],  # Row 1 (cell (1,1) is blocked)
        [0, 0, 0]   # Row 2
    ]
    
    start = (0, 0)  # Top-left corner
    goal = (2, 2)   # Bottom-right corner
    
    print("=" * 60)
    print("QUESTION 2: GRID BFS - ROBOT MOVEMENT")
    print("=" * 60)
    print()
    
    # Display the grid
    print("Grid Representation (3x3 matrix):")
    print("-" * 60)
    print("Initial Grid:")
    print_grid_with_path(grid, None)
    print(f"Start Position: {start}")
    print(f"Goal Position:  {goal}")
    print(f"Blocked Cell:   (1, 1)")
    print()
    
    # Task ii: Implement BFS to find shortest path
    print(f"Finding shortest path from {start} to {goal}...")
    print()
    
    path, steps = bfs_grid_path(grid, start, goal)
    
    # Task iii: Display the path
    if path:
        print("=" * 60)
        print("RESULTS:")
        print("=" * 60)
        print()
        print("✓ Path found!")
        print()
        
        print("Grid with Path:")
        print("-" * 60)
        print_grid_with_path(grid, path)
        
        print("Sequence of grid coordinates:")
        print("-" * 60)
        print(" → ".join(str(coord) for coord in path))
        print()
        print(f"Number of steps (moves): {steps}")
        print()
        
        # Step-by-step movement breakdown
        print("Step-by-step movements:")
        print("-" * 60)
        for i in range(len(path) - 1):
            curr = path[i]
            next_pos = path[i + 1]
            
            # Determine direction
            if next_pos[0] < curr[0]:
                direction = "UP"
            elif next_pos[0] > curr[0]:
                direction = "DOWN"
            elif next_pos[1] < curr[1]:
                direction = "LEFT"
            else:
                direction = "RIGHT"
            
            print(f"  Step {i + 1}: {curr} → {next_pos} ({direction})")
        print()
    else:
        print(f"✗ No path found from {start} to {goal}")
        print()
    
    print("=" * 60)


if __name__ == "__main__":
    main()
