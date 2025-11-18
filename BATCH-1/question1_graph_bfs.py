"""
Question 1: Graph BFS - City Transport Network

HOW BFS WORKS IN THIS SOLUTION:
Breadth-First Search explores nodes layer by layer, starting from Lagos. 
Using a queue (deque), we visit all neighbors at the current distance before 
moving deeper. By tracking each node's parent, we can reconstruct the shortest 
path (fewest edges) from Lagos to Akure in this unweighted graph.
"""

from collections import deque


def bfs_shortest_path(graph, start, goal):
    """
    Find the shortest path between two nodes using BFS.
    
    Args:
        graph (dict): Adjacency list representation of the graph
        start (str): Starting node
        goal (str): Destination node
    
    Returns:
        tuple: (path as list of nodes, number of steps/edges)
               Returns (None, 0) if no path exists
    """
    # Initialize BFS data structures
    queue = deque([start])  # Queue for BFS frontier
    visited = {start}        # Set of visited nodes
    parent = {start: None}   # Parent mapping for path reconstruction
    
    # BFS traversal
    while queue:
        current = queue.popleft()
        
        # Check if we reached the goal
        if current == goal:
            # Reconstruct path by backtracking through parents
            path = []
            node = goal
            while node is not None:
                path.append(node)
                node = parent[node]
            path.reverse()
            
            # Number of steps = number of edges = len(path) - 1
            steps = len(path) - 1
            return path, steps
        
        # Explore neighbors
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)
    
    # No path found
    return None, 0


def main():
    # Task i: Represent the graph as a dictionary
    # Each key is a city, and its value is a list of directly connected cities
    transport_network = {
        "Lagos": ["Ibadan", "Abeokuta"],
        "Ibadan": ["Ilorin", "Osogbo"],
        "Abeokuta": ["Ondo"],
        "Osogbo": ["Akure"],
        "Ondo": ["Akure"],
        "Ilorin": ["Lokoja"],
        "Akure": [],
        "Lokoja": []
    }
    
    print("=" * 60)
    print("QUESTION 1: GRAPH BFS - CITY TRANSPORT NETWORK")
    print("=" * 60)
    print()
    
    # Display the graph representation
    print("Graph Representation (Adjacency List):")
    print("-" * 60)
    for city, neighbors in transport_network.items():
        if neighbors:
            print(f"{city:12} → {neighbors}")
        else:
            print(f"{city:12} → []")
    print()
    
    # Task ii: Implement BFS to find shortest path from Lagos to Akure
    start_city = "Lagos"
    goal_city = "Akure"
    
    print(f"Finding shortest path from {start_city} to {goal_city}...")
    print()
    
    path, steps = bfs_shortest_path(transport_network, start_city, goal_city)
    
    # Task iii: Print the results
    if path:
        print("=" * 60)
        print("RESULTS:")
        print("=" * 60)
        print()
        print("✓ Path found!")
        print()
        print("Sequence of cities in the path:")
        print("-" * 60)
        print(" → ".join(path))
        print()
        print(f"Number of steps (edges): {steps}")
        print()
        
        # Additional visualization
        print("Step-by-step breakdown:")
        print("-" * 60)
        for i in range(len(path) - 1):
            print(f"  Step {i + 1}: {path[i]} → {path[i + 1]}")
        print()
    else:
        print(f"✗ No path found from {start_city} to {goal_city}")
        print()
    
    print("=" * 60)


if __name__ == "__main__":
    main()
