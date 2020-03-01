#
# @lc app=leetcode id=315 lang=python3
#
# [315] Count of Smaller Numbers After Self
#
# https://leetcode.com/problems/count-of-smaller-numbers-after-self/description/
#
# algorithms
# Hard (40.61%)
# Likes:    1759
# Dislikes: 69
# Total Accepted:    107.8K
# Total Submissions: 265.2K
# Testcase Example:  '[5,2,6,1]'
#
# You are given an integer array nums and you have to return a new counts
# array. The counts array has the property where counts[i] is the number of
# smaller elements to the right of nums[i].
# 
# Example:
# 
# 
# Input: [5,2,6,1]
# Output: [2,1,1,0] 
# Explanation:
# To the right of 5 there are 2 smaller elements (2 and 1).
# To the right of 2 there is only 1 smaller element (1).
# To the right of 6 there is 1 smaller element (1).
# To the right of 1 there is 0 smaller element.
# 
#

# @lc code=start
import bisect

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        result, sortedList = [], []
        for num in nums[::-1]:
            p = bisect.bisect_left(sortedList, num)
            result.append(p)
            bisect.insort_left(sortedList, num)
        return result[::-1]
        
# @lc code=end

