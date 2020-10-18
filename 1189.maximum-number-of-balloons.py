#
# @lc app=leetcode id=1189 lang=python3
#
# [1189] Maximum Number of Balloons
#
# https://leetcode.com/problems/maximum-number-of-balloons/description/
#
# algorithms
# Easy (61.13%)
# Likes:    361
# Dislikes: 40
# Total Accepted:    45.1K
# Total Submissions: 72.9K
# Testcase Example:  '"nlaebolko"'
#
# Given a string text, you want to use the characters of text to form as many
# instances of the word "balloon" as possible.
# 
# You can use each character in text at most once. Return the maximum number of
# instances that can be formed.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: text = "nlaebolko"
# Output: 1
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: text = "loonbalxballpoon"
# Output: 2
# 
# 
# Example 3:
# 
# 
# Input: text = "leetcode"
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# 1 <= text.length <= 10^4
# text consists of lower case English letters only.
# 
#

# @lc code=start
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        return min(text.count(c) // "balloon".count(c) for c in set("balloon"))
        
# @lc code=end

