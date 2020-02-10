#
# @lc app=leetcode id=1167 lang=python3
#
# [1167] Minimum Cost to Connect Sticks
#
# https://leetcode.com/problems/minimum-cost-to-connect-sticks/description/
#
# algorithms
# Medium (61.44%)
# Likes:    171
# Dislikes: 51
# Total Accepted:    14.2K
# Total Submissions: 23K
# Testcase Example:  '[2,4,3]'
#
# You have some sticks with positive integer lengths.
# 
# You can connect any two sticks of lengths X and Y into one stick by paying a
# cost of X + Y.  You perform this action until there is one stick remaining.
# 
# Return the minimum cost of connecting all the given sticks into one stick in
# this way.
# 
# 
# Example 1:
# Input: sticks = [2,4,3]
# Output: 14
# Example 2:
# Input: sticks = [1,8,3,5]
# Output: 30
# 
# 
# Constraints:
# 
# 
# 1 <= sticks.length <= 10^4
# 1 <= sticks[i] <= 10^4
# 
# 
#

# @lc code=start

import heapq

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:

        heapq.heapify(sticks)
        res = 0
        while len(sticks) > 1:
            x, y = heapq.heappop(sticks), heapq.heappop(sticks)
            res += (x + y)
            heapq.heappush(sticks, x + y)
        return res
        
# @lc code=end

