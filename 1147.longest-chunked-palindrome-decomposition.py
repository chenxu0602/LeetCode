#
# @lc app=leetcode id=1147 lang=python3
#
# [1147] Longest Chunked Palindrome Decomposition
#
# https://leetcode.com/problems/longest-chunked-palindrome-decomposition/description/
#
# algorithms
# Hard (58.71%)
# Likes:    90
# Dislikes: 8
# Total Accepted:    5.3K
# Total Submissions: 9K
# Testcase Example:  '"ghiabcdefhelloadamhelloabcdefghi"'
#
# Return the largest possible k such that there exists a_1, a_2, ..., a_k such
# that:
# 
# 
# Each a_i is a non-empty string;
# Their concatenation a_1 + a_2 + ... + a_k is equal to text;
# For all 1 <= i <= k,  a_i = a_{k+1 - i}.
# 
# 
# 
# Example 1:
# 
# 
# Input: text = "ghiabcdefhelloadamhelloabcdefghi"
# Output: 7
# Explanation: We can split the string on
# "(ghi)(abcdef)(hello)(adam)(hello)(abcdef)(ghi)".
# 
# 
# Example 2:
# 
# 
# Input: text = "merchant"
# Output: 1
# Explanation: We can split the string on "(merchant)".
# 
# 
# Example 3:
# 
# 
# Input: text = "antaprezatepzapreanta"
# Output: 11
# Explanation: We can split the string on
# "(a)(nt)(a)(pre)(za)(tpe)(za)(pre)(a)(nt)(a)".
# 
# 
# Example 4:
# 
# 
# Input: text = "aaa"
# Output: 3
# Explanation: We can split the string on "(a)(a)(a)".
# 
# 
# 
# Constraints:
# 
# 
# text consists only of lowercase English characters.
# 1 <= text.length <= 1000
# 
#

# @lc code=start
class Solution:
    def longestDecomposition(self, text: str, res: int = 0) -> int:
        n = len(text)
        for l in range(1, n//2+1):
            if text[0] == text[n-l] and text[l-1] == text[n-1]:
                if text[:l] == text[n-l:]:
                    return self.longestDecomposition(text[l:n-l], res+2)

        return res+1 if text else res


        
        
# @lc code=end

