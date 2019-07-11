class NumArray:
    def __init__(self, nums):
        self.accumulator = [0]
        for num in nums: 
            self.accumulator += [self.accumulator[-1] + num]  
    def sumRange(self, i, j):
        return self.accumulator[j + 1] - self.accumulator[i]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

if __name__ == "__main__":
    nums = [-2, 0, 3, -5, 2, -1]
    obj = NumArray(nums)
    i, j = 0, 5
    print(obj.sumRange(i, j))