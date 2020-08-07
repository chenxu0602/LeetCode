#
# @lc app=leetcode id=275 lang=python3
#
# [275] H-Index II
#
# https://leetcode.com/problems/h-index-ii/description/
#
# algorithms
# Medium (35.91%)
# Likes:    447
# Dislikes: 716
# Total Accepted:    129.5K
# Total Submissions: 360.4K
# Testcase Example:  '[0,1,3,5,6]'
#
# Given an array of citations sorted in ascending order (each citation is a
# non-negative integer) of a researcher, write a function to compute the
# researcher's h-index.
# 
# According to the definition of h-index on Wikipedia: "A scientist has index h
# if h of his/her N papers have at least h citations each, and the other N − h
# papers have no more than h citations each."
# 
# Example:
# 
# 
# Input: citations = [0,1,3,5,6]
# Output: 3 
# Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each
# of them had 
# ⁠            received 0, 1, 3, 5, 6 citations respectively. 
# Since the researcher has 3 papers with at least 3 citations each and the
# remaining 
# two with no more than 3 citations each, her h-index is 3.
# 
# Note:
# 
# If there are several possible values for h, the maximum one is taken as the
# h-index.
# 
# Follow up:
# 
# 
# This is a follow up problem to H-Index, where citations is now guaranteed to
# be sorted in ascending order.
# Could you solve it in logarithmic time complexity?
# 
# 
#

# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # Time  complexity: O(logN)
        # Space complexity: O(1)
        n = len(citations)
        left, right = 0, n - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if citations[pivot] == n - pivot:
                return n - pivot
            elif citations[pivot] < n - pivot:
                left = pivot + 1
            else:
                right = pivot - 1

        return n - left
        
# @lc code=end

