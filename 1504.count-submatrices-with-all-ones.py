#
# @lc app=leetcode id=1504 lang=python3
#
# [1504] Count Submatrices With All Ones
#
# https://leetcode.com/problems/count-submatrices-with-all-ones/description/
#
# algorithms
# Medium (61.52%)
# Likes:    623
# Dislikes: 38
# Total Accepted:    15.3K
# Total Submissions: 24.9K
# Testcase Example:  '[[1,0,1],[1,1,0],[1,1,0]]'
#
# Given a rows * columns matrix mat of ones and zeros, return how many
# submatrices have all ones.
# 
# 
# Example 1:
# 
# 
# Input: mat = [[1,0,1],
# [1,1,0],
# [1,1,0]]
# Output: 13
# Explanation:
# There are 6 rectangles of side 1x1.
# There are 2 rectangles of side 1x2.
# There are 3 rectangles of side 2x1.
# There is 1 rectangle of side 2x2. 
# There is 1 rectangle of side 3x1.
# Total number of rectangles = 6 + 2 + 3 + 1 + 1 = 13.
# 
# 
# Example 2:
# 
# 
# Input: mat = [[0,1,1,0],
# [0,1,1,1],
# [1,1,1,0]]
# Output: 24
# Explanation:
# There are 8 rectangles of side 1x1.
# There are 5 rectangles of side 1x2.
# There are 2 rectangles of side 1x3. 
# There are 4 rectangles of side 2x1.
# There are 2 rectangles of side 2x2. 
# There are 2 rectangles of side 3x1. 
# There is 1 rectangle of side 3x2. 
# Total number of rectangles = 8 + 5 + 2 + 4 + 2 + 2 + 1 = 24.
# 
# 
# Example 3:
# 
# 
# Input: mat = [[1,1,1,1,1,1]]
# Output: 21
# 
# 
# Example 4:
# 
# 
# Input: mat = [[1,0,1],[0,1,0],[1,0,1]]
# Output: 5
# 
# 
# 
# Constraints:
# 
# 
# 1 <= rows <= 150
# 1 <= columns <= 150
# 0 <= mat[i][j] <= 1
# 
#

# @lc code=start
class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        # O(MN)

        # Define a stack to store indices of non-decreasing height, and a variable cnt for the number of all-1 submatrices at given position (i, j). Take the height of row i as an example, say h = mat[i]. At column j, if h[j-1] <= h[j], it is apparent that cnt[j] = cnt[j-1] + h[j], since every case that contributes to cnt[j-1] could be added a new column of 1's from the jth column to contribute to cnt[j].
        # The tricky part is when h[j-1] > h[j]. In this case, we need to "hypothetically" lower h[j-1] to h[j] to get an updated cnt*[j-1] before adding h[j] to get cnt[j]. Suppose that the histogram is like below to reflect 3,3,3,2. To compute cnt[3], we have to adjust cnt[2] to a hypothetical height of 2 by removing top row before adding the new column to get cnt[3]. The specific operation is done using a mono-stack which stores indices of non-decreasing height. Whenever a new height comes in, pop out the heights in the stack that are higher than the new height while removing the quota contributed by the extra height (between poped height and new height).

        m, n = map(len, (mat, mat[0]))

        for i in range(m):
            for j in range(n):
                if mat[i][j] > 0 and i > 0:
                    mat[i][j] += mat[i - 1][j]

        ans = 0
        for i in range(m):
            stack = []
            cnt = 0
            for j in range(n):
                while stack and mat[i][stack[-1]] > mat[i][j]:
                    jj = stack.pop()
                    kk = stack[-1] if stack else -1
                    cnt -= (mat[i][jj] - mat[i][j]) * (jj - kk)

                cnt += mat[i][j]
                ans += cnt
                stack.append(j)

        return ans
        
# @lc code=end

