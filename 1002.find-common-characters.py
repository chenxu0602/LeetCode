#
# @lc app=leetcode id=1002 lang=python3
#
# [1002] Find Common Characters
#
# https://leetcode.com/problems/find-common-characters/description/
#
# algorithms
# Easy (67.67%)
# Likes:    1034
# Dislikes: 119
# Total Accepted:    79.6K
# Total Submissions: 117.5K
# Testcase Example:  '["bella","label","roller"]'
#
# Given an array A of strings made only from lowercase letters, return a list
# of all characters that show up in all strings within the list (including
# duplicates).  For example, if a character occurs 3 times in all strings but
# not 4 times, you need to include that character three times in the final
# answer.
# 
# You may return the answer in any order.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: ["bella","label","roller"]
# Output: ["e","l","l"]
# 
# 
# 
# Example 2:
# 
# 
# Input: ["cool","lock","cook"]
# Output: ["c","o"]
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 100
# 1 <= A[i].length <= 100
# A[i][j] is a lowercase letter
# 
# 
# 
#

# @lc code=start
from collections import Counter

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        # results = []
        # i = 0
        # while i < len(A[0]):
        #     if all(A[0][i] in item for item in A):
        #         results.append(A[0][i])
        #         A = [item.replace(A[0][i], "", 1) for item in A]
        #         i -= 1
        #     i += 1
        # return results

        res = Counter(A[0])
        for a in A:
            res &= Counter(a)
        return res.elements()

        
# @lc code=end

