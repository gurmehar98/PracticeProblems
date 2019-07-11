class Solution:
    def countBits(self, num):
        self.count, self.memoization, self.resList = 0, {}, []
        self.resList.append(0)
        for i in range(num + 1): self._helper(i)
        return self.resList
    def _helper(self, num):
        if num == 0: return 0
        if num % 2 == 1 or num == 1: self.count += 1
        self._helper(num // 2)
        if self.count > 0: self.resList.append(self.count)
        self.count = 0

if __name__ == "__main__":
    num = 2
    s = Solution()
    print(s.countBits(num))