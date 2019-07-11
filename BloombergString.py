from itertools import groupby

class Solution(object):
    def removeDuplicates(self, inpStr):
        return self._helper(inpStr)
    def _helper(self, inpStr):
        result = []
        for (_, group) in groupby(inpStr):
            groupList = list(group)
            if len(groupList) < 3:
                for i in range(len(groupList)):
                    result.append(groupList[i])
        if inpStr == "".join(result): return inpStr
        return self._helper("".join(result))

if __name__ == "__main__" :
    inpStr = "aabbbccddddc"
    s = Solution()
    print(s.removeDuplicates(inpStr))