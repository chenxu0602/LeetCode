#
# @lc app=leetcode id=1653 lang=python3
#
# [1653] Minimum Deletions to Make String Balanced
#
# https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/description/
#
# algorithms
# Medium (47.80%)
# Likes:    189
# Dislikes: 6
# Total Accepted:    4.8K
# Total Submissions: 9.8K
# Testcase Example:  '"aababbab"'
#
# You are given a string s consisting only of characters 'a' and 'b'​​​​.
# 
# You can delete any number of characters in s to make s balanced. s is
# balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b'
# and s[j]= 'a'.
# 
# Return the minimum number of deletions needed to make s balanced.
# 
# 
# Example 1:
# 
# 
# Input: s = "aababbab"
# Output: 2
# Explanation: You can either:
# Delete the characters at 0-indexed positions 2 and 6 ("aababbab" ->
# "aaabbb"), or
# Delete the characters at 0-indexed positions 3 and 6 ("aababbab" ->
# "aabbbb").
# 
# 
# Example 2:
# 
# 
# Input: s = "bbaaaaabb"
# Output: 2
# Explanation: The only solution is to delete the first two characters.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^5
# s[i] is 'a' or 'b'​​.
# 
# 
#

# @lc code=start
class Solution:
    def minimumDeletions(self, s: str) -> int:
        # stack, res = [], 0
        # for c in s:
        #     if stack and c < stack[-1]:
        #         stack.pop()
        #         res += 1
        #     else:
        #         stack.append(c)
        # return res


        l = len(s)
        # dp stores number of chars to remove to make s.substring(0, i) valid
        dp = [0] * (l + 1)
        bcount = 0
        for i in range(l):
            if s[i] == 'a':
                # case 1: keep current a. ==> prev chars must be a...a
                # so need to remove all 'b' chars before i, which is bcount
                
                # case 2: remove current a ==> prev chars must be a...ab...b
                # so need to remove current a and whatever makes substring before current i valid which is dp[i];
                dp[i + 1] = min(dp[i] + 1,  bcount)
            else:
                # it's always valid to append 'b'.
                dp[i + 1] = dp[i]
                bcount += 1
        return dp[l]
        
# @lc code=end

