#
# @lc app=leetcode id=3013 lang=python3
#
# [3013] Divide an Array Into Subarrays With Minimum Cost II
#

# @lc code=start
from sortedcontainers import SortedList

class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:

        k -= 2
        rem = float('inf')
        window = SortedList(nums[1:1 + dist])
        window_sum = sum(window[:k])

        for i in range(1, len(nums) - dist):
            window.add(nums[i + dist])
            window_sum += min(window[k], nums[i + dist])

            rem = min(rem, window_sum)

            window_sum -= min(window[k], nums[i])
            window.remove(nums[i])

        return nums[0] + rem
        
# @lc code=end

