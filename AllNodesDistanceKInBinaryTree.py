class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root, target, K):
        self.parent, self.visited = {}, {}
        self._dfs(root, None)
        return self._helper(root, target, K)
    def _helper(self, root, target, K):
        distance, queue = 0, []
        queue.append(target)
        while len(queue) != 0:
            if distance == K: break
            temp = []
            for node in queue:
                self.visited[node] = True
                if node.left != None and self.visited[node.left] == False: temp.append(node.left)
                if node.right != None and self.visited[node.right] == False: temp.append(node.right)
                if self.parent[node] != None and self.visited[self.parent[node]] == False: temp.append(self.parent[node])
            queue = temp
            distance += 1 
        return [node.val for node in queue]
    def _dfs(self, root, prev):
        if not root: return
        self.visited[root], self.parent[root] = False, prev
        self._dfs(root.left, root)
        self._dfs(root.right, root)