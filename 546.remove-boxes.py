#
# @lc app=leetcode id=546 lang=python3
#
# [546] Remove Boxes
#
# https://leetcode.com/problems/remove-boxes/description/
#
# algorithms
# Hard (38.69%)
# Likes:    392
# Dislikes: 37
# Total Accepted:    9.9K
# Total Submissions: 25.6K
# Testcase Example:  '[1,3,2,2,2,3,4,3,1]'
#
# Given several boxes with different colors represented by different positive
# numbers. 
# You may experience several rounds to remove boxes until there is no box left.
# Each time you can choose some continuous boxes with the same color (composed
# of k boxes, k >= 1), remove them and get k*k points.
# Find the maximum points you can get.
# 
# 
# Example 1:
# Input: 
# 
# [1, 3, 2, 2, 2, 3, 4, 3, 1]
# 
# Output:
# 
# 23
# 
# Explanation: 
# 
# [1, 3, 2, 2, 2, 3, 4, 3, 1] 
# ----> [1, 3, 3, 4, 3, 1] (3*3=9 points) 
# ----> [1, 3, 3, 3, 1] (1*1=1 points) 
# ----> [1, 1] (3*3=9 points) 
# ----> [] (2*2=4 points)
# 
# 
# 
# Note:
# The number of boxes n would not exceed 100.
# 
# 
#
class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        n = len(boxes)
        memo = [[[0] * n for _ in range(n)] for _ in range(n)]

        def dp(i, j, k):
            if i > j:
                return 0
            if not memo[i][j][k]:
                m = i
                while m + 1 <= j and boxes[m+1] == boxes[i]:
                    m += 1
                i, k = m, k + m - i
                ans = dp(i+1, j, 0) + (k+1)**2

                for m in range(i+1, j+1):
                    if boxes[i] == boxes[m]:
                        ans = max(ans, dp(i+1, m-1, 0) + dp(m, j, k+1))
                memo[i][j][k] = ans
            return memo[i][j][k]

        return dp(0, n-1, 0)
        

