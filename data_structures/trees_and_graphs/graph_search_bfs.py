from collections import deque


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        # Adds an edge from vertex u to vertex v
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        result = []

        while queue:
            current = queue.popleft()
            if not current in visited:
                visited.add(current)
                result.append(current)

                for neighbor in self.graph.get(current, []):
                    if not neighbor in visited:
                        queue.append(neighbor)

        return result


if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    print("BFS:", g.bfs(2))  # [2, 0, 3, 1]
