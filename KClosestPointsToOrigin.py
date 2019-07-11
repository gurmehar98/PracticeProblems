import heapq
class Solution:
    def kClosest(self, points, K):
        return heapq.nsmallest(K, points, lambda x: x[0] ** 2 + x[1] ** 2)

if __name__ == "__main__":
    points, K = [[1,3],[-2,2]], 1
    obj = Solution()
    print(obj.kClosest(points, K))