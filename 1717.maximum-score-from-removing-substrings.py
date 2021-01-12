#
# @lc app=leetcode id=1717 lang=python3
#
# [1717] Maximum Score From Removing Substrings
#
# https://leetcode.com/problems/maximum-score-from-removing-substrings/description/
#
# algorithms
# Medium (35.58%)
# Likes:    128
# Dislikes: 11
# Total Accepted:    3.3K
# Total Submissions: 9.2K
# Testcase Example:  '"cdbcbbaaabab"\n4\n5'
#
# You are given a string s and two integers x and y. You can perform two types
# of operations any number of times.
# 
# 
# Remove substring "ab" and gain x points.
# 
# 
# For example, when removing "ab" from "cabxbae" it becomes
# "cxbae".
# 
# 
# Remove substring "ba" and gain y points.
# 
# For example, when removing "ba" from "cabxbae" it becomes
# "cabxe".
# 
# 
# 
# 
# Return the maximum points you can gain after applying the above operations on
# s.
# 
# 
# Example 1:
# 
# 
# Input: s = "cdbcbbaaabab", x = 4, y = 5
# Output: 19
# Explanation:
# - Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5
# points are added to the score.
# - Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4
# points are added to the score.
# - Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points
# are added to the score.
# - Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are
# added to the score.
# Total score = 5 + 4 + 5 + 5 = 19.
# 
# Example 2:
# 
# 
# Input: s = "aabbaaxybbaabb", x = 5, y = 4
# Output: 20
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^5
# 1 <= x, y <= 10^4
# s consists of lowercase English letters.
# 
# 
#

# @lc code=start
from collections import Counter

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        # If 'ab' (x) gains more, we will use 'ab' whenever we see it, and when we see 'ba', keep it in Counter for now, b
        # Time  complexity: O(N)
        # Space complexity: O(1)
        a, b = 'a', 'b'
        if x < y:
            x, y = y, x
            a, b = b, a

        seen = Counter()
        ans = 0

        for c in s + 'x':
            if c in 'ab':
                if c == b and seen[a] > 0:
                    ans += x
                    seen[a] -= 1
                else:
                    seen[c] += 1
            else:
                ans += y * min(seen[a], seen[b])
                seen = Counter()

        return ans
        
# @lc code=end

