#
# @lc app=leetcode id=2784 lang=python3
#
# [2784] Check if Array is Good
#

# @lc code=start
class Solution:
    def isGood(self, nums: List[int]) -> bool:

        xor = 0
        n = len(nums) - 1
        numN = 0

        for i in range(1, n):
            xor ^= i

        for i in range(len(nums)):
            if nums[i] > n:
                return False 
            elif nums[i] == n:
                numN += 1
            else:
                xor ^= nums[i]

        return xor == 0 and numN == 2

            
        
# @lc code=end

