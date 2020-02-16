#
# @lc app=leetcode id=1316 lang=python3
#
# [1316] Distinct Echo Substrings
#
# https://leetcode.com/problems/distinct-echo-substrings/description/
#
# algorithms
# Hard (45.03%)
# Likes:    38
# Dislikes: 86
# Total Accepted:    3.6K
# Total Submissions: 7.9K
# Testcase Example:  '"abcabcabc"'
#
# Return the number of distinct non-empty substrings of text that can be
# written as the concatenation of some string with itself (i.e. it can be
# written as a + a where a is some string).
# 
# 
# Example 1:
# 
# 
# Input: text = "abcabcabc"
# Output: 3
# Explanation: The 3 substrings are "abcabc", "bcabca" and "cabcab".
# 
# 
# Example 2:
# 
# 
# Input: text = "leetcodeleetcode"
# Output: 2
# Explanation: The 2 substrings are "ee" and "leetcodeleetcode".
# 
# 
# 
# Constraints:
# 
# 
# 1 <= text.length <= 2000
# text has only lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:

        res, n = set(), len(text)

        def check(i, j):
            l = j - i
            if l % 2 == 0 and text[i:i+l//2] == text[i+l//2:j]:
                return True
            return False

        for i in range(n):
            for j in range(i+1, n+1):
                if check(i, j):
                    res.add(text[i:j])

        return len(res)

        
        
# @lc code=end

