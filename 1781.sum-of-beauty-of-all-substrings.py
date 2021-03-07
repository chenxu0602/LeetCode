#
# @lc app=leetcode id=1781 lang=python3
#
# [1781] Sum of Beauty of All Substrings
#
# https://leetcode.com/problems/sum-of-beauty-of-all-substrings/description/
#
# algorithms
# Medium (42.96%)
# Likes:    51
# Dislikes: 38
# Total Accepted:    3.4K
# Total Submissions: 7.9K
# Testcase Example:  '"aabcb"'
#
# The beauty of a string is the difference in frequencies between the most
# frequent and least frequent characters.
# 
# 
# For example, the beauty of "abaacc" is 3 - 1 = 2.
# 
# 
# Given a string s, return the sum of beauty of all of its substrings.
# 
# 
# Example 1:
# 
# 
# Input: s = "aabcb"
# Output: 5
# Explanation: The substrings with non-zero beauty are
# ["aab","aabc","aabcb","abcb","bcb"], each with beauty equal to 1.
# 
# Example 2:
# 
# 
# Input: s = "aabcbaa"
# Output: 17
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <=^ 500
# s consists of only lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def beautySum(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            freq = [0] * 26
            for j in range(i, len(s)):
                freq[ord(s[j]) - ord('a')] += 1
                ans += max(freq) - min(x for x in freq if x)

        return ans
        
# @lc code=end

