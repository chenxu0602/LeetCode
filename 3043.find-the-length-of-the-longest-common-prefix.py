#
# @lc app=leetcode id=3043 lang=python3
#
# [3043] Find the Length of the Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:

        res = 0
        s1 = set()
        for a in arr1:
            s = str(a)
            for i in range(1, len(s) + 1):
                s1.add(s[:i])

        s2 = set()
        for a in arr2:
            s = str(a)
            for i in range(1, len(s) + 1):
                s2.add(s[:i])

        for s in s1:
            if s in s2:
                res = max(res, len(s))

        return res
        
# @lc code=end

