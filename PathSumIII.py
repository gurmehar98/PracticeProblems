class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    #Memoized Solution
    def pathSum(self, root, sum):
        self.numPaths, cache = 0, {0:1}
        self._helper(root, sum, 0, cache)
        return self.numPaths
    def _helper(self, root, sum, currPathSum, cache):
        if root == None: return
        currPathSum += root.val
        oldPathSum = currPathSum - sum
        self.numPaths += cache.get(oldPathSum, 0)
        cache[currPathSum] = cache.get(currPathSum, 0) + 1
        self._helper(root.left, sum, currPathSum, cache)
        self._helper(root.right, sum, currPathSum, cache)
        cache[currPathSum] -= 1

    #Regular Brute-Force Solution:
    '''
    def pathSum(self, root, sum):
        self.numPaths = 0
        self._helper(root, sum)
        return self.numPaths
    def _helper(self, root, sum):
        if root == None: return
        self._helper(root.left, sum)
        self._helper(root.right, sum)
        self._dfs(root, sum)
    def _dfs(self, root, sum):
        if root == None: return
        if root.val == sum: self.numPaths += 1
        self._dfs(root.left, sum - root.val)
        self._dfs(root.right, sum - root.val)
    '''