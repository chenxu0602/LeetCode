#
# @lc app=leetcode id=670 lang=python3
#
# [670] Maximum Swap
#
# https://leetcode.com/problems/maximum-swap/description/
#
# algorithms
# Medium (41.57%)
# Likes:    739
# Dislikes: 54
# Total Accepted:    50.6K
# Total Submissions: 121.6K
# Testcase Example:  '2736'
#
# 
# Given a non-negative integer, you could swap two digits at most once to get
# the maximum valued number. Return the maximum valued number you could get.
# 
# 
# Example 1:
# 
# Input: 2736
# Output: 7236
# Explanation: Swap the number 2 and the number 7.
# 
# 
# 
# Example 2:
# 
# Input: 9973
# Output: 9973
# Explanation: No swap.
# 
# 
# 
# 
# Note:
# 
# The given number is in the range [0, 10^8]
# 
# 
#

# @lc code=start
class Solution:
    def maximumSwap(self, num: int) -> int:
        # Greedy
        # Time  complexity: O(N) where N is the total number of digits in the input number
        # Space complexity: O(N)
        A = list(map(int, str(num)))
        last = {x: i for i, x in enumerate(A)}
        for i, x in enumerate(A):
            for d in range(9, x, -1):
                if last.get(d, -1) > i:
                    A[i], A[last[d]] = A[last[d]], A[i]
                    return int(''.join(map(str, A)))

        return num
        
# @lc code=end

