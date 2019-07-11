class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    def cloneGraph(self, node):
        self.visited = {}
        return self._helper(node)
    def _helper(self, node):
        if node != None and node not in self.visited:
            newNode = UndirectedGraphNode(node.label)
            self.visited[newNode.label] = newNode
            newNode.neighbors = [self.visited.get(n.label) or self._helper(n) for n in node.neighbors]
            return newNode