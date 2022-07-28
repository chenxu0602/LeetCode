#
# @lc app=leetcode id=2341 lang=python3
#
# [2341] Maximum Number of Pairs in Array
#

# @lc code=start
from collections import Counter

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        ans = [0, 0]
        for v in cnt.values():
            ans[0] += v // 2
            ans[1] += v % 2
        return ans
        
# @lc code=end

