class Solution:
    def climbStairs(self, n):
        ind, self.memoization = 0,  {}
        return self._helper(n, ind)
    def _helper(self, n, ind):
        if ind > n: return 0
        if ind == n: return 1
        if ind in self.memoization.keys(): return self.memoization[ind]
        oneS, twoS = self._helper(n, ind + 1), self._helper(n, ind + 2)
        self.memoization[ind] = oneS + twoS
        return oneS + twoS

if __name__ == "__main__":
    n = 3
    s = Solution()
    print(s.climbStairs(n))