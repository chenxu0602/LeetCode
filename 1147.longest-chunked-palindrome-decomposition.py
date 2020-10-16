#
# @lc app=leetcode id=1147 lang=python3
#
# [1147] Longest Chunked Palindrome Decomposition
#
# https://leetcode.com/problems/longest-chunked-palindrome-decomposition/description/
#
# algorithms
# Hard (58.59%)
# Likes:    214
# Dislikes: 12
# Total Accepted:    10.4K
# Total Submissions: 17.6K
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
    res = 0
    def longestDecomposition(self, text: str, res: int = 0) -> int:
        # Time  complexity: O(N x len(string))
        # Space complexity: O(N)
        # n = len(text)
        # for l in range(1, n // 2 + 1):
        #     if text[0] == text[n-l] and text[l-1] == text[n-1]:
        #         if text[:l] == text[n-l:]:
        #             return self.longestDecomposition(text[l:n - l], res + 2)
        # return res + 1 if text else res


        S = text
        res, l, r = 0, "", ""
        for i, j in zip(S, S[::-1]):
            l, r = l + i, j + r
            if l == r:
                res, l, r = res + 1, "", ""
        return res



        
# @lc code=end

