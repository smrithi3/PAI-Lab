from collections import deque

def bfs(graph, start):
    visited = set()  # To keep track of visited vertices
    queue = deque([start])  # Initialize the queue with the starting vertex

    while queue:
        vertex = queue.popleft()  # Dequeue a vertex
        if vertex not in visited:
            print(vertex, end=' ')  # Process the current vertex
            visited.add(vertex)

            # Enqueue neighboring vertices that haven't been visited
            queue.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited)

# Example usage:
# Define an adjacency list representation of a graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C'],
    'H': ['E']
}

start_vertex = 'A'
print("BFS traversal starting from vertex", start_vertex)
bfs(graph, start_vertex)
