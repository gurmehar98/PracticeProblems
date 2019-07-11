class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findMode(self, root):
        if root == None: return []
        self.myDict = {}
        self._helper(root)
        maxVal = max(self.myDict.values())
        return [k for k, v in self.myDict.items() if v == maxVal]
    def _helper(self, root):
        if root == None: return []
        self._helper(root.left)
        self._helper(root.right)
        if root.val not in self.myDict.keys(): self.myDict[root.val] = 1
        else: self.myDict[root.val] += 1