#
# @lc app=leetcode id=2226 lang=python3
#
# [2226] Maximum Candies Allocated to K Children
#

# @lc code=start
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        left, right = 0, sum(candies) // k
        while left < right:
            mid = (left + right + 1) // 2
            if sum(x // mid for x in candies) >= k:
                left = mid
            else:
                right = mid - 1

        return left
        
# @lc code=end

