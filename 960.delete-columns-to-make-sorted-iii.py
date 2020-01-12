#
# @lc app=leetcode id=960 lang=python3
#
# [960] Delete Columns to Make Sorted III
#
# https://leetcode.com/problems/delete-columns-to-make-sorted-iii/description/
#
# algorithms
# Hard (53.38%)
# Likes:    171
# Dislikes: 5
# Total Accepted:    4.5K
# Total Submissions: 8.5K
# Testcase Example:  '["babca","bbazb"]'
#
# We are given an array A of N lowercase letter strings, all of the same
# length.
# 
# Now, we may choose any set of deletion indices, and for each string, we
# delete all the characters in those indices.
# 
# For example, if we have an array A = ["babca","bbazb"] and deletion indices
# {0, 1, 4}, then the final array after deletions is ["bc","az"].
# 
# Suppose we chose a set of deletion indices D such that after deletions, the
# final array has every element (row) in lexicographic order.
# 
# For clarity, A[0] is in lexicographic order (ie. A[0][0] <= A[0][1] <= ... <=
# A[0][A[0].length - 1]), A[1] is in lexicographic order (ie. A[1][0] <=
# A[1][1] <= ... <= A[1][A[1].length - 1]), and so on.
# 
# Return the minimum possible value of D.length.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: ["babca","bbazb"]
# Output: 3
# Explanation: After deleting columns 0, 1, and 4, the final array is A =
# ["bc", "az"].
# Both these rows are individually in lexicographic order (ie. A[0][0] <=
# A[0][1] and A[1][0] <= A[1][1]).
# Note that A[0] > A[1] - the array A isn't necessarily in lexicographic
# order.
# 
# 
# 
# Example 2:
# 
# 
# Input: ["edcba"]
# Output: 4
# Explanation: If we delete less than 4 columns, the only row won't be
# lexicographically sorted.
# 
# 
# 
# Example 3:
# 
# 
# Input: ["ghi","def","abc"]
# Output: 0
# Explanation: All rows are already lexicographically sorted.
# 
# 
# 
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 100
# 1 <= A[i].length <= 100
# 
#
class Solution:
    def minDeletionSize(self, A: List[str]) -> int:

        """
        Let dp[k] be the number of columns that are kept in answering the question for input [row[k:] for row in A]. The above gives a simple recursion for dp[k].
        """


        W = len(A[0])
        dp = [1] * W
        for i in range(W-2, -1, -1):
            for j in range(i+1, W):
                if all(row[i] <= row[j] for row in A):
                    dp[i] = max(dp[i], 1 + dp[j])
        return W - max(dp)

        

