class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubtree(self, s, t):
        return self._helper(s, t)
    def _helper(self, s, t):
        if self._dfs(s, t): return True
        if s == None: return False
        return self._helper(s.left, t) or self._helper(s.right, t)
    def _dfs(self, s, t):
        if s == None or t == None: return s == t
        return (s.val == t.val and self._dfs(s.left, t.left) and self._dfs(s.right, t.right))

if __name__ == "__main__":
    s = TreeNode(3)
    s.left = TreeNode(4)
    s.left.left = TreeNode(1)
    s.left.left.left = TreeNode(0)
    s.left.right = TreeNode(2)
    s.right = TreeNode(5)
    t = TreeNode(4)
    t.left = TreeNode(1)
    t.right = TreeNode(2)
    obj = Solution()
    print(obj.isSubtree(s, t))