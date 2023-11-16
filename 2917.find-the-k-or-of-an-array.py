#
# @lc app=leetcode id=2917 lang=python3
#
# [2917] Find the K-or of an Array
#

# @lc code=start
from itertools import zip_longest

class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:

        nums = zip_longest(*map(lambda x: bin(x)[-1:1:-1], nums), fillvalue='0')

        return sum(1 << i for i, v in enumerate(nums) if v.count('1') >= k)
        
# @lc code=end

