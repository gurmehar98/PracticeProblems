class Solution:
    def frequencySort(self, s):
        inpSet, resList = set(s), []
        for val in inpSet: resList.append((val, s.count(val)))
        resList.sort(key = lambda x: x[1], reverse = True) 
        return "".join(map(lambda x: x[0] * x[1], resList))