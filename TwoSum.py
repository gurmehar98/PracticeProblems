class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) <= 1: return False
        checkDict = {}
        for i in range(len(nums)):
            if nums[i] in checkDict: return [checkDict[nums[i]], i]
            else: checkDict[target - nums[i]] = i