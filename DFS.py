from collections import defaultdict, deque
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def addEdge(self, x, y):
        if y not in self.graph[x]:
            self.graph[x].append(y)
    def _helper(self, root, visited):
        print(root)
        for i in self.graph[root]:
            if i not in visited:
                self._helper(i, visited)
                visited.add(i)

    def dfs(self, root):
        if root not in self.graph.keys():
            return
        visited = set()
        visited.add(root)
        self._helper(root, visited)

if __name__ == "__main__":
    G = Graph()
    G.addEdge(1, 2)
    G.addEdge(1, 3)
    G.addEdge(2, 4)
    G.addEdge(2, 5)
    G.addEdge(3, 6)
    G.addEdge(3, 7)
    G.dfs(1)
