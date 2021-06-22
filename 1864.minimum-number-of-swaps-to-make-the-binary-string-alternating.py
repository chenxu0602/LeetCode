#
# @lc app=leetcode id=1864 lang=python3
#
# [1864] Minimum Number of Swaps to Make the Binary String Alternating
#
# https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-binary-string-alternating/description/
#
# algorithms
# Medium (36.17%)
# Likes:    178
# Dislikes: 20
# Total Accepted:    8.6K
# Total Submissions: 23.7K
# Testcase Example:  '"111000"'
#
# Given a binary string s, return the minimum number of character swaps to make
# it alternating, or -1 if it is impossible.
# 
# The string is called alternating if no two adjacent characters are equal. For
# example, the strings "010" and "1010" are alternating, while the string
# "0100" is not.
# 
# Any two characters may be swapped, even if they are not adjacent.
# 
# 
# Example 1:
# 
# 
# Input: s = "111000"
# Output: 1
# Explanation: Swap positions 1 and 4: "111000" -> "101010"
# The string is now alternating.
# 
# 
# Example 2:
# 
# 
# Input: s = "010"
# Output: 0
# Explanation: The string is already alternating, no swaps are needed.
# 
# 
# Example 3:
# 
# 
# Input: s = "1110"
# Output: -1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 1000
# s[i] is either '0' or '1'.
# 
# 
#

# @lc code=start
class Solution:
    def minSwaps(self, s: str) -> int:

        def helper(s, c):
            swaps = 0
            for ch in s:
                if ch != c:
                    swaps += 1

                c = str(int(c) ^ 1)

            return swaps // 2

        n = len(s)
        ones = zero = 0
        for c in s:
            if c == '1':
                ones += 1
            else:
                zero += 1

        if abs(ones - zero) > 1:
            return -1

        if ones > zero:
            return helper(s, '1')
        elif zero > ones:
            return helper(s, '0')

        return min(helper(s, '1'), helper(s, '0'))
        
        
# @lc code=end

