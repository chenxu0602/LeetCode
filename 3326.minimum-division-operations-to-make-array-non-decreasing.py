#
# @lc app=leetcode id=3326 lang=python3
#
# [3326] Minimum Division Operations to Make Array Non Decreasing
#

# @lc code=start
class Solution:
    def minOperations(self, nums: List[int]) -> int:

        def findNum(n1, n2):
            for i in range(2, n1 + 1):
                if n2 % i == 0:
                    return i
            return -1

        ans = 0
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] < nums[i - 1]:
                nums[i - 1] = findNum(nums[i], nums[i - 1])
                if nums[i - 1] == -1: 
                    return -1
                ans += 1

        return ans
        
# @lc code=end

