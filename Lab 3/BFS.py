from collections import deque

def bfs(graph, start):
    visited = set()  # A set to keep track of visited nodes
    queue = deque([start])  # A queue to manage the nodes to visit

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")  
            visited.add(node)
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

# Example 
if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F', 'G'],
        'D': ['B'],
        'E': ['B'],
        'F': ['C'],
        'G': ['C']
    }
    print("BFS starting from node A:")
    bfs(graph, 'A')
