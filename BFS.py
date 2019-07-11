from collections import defaultdict, deque
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def addEdge(self, x, y):
        if y not in self.graph[x]:
            self.graph[x].append(y)
    def bfs(self, root):
        if root not in self.graph.keys():
            return
        myQueue, visited = deque(), set()
        myQueue.append(root)
        visited.add(root)
        while myQueue:
            curr = myQueue.popleft()
            print(curr)
            for i in self.graph[curr]:
                if i not in visited:
                    myQueue.append(i)
                    visited.add(i)

if __name__ == "__main__":
    G = Graph()
    G.addEdge(1, 2)
    G.addEdge(1, 3)
    G.addEdge(2, 4)
    G.addEdge(2, 5)
    G.addEdge(3, 6)
    G.addEdge(3, 7)
    G.bfs(1)
