#
# @lc app=leetcode id=1726 lang=python3
#
# [1726] Tuple with Same Product
#
# https://leetcode.com/problems/tuple-with-same-product/description/
#
# algorithms
# Medium (54.84%)
# Likes:    153
# Dislikes: 9
# Total Accepted:    9.6K
# Total Submissions: 17.4K
# Testcase Example:  '[2,3,4,6]'
#
# Given an array nums of distinct positive integers, return the number of
# tuples (a, b, c, d) such that a * b = c * d where a, b, c, and d are elements
# of nums, and a != b != c != d.
# 
# 
# Example 1:
# 
# 
# Input: nums = [2,3,4,6]
# Output: 8
# Explanation: There are 8 valid tuples:
# (2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
# (3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,2,4,5,10]
# Output: 16
# Explanation: There are 16 valids tuples:
# (1,10,2,5) , (1,10,5,2) , (10,1,2,5) , (10,1,5,2)
# (2,5,1,10) , (2,5,10,1) , (5,2,1,10) , (5,2,10,1)
# (2,10,4,5) , (2,10,5,4) , (10,2,4,5) , (10,2,4,5)
# (4,5,2,10) , (4,5,10,2) , (5,4,2,10) , (5,4,10,2)
# 
# 
# Example 3:
# 
# 
# Input: nums = [2,3,4,6,8,12]
# Output: 40
# 
# 
# Example 4:
# 
# 
# Input: nums = [2,3,5,7]
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 10^4
# All elements in nums are distinct.
# 
#

# @lc code=start
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        # TLE
        # ans = 0
        # nums.sort()
        # for i in range(len(nums) - 3):
        #     for j in range(i + 3, len(nums)):
        #         target = nums[i] * nums[j]
        #         c, d = i + 1, j - 1
        #         while c < d:
        #             tmp = nums[c] * nums[d]
        #             if tmp < target:
        #                 c += 1
        #             elif tmp > target:
        #                 d -= 1
        #             else:
        #                 ans += 1
        #                 c += 1; d -= 1

        # return ans * 8


        ans, freq = 0, {}
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                key = nums[i] * nums[j]
                ans += freq.get(key, 0)
                freq[key] = 1 + freq.get(key, 0)

        return ans * 8

                    
                


        
# @lc code=end

