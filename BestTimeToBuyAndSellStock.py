class Solution:
    def maxProfit(self, prices):
        if prices == []: return 0
        self.minPrice, self.maxTotal = float("inf"), -float("inf")
        self._helper(prices)
        return self.maxTotal
    def _helper(self, prices):
        for i in range(0, len(prices)):
            self.minPrice = min(self.minPrice, prices[i])
            currTotal = prices[i] - self.minPrice
            if currTotal > self.maxTotal: self.maxTotal = currTotal

if __name__ == "__main__":
    nums = [7, 1, 5, 3, 6, 4]
    s = Solution()
    print(s.maxProfit(nums))