#
# @lc app=leetcode id=2150 lang=python3
#
# [2150] Find All Lonely Numbers in the Array
#

# @lc code=start
from collections import Counter

class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        m = Counter(nums)
        return [n for n in nums if m[n] == 1 and m[n + 1] + m[n - 1] == 0]
        
# @lc code=end

