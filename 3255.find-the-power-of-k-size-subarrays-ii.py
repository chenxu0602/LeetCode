#
# @lc app=leetcode id=3255 lang=python3
#
# [3255] Find the Power of K-Size Subarrays II
#

# @lc code=start
from itertools import accumulate

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:

        consecutive = [a - b == 1 for a, b in zip(nums[1:], nums)]

        acc = list(accumulate(consecutive, lambda x, y: x + y if y == 1 else 1, initial=1))
        return [num if cnt >= k else -1 for num, cnt in zip(nums[k - 1:], acc[k - 1:])]
        
# @lc code=end

