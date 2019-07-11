class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums):
        root = None
        return self._helper(nums, root)
    def _helper(self, nums, root):
        if nums == []: return None
        maxVal = max(nums)
        root = TreeNode(maxVal)
        if root == None: return None
        maxValInd = nums.index(maxVal)
        root.left = self._helper(nums[:maxValInd], root.left)
        root.right = self._helper(nums[maxValInd + 1:], root.right)
        return root

if __name__ == "__main__":
    nums = [3, 2, 1, 6, 0, 5]
    s = Solution()
    print(s.constructMaximumBinaryTree(nums))