#
# @lc app=leetcode id=3309 lang=python3
#
# [3309] Maximum Possible Number by Binary Concatenation
#

# @lc code=start
class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:

        def cmp(a, b):
            if a + b > b + a:
                return -1
            return 1

        nums = [bin(num)[2:] for num in nums]
        nums.sort(key=cmp_to_key(cmp))

        ans = ''.join(nums)
        return int(ans, 2)
            
        
# @lc code=end

