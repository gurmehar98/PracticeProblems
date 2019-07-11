class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def sortedArrayToBST(self, nums):
        if nums == []: return None
        return self._helper(nums)
    def _helper(self, nums):
        if len(nums) == 1: return TreeNode(nums[0])
        elif len(nums) == 2:
            root = TreeNode(nums[0])
            root.right = TreeNode(nums[1])
            return root
        middle = len(nums) // 2
        root = TreeNode(nums[middle])
        root.left = self._helper(nums[:middle])
        root.right = self._helper(nums[middle + 1:])
        return root

if __name__ == "__main__":
    nums = [-10, -3, 0, 5, 9]
    s = Solution()
    print(s.sortedArrayToBST(nums))