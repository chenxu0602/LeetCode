#
# @lc app=leetcode id=85 lang=python3
#
# [85] Maximal Rectangle
#
# https://leetcode.com/problems/maximal-rectangle/description/
#
# algorithms
# Hard (35.87%)
# Likes:    2129
# Dislikes: 57
# Total Accepted:    153.4K
# Total Submissions: 427.2K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle
# containing only 1's and return its area.
# 
# Example:
# 
# 
# Input:
# [
# ⁠ ["1","0","1","0","0"],
# ⁠ ["1","0","1","1","1"],
# ⁠ ["1","1","1","1","1"],
# ⁠ ["1","0","0","1","0"]
# ]
# Output: 6
# 
# 
#

# @lc code=start
class Solution:
    def leetcode84(self, heights):
        stack = [-1]
        heights.append(0)
        ans = 0

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, w * h)
            stack.append(i)

        heights.pop()
        return ans

    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        # Time complexity:   O(N^2 x M)
        # Space complexity:  O(N x M)

        # maxarea = 0

        # dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if matrix[i][j] == '0': continue

        #         width = dp[i][j] = dp[i][j-1] + 1 if j else 1

        #         for k in range(i, -1, -1):
        #             width = min(width, dp[k][j])
        #             maxarea = max(maxarea, width * (i - k + 1))

        # return maxarea


        # Time complexity:   O(N x M)
        # Space complexity:  O(M)

        if not matrix: return 0

        maxarea = 0
        dp = [0] * len(matrix[0])

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dp[j] = dp[j] + 1 if matrix[i][j] == '1' else 0
            
            maxarea = max(maxarea, self.leetcode84(dp))
        return maxarea

        
# @lc code=end

