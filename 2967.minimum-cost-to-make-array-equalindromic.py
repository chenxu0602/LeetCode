#
# @lc app=leetcode id=2967 lang=python3
#
# [2967] Minimum Cost to Make Array Equalindromic
#

# @lc code=start
class Solution:
    def minimumCost(self, nums: List[int]) -> int:

        nums.sort()
        pal = lambda x: str(x) == str(x)[::-1]
        left = right = nums[len(nums) // 2]

        while not pal(left): left -= 1
        while not pal(right): right += 1

        return min(sum(map(lambda x: abs(x - left), nums)), sum(map(lambda x: abs(x - right), nums)))
        
# @lc code=end

