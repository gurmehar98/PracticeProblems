import heapq

class Solution:
    def topKFrequent(self, nums, k):
        freqDict, freqHeap, resList = {}, [], []
        for n in nums:
            if n in freqDict.keys(): freqDict[n] += 1
            else: freqDict[n] = 1
        for key in freqDict.keys(): heapq.heappush(freqHeap, (-freqDict[key], key))
        for _ in range(0, k): resList.append(heapq.heappop(freqHeap)[1])
        return resList
      