#
# @lc app=leetcode id=2826 lang=python3
#
# [2826] Sorting Three Groups
#

# @lc code=start
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        # Use a presents the operation to make sequence all 1s
        # Use b presents the operation to make sequence incresing from 1 to 2
        # Use c presents the operation to make sequence incresing from 1 to 3
        # Time  complexity: O(3n)
        # Space complexity: O(3)
        # a = b = c = 0
        # for num in nums:
        #     a += num != 1
        #     b = min(a, b + (num != 2))
        #     c = min(b, c + (num != 3))
        # return c


        dp = [len(nums)] * 4
        for num in nums:
            dp[num] -= 1
            dp[2] = min(dp[2], dp[1])
            dp[3] = min(dp[3], dp[2])
        return dp[3]


        
# @lc code=end

