#
# @lc app=leetcode id=2552 lang=python3
#
# [2552] Count Increasing Quadruplets
#

# @lc code=start
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:

        # Specifically, We use dp[j] stores the count of all valid triplets (i, j, k) that satisfies i < j < k and nums[i] < nums[k] < nums[j] and using the current index number as the role j.

        # Time  complexity: O(n^2)
        # Space complexity: O(n)

        n = len(nums)
        dp = [0] * n
        ans = 0

        for j in range(n):
            prev_small = 0
            for i in range(j):
                if nums[i] < nums[j]:
                    prev_small += 1
                    ans += dp[i]
                elif nums[i] > nums[j]:
                    dp[i] += prev_small

        return ans
                   
        
# @lc code=end

