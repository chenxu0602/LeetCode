#
# @lc app=leetcode id=1151 lang=python3
#
# [1151] Minimum Swaps to Group All 1's Together
#
# https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/description/
#
# algorithms
# Medium (54.69%)
# Likes:    59
# Dislikes: 0
# Total Accepted:    2.4K
# Total Submissions: 4.2K
# Testcase Example:  '[1,0,1,0,1]'
#
# Given a binary array data, return the minimum number of swaps required to
# group all 1’s present in the array together in any place in the array.
# 
# 
# 
# Example 1:
# 
# 
# Input: [1,0,1,0,1]
# Output: 1
# Explanation: 
# There are 3 ways to group all 1's together:
# [1,1,1,0,0] using 1 swap.
# [0,1,1,1,0] using 2 swaps.
# [0,0,1,1,1] using 1 swap.
# The minimum is 1.
# 
# 
# Example 2:
# 
# 
# Input: [0,0,0,1,0]
# Output: 0
# Explanation: 
# Since there is only one 1 in the array, no swaps needed.
# 
# 
# Example 3:
# 
# 
# Input: [1,0,1,0,1,0,0,1,1,0,1]
# Output: 3
# Explanation: 
# One possible solution that uses 3 swaps is [0,0,0,0,0,1,1,1,1,1,1].
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= data.length <= 10^5
# 0 <= data[i] <= 1
# 
# 
#

# @lc code=start
class Solution:
    def minSwaps(self, data: List[int]) -> int:
        l = data.count(1)
        mn = cur = data[:l].count(0)
        for i in range(l, len(data)):
            cur += not data[i]
            cur -= not data[i-l]
            mn = min(mn, cur)
        return mn
        
# @lc code=end

