#
# @lc app=leetcode id=1035 lang=python3
#
# [1035] Uncrossed Lines
#
# https://leetcode.com/problems/uncrossed-lines/description/
#
# algorithms
# Medium (56.06%)
# Likes:    956
# Dislikes: 21
# Total Accepted:    47.9K
# Total Submissions: 85.4K
# Testcase Example:  '[1,4,2]\n[1,2,4]'
#
# We write the integers of A and B (in the order they are given) on two
# separate horizontal lines.
# 
# Now, we may draw connecting lines: a straight line connecting two numbers
# A[i] and B[j] such that:
# 
# 
# A[i] == B[j];
# The line we draw does not intersect any other connecting (non-horizontal)
# line.
# 
# 
# Note that a connecting lines cannot intersect even at the endpoints: each
# number can only belong to one connecting line.
# 
# Return the maximum number of connecting lines we can draw in this way.
# 
# 
# 
# Example 1:
# 
# 
# Input: A = [1,4,2], B = [1,2,4]
# Output: 2
# Explanation: We can draw 2 uncrossed lines as in the diagram.
# We cannot draw 3 uncrossed lines, because the line from A[1]=4 to B[2]=4 will
# intersect the line from A[2]=2 to B[1]=2.
# 
# 
# 
# Example 2:
# 
# 
# Input: A = [2,5,1,2,5], B = [10,5,2,1,5,2]
# Output: 3
# 
# 
# 
# Example 3:
# 
# 
# Input: A = [1,3,7,1,7,5], B = [1,9,2,5,1]
# Output: 2
# 
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 500
# 1 <= B.length <= 500
# 1 <= A[i], B[i] <= 2000
# 
# 
#

# @lc code=start
class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
        for i in range(len(A)):
            for j in range(len(B)):
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j], dp[i][j] + (A[i] == B[j]))
        return dp[-1][-1]
        
# @lc code=end

