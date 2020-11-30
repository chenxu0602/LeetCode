#
# @lc app=leetcode id=1544 lang=python3
#
# [1544] Make The String Great
#
# https://leetcode.com/problems/make-the-string-great/description/
#
# algorithms
# Easy (54.73%)
# Likes:    251
# Dislikes: 27
# Total Accepted:    22.3K
# Total Submissions: 40.8K
# Testcase Example:  '"leEeetcode"'
#
# Given a string s of lower and upper case English letters.
# 
# A good string is a string which doesn't have two adjacent characters s[i] and
# s[i + 1] where:
# 
# 
# 0 <= i <= s.length - 2
# s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case
# or vice-versa.
# 
# 
# To make the string good, you can choose two adjacent characters that make the
# string bad and remove them. You can keep doing this until the string becomes
# good.
# 
# Return the string after making it good. The answer is guaranteed to be unique
# under the given constraints.
# 
# Notice that an empty string is also good.
# 
# 
# Example 1:
# 
# 
# Input: s = "leEeetcode"
# Output: "leetcode"
# Explanation: In the first step, either you choose i = 1 or i = 2, both will
# result "leEeetcode" to be reduced to "leetcode".
# 
# 
# Example 2:
# 
# 
# Input: s = "abBAcC"
# Output: ""
# Explanation: We have many possible scenarios, and all lead to the same
# answer. For example:
# "abBAcC" --> "aAcC" --> "cC" --> ""
# "abBAcC" --> "abBA" --> "aA" --> ""
# 
# 
# Example 3:
# 
# 
# Input: s = "s"
# Output: "s"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 100
# s contains only lower and upper case English letters.
# 
#

# @lc code=start
class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and abs(ord(stack[-1]) - ord(c)) == 32:
                stack.pop()
            else:
                stack.append(c)

        return "".join(stack)
        
# @lc code=end

