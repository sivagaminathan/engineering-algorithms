from collections import deque


class Graph:
    def __init__(self):
        self.graph = {}

    # Add Vertex
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    # Add Edge
    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.graph:
            self.add_vertex(vertex1)
        if vertex2 not in self.graph:
            self.add_vertex(vertex2)

        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)

    # Display Graph 
    def display(self):
        for vertex, edges in self.graph.items():
            print(f"{vertex} -> {edges}" )

    # DFS 
    def dfs(self, start):
        visited = set()
        self._dfs_recursive(start,visited)

    def _dfs_recursive(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end= " ")

        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self._dfs_recursive(neighbor, visited)

    # BFS 
    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)

        while queue:
            vertex = queue.popleft()
            print(vertex, end=" ")

            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

def main():
    graph = Graph()
    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "D")
    graph.add_edge("C", "D")
    graph.add_edge("D", "E")

    print("Graph Adjacency List:")
    graph.display()

    print("\n DFS Traversal starting from vertex A:")
    graph.dfs("A")

    print("\n\n BFS Traversal starting from vertex A:")
    graph.bfs("A")

if __name__ == "__main__":
    main()