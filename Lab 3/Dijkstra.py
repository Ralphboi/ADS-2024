import heapq

def dijkstra(graph, start):
    # Priority queue to store (distance, vertex)
    pq = [(0, start)]
    # Dictionary to store the shortest path to each vertex
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    # Dictionary to store the shortest path tree
    previous_nodes = {vertex: None for vertex in graph}

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_vertex
                heapq.heappush(pq, (distance, neighbor))

    return distances, previous_nodes

def reconstruct_path(previous_nodes, start, end):
    path = []
    current_vertex = end
    while current_vertex is not None:
        path.append(current_vertex)
        current_vertex = previous_nodes[current_vertex]
    path.reverse()
    return path if path[0] == start else []

# Example
if __name__ == "__main__":
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }
    start = 'A'
    end = 'D'
    distances, previous_nodes = dijkstra(graph, start)
    
    print("Shortest distances from start node:")
    for vertex, distance in distances.items():
        print(f"Distance to {vertex}: {distance}")

    print("\nShortest path from start to end node:")
    path = reconstruct_path(previous_nodes, start, end)
    print(" -> ".join(path))
