#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#
# https://leetcode.com/problems/is-subsequence/description/
#
# algorithms
# Easy (49.12%)
# Likes:    1613
# Dislikes: 204
# Total Accepted:    224K
# Total Submissions: 455.2K
# Testcase Example:  '"abc"\n"ahbgdc"'
#
# Given a string s and a string t, check if s is subsequence of t.
# 
# A subsequence of a string is a new string which is formed from the original
# string by deleting some (can be none) of the characters without disturbing
# the relative positions of the remaining characters. (ie, "ace" is a
# subsequence of "abcde" while "aec" is not).
# 
# Follow up:
# If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you
# want to check one by one to see if T has its subsequence. In this scenario,
# how would you change your code?
# 
# Credits:
# Special thanks to @pbrother for adding this problem and creating all test
# cases.
# 
# 
# Example 1:
# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:
# Input: s = "axc", t = "ahbgdc"
# Output: false
# 
# 
# Constraints:
# 
# 
# 0 <= s.length <= 100
# 0 <= t.length <= 10^4
# Both strings consists only of lowercase characters.
# 
# 
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Divide and Conquer with Greedy
        # Time  complexity: O(T)
        # Space complexity: O(T)
        # LEFT_BOUND, RIGHT_BOUND = len(s), len(t)

        # def rec_isSubsequence(left_index, right_index):
        #     if left_index == LEFT_BOUND:
        #         return True
        #     if right_index == RIGHT_BOUND:
        #         return False
        #     if s[left_index] == t[right_index]:
        #         left_index += 1
        #     right_index += 1

        #     return rec_isSubsequence(left_index, right_index)

        # return rec_isSubsequence(0, 0)


        # Tow-Pointers
        # Time  complexity: O(T)
        # Space complexity: O(1)
        # LEFT_BOUND, RIGHT_BOUND = len(s), len(t)

        # p_left = p_right = 0
        # while p_left < LEFT_BOUND and p_right < RIGHT_BOUND:
        #     if s[p_left] == t[p_right]:
        #         p_left += 1
        #     p_right += 1

        # return p_left == LEFT_BOUND


        # if not s: return True
        # i = 0
        # for char in t:
        #     if s[i] == char:
        #         i += 1

        #     if i == len(s):
        #         return True

        # return False


        # last = -1
        # for char in s:
        #     try:
        #         last = t.index(char, last + 1)
        #     except:
        #         return False
        # return True


        t = iter(t)
        return all(c in t for c in s)

        
# @lc code=end

