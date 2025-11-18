"""
Question 3: Word BFS - Word Ladder Transformation

HOW BFS WORKS IN THIS SOLUTION:
We treat each valid word as a node in a graph, with edges connecting words that 
differ by exactly one letter. BFS explores transformations by edit-distance layers, 
guaranteeing the shortest sequence of single-letter changes from start to target. 
Each BFS level represents one letter change, so the first time we reach the target 
word, we have found the minimum transformation sequence.
"""

from collections import deque
import string


def get_neighbors(word, word_set):
    """
    Generate all valid neighbor words that differ by one letter.
    
    Args:
        word (str): Current word
        word_set (set): Set of valid words from dictionary
    
    Returns:
        list: List of valid neighbor words
    """
    neighbors = []
    
    # Try changing each position to each letter
    for i in range(len(word)):
        for letter in string.ascii_lowercase:
            if letter != word[i]:
                # Create new word with one letter changed
                new_word = word[:i] + letter + word[i+1:]
                
                # Check if it's in the dictionary
                if new_word in word_set:
                    neighbors.append(new_word)
    
    return neighbors


def bfs_word_ladder(start, target, word_list):
    """
    Find the shortest transformation sequence using BFS.
    
    Args:
        start (str): Starting word
        target (str): Target word
        word_list (list): Dictionary of valid words
    
    Returns:
        tuple: (transformation sequence as list, number of transformations)
               Returns (None, 0) if no sequence exists
    """
    # Convert to set for O(1) lookup
    word_set = set(word_list)
    
    # Check if target exists in dictionary
    if target not in word_set:
        return None, 0
    
    # Initialize BFS
    queue = deque([start])
    visited = {start}
    parent = {start: None}
    
    # BFS traversal
    while queue:
        current = queue.popleft()
        
        # Check if we reached the target
        if current == target:
            # Reconstruct path
            path = []
            node = target
            while node is not None:
                path.append(node)
                node = parent[node]
            path.reverse()
            
            transformations = len(path) - 1
            return path, transformations
        
        # Explore neighbors (words differing by one letter)
        neighbors = get_neighbors(current, word_set)
        
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)
    
    # No transformation sequence found
    return None, 0


def show_differences(word1, word2):
    """Highlight the differences between two words."""
    diff_positions = []
    for i, (c1, c2) in enumerate(zip(word1, word2)):
        if c1 != c2:
            diff_positions.append(i)
    
    result = []
    for i, char in enumerate(word2):
        if i in diff_positions:
            result.append(f"[{char}]")
        else:
            result.append(char)
    
    return "".join(result)


def main():
    # Problem data
    start_word = "hit"
    target_word = "cog"
    dictionary = ["hot", "dot", "dog", "lot", "log", "cog"]
    
    print("=" * 60)
    print("QUESTION 3: WORD BFS - WORD LADDER TRANSFORMATION")
    print("=" * 60)
    print()
    
    # Display problem setup
    print("Problem Setup:")
    print("-" * 60)
    print(f"Start Word:  {start_word}")
    print(f"Target Word: {target_word}")
    print(f"Dictionary:  {dictionary}")
    print()
    print("Rules:")
    print("  • Change only ONE letter at a time")
    print("  • Each intermediate word must exist in the dictionary")
    print()
    
    # Find transformation sequence
    print(f"Finding shortest transformation sequence...")
    print()
    
    sequence, transformations = bfs_word_ladder(start_word, target_word, dictionary)
    
    # Display results
    if sequence:
        print("=" * 60)
        print("RESULTS:")
        print("=" * 60)
        print()
        print("✓ Transformation sequence found!")
        print()
        
        print("Shortest Transformation Sequence:")
        print("-" * 60)
        print(" → ".join(sequence))
        print()
        print(f"Number of transformations: {transformations}")
        print()
        
        # Detailed transformation steps
        print("Detailed Step-by-Step Transformations:")
        print("-" * 60)
        for i in range(len(sequence) - 1):
            current = sequence[i]
            next_word = sequence[i + 1]
            
            # Find which letter changed
            diff_pos = -1
            for j in range(len(current)):
                if current[j] != next_word[j]:
                    diff_pos = j
                    break
            
            if diff_pos >= 0:
                highlighted = show_differences(current, next_word)
                print(f"  Step {i + 1}: {current} → {highlighted}")
                print(f"           Changed position {diff_pos}: '{current[diff_pos]}' → '{next_word[diff_pos]}'")
            else:
                print(f"  Step {i + 1}: {current} → {next_word}")
        print()
        
        # Summary
        print("Transformation Summary:")
        print("-" * 60)
        print(f"  Total words in sequence: {len(sequence)}")
        print(f"  Total transformations:   {transformations}")
        print(f"  Words from dictionary:   {len(sequence) - 2}")  # Excluding start and end
        print()
        
    else:
        print(f"✗ No transformation sequence found from '{start_word}' to '{target_word}'")
        print("   The target word may not be reachable with the given dictionary.")
        print()
    
    print("=" * 60)


if __name__ == "__main__":
    main()
