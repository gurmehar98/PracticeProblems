class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        self.total = 0
        self.myDict = dict()
        if root == None:
            return []
        self._helper(root)
        maxVal = max(self.myDict.values())
        return [k for k, v in self.myDict.items() if v == maxVal]
    def _helper(self, root):
        if root == None:
            return 0
        l = self._helper(root.left)
        r = self._helper(root.right)
        self.total = l + r + root.val
        if self.total not in self.myDict.keys():
            self.myDict[self.total] = 1
        else:
            self.myDict[self.total] += 1
        return self.total

if __name__ == "__main__":
    myTree = TreeNode(5)
    myTree.left = TreeNode(2)
    myTree.right = TreeNode(-3)
    s = Solution()
    print(s.findFrequentTreeSum(myTree))