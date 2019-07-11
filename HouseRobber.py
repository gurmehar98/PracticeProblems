class Solution:
    def rob(self, nums):
        ind, maxVal, self.memoization = 0, 0, {}
        for i in range(0, len(nums)):
            rec = self._helper(nums, ind + i)
            maxVal = max(rec, maxVal)
        return maxVal
    def _helper(self, nums, ind):
        if ind >= len(nums):
            return 0
        curr, maxRob = 0, 0
        if ind in self.memoization.keys():
            return self.memoization[ind]
        for i in range(2, len(nums)):
            curr = self._helper(nums, ind + i) 
            if curr > maxRob:
                maxRob = curr
        self.memoization[ind] = maxRob + nums[ind]
        return maxRob + nums[ind]

if __name__ == "__main__":
    nums = [2, 7, 9, 3, 1]
    s = Solution()
    print(s.rob(nums))