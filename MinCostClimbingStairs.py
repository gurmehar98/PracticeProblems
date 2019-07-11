class Solution:
    def minCostClimbingStairs(self, cost):
        ind1, ind2, self.memoization = 0, 1, {}
        return min(self._helper(cost, ind1), self._helper(cost, ind2))
    def _helper(self, cost, ind):
        if ind >= len(cost): return 0 
        if ind in self.memoization.keys(): return self.memoization[ind]
        oneS = self._helper(cost, ind + 1)
        twoS = self._helper(cost, ind + 2)
        self.memoization[ind] = min(oneS, twoS) + cost[ind]
        return min(oneS, twoS) + cost[ind]

if __name__ == "__main__":
    cost = [10, 15, 20]
    s = Solution()
    print(s.minCostClimbingStairs(cost))