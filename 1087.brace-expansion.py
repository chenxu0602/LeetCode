#
# @lc app=leetcode id=1087 lang=python3
#
# [1087] Brace Expansion
#
# https://leetcode.com/problems/brace-expansion/description/
#
# algorithms
# Medium (62.73%)
# Likes:    270
# Dislikes: 31
# Total Accepted:    22.7K
# Total Submissions: 36.1K
# Testcase Example:  '"{a,b}c{d,e}f"'
#
# A string S represents a list of words.
# 
# Each letter in the word has 1 or more options.  If there is one option, the
# letter is represented as is.  If there is more than one option, then curly
# braces delimit the options.  For example, "{a,b,c}" represents options ["a",
# "b", "c"].
# 
# For example, "{a,b,c}d{e,f}" represents the list ["ade", "adf", "bde", "bdf",
# "cde", "cdf"].
# 
# Return all words that can be formed in this manner, in lexicographical
# order.
# 
# 
# 
# Example 1:
# 
# 
# Input: "{a,b}c{d,e}f"
# Output: ["acdf","acef","bcdf","bcef"]
# 
# 
# Example 2:
# 
# 
# Input: "abcd"
# Output: ["abcd"]
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= S.length <= 50
# There are no nested curly brackets.
# All characters inside a pair of consecutive opening and ending curly brackets
# are different.
# 
# 
#

# @lc code=start
import itertools

class Solution:
    def expand(self, S: str) -> List[str]:
        A = S.replace('{', ' ').replace('}', ' ').strip().split(' ')
        B = [sorted(a.split(',')) for a in A]
        return ["".join(c) for c in itertools.product(*B)]
        
# @lc code=end

