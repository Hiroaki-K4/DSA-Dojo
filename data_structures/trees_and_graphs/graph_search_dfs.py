class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        # Adds an edge from vertex u to vertex v
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs_recursive(self, start, visited=None):
        if visited is None:
            visited = set()
        # Mark the current node as visited
        visited.add(start)
        print(start, end=" ")
        # Visit all neighbors that haven't been visited
        for neighbor in self.graph.get(start, []):
            if neighbor not in visited:
                self.dfs_recursive(neighbor, visited)

    def dfs_iterative(self, start):
        # Stack for the iterative DFS
        stack = [start]
        visited = set()
        while stack:
            node = stack.pop()
            if node not in visited:
                print(node, end=" ")
                visited.add(node)
                # Add neighbors to stack in reverse order to maintain order of traversal
                stack.extend(reversed(self.graph.get(node, [])))


if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    print("DFS (Recursive):")
    g.dfs_recursive(2)  # Starting from vertex 2
    print()

    print("DFS (Iterative):")
    g.dfs_iterative(2)  # Starting from vertex 2
    print()
