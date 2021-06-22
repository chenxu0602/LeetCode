#
# @lc app=leetcode id=1869 lang=python3
#
# [1869] Longer Contiguous Segments of Ones than Zeros
#
# https://leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros/description/
#
# algorithms
# Easy (59.57%)
# Likes:    145
# Dislikes: 6
# Total Accepted:    17.9K
# Total Submissions: 30.1K
# Testcase Example:  '"1101"'
#
# Given a binary string s, return true if the longest contiguous segment of 1s
# is strictly longer than the longest contiguous segment of 0s in s. Return
# false otherwise.
# 
# 
# For example, in s = "110100010" the longest contiguous segment of 1s has
# length 2, and the longest contiguous segment of 0s has length 3.
# 
# 
# Note that if there are no 0s, then the longest contiguous segment of 0s is
# considered to have length 0. The same applies if there are no 1s.
# 
# 
# Example 1:
# 
# 
# Input: s = "1101"
# Output: true
# Explanation:
# The longest contiguous segment of 1s has length 2: "1101"
# The longest contiguous segment of 0s has length 1: "1101"
# The segment of 1s is longer, so return true.
# 
# 
# Example 2:
# 
# 
# Input: s = "111000"
# Output: false
# Explanation:
# The longest contiguous segment of 1s has length 3: "111000"
# The longest contiguous segment of 0s has length 3: "111000"
# The segment of 1s is not longer, so return false.
# 
# 
# Example 3:
# 
# 
# Input: s = "110100010"
# Output: false
# Explanation:
# The longest contiguous segment of 1s has length 2: "110100010"
# The longest contiguous segment of 0s has length 3: "110100010"
# The segment of 1s is not longer, so return false.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 100
# s[i] is either '0' or '1'.
# 
# 
#

# @lc code=start
class Solution:
    def checkZeroOnes(self, s: str) -> bool:

        best_one, best_zero, current_one, current_zero = 0, 0, 0, 0

        for i in s:
            if i == '1':
                current_zero = 0
                current_one += 1
            else:
                current_zero += 1
                current_one = 0

            best_one = max(best_one, current_one)
            best_zero = max(best_zero, current_zero)

        return best_one > best_zero
        
# @lc code=end

