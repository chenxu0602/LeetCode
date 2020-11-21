#
# @lc app=leetcode id=1437 lang=python3
#
# [1437] Check If All 1's Are at Least Length K Places Away
#
# https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/description/
#
# algorithms
# Medium (61.93%)
# Likes:    103
# Dislikes: 108
# Total Accepted:    20K
# Total Submissions: 32.3K
# Testcase Example:  '[1,0,0,0,1,0,0,1]\r\n2\r'
#
# Given an array nums of 0s and 1s and an integer k, return True if all 1's are
# at least k places away from each other, otherwise return False.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: nums = [1,0,0,0,1,0,0,1], k = 2
# Output: true
# Explanation: Each of the 1s are at least 2 places away from each other.
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: nums = [1,0,0,1,0,1], k = 2
# Output: false
# Explanation: The second 1 and third 1 are only one apart from each other.
# 
# Example 3:
# 
# 
# Input: nums = [1,1,1,1,1], k = 0
# Output: true
# 
# 
# Example 4:
# 
# 
# Input: nums = [0,1,0,1], k = 1
# Output: true
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# 0 <= k <= nums.length
# nums[i] is 0 or 1
# 
# 
#

# @lc code=start
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if k == 0: return True
        if not nums: return False
        if not any(nums): return True
        l, r = nums.index(1), ''.join(map(str, nums)).rindex('1')
        nums = nums[l:r + 1]
        return all((len(list(v)) == 1 if i == 1 else True) \
            and (len(list(v)) >= k if i == 0 else True) \
            for i, v in itertools.groupby(nums))
        
# @lc code=end

