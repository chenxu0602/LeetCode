#
# @lc app=leetcode id=2963 lang=python3
#
# [2963] Count the Number of Good Partitions
#

# @lc code=start
class Solution:
    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        
        MOD = 10**9 + 7

        last = {v: i for i, v in enumerate(nums)}
        rightmost = p = -1
        for i, v in enumerate(nums):
            if rightmost < i: p += 1
            rightmost = max(rightmost, last[v])

        return pow(2, p, MOD)

# @lc code=end

