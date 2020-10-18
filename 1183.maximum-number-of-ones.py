#
# @lc app=leetcode id=1183 lang=python3
#
# [1183] Maximum Number of Ones
#
# https://leetcode.com/problems/maximum-number-of-ones/description/
#
# algorithms
# Hard (51.58%)
# Likes:    44
# Dislikes: 8
# Total Accepted:    1K
# Total Submissions: 2K
# Testcase Example:  '3\n3\n2\n1'
#
# Consider a matrix M with dimensions width * height, such that every cell has
# value 0 or 1, and any square sub-matrix of M of size sideLength * sideLength
# has at most maxOnes ones.
# 
# Return the maximum possible number of ones that the matrix M can have.
# 
# 
# Example 1:
# 
# 
# Input: width = 3, height = 3, sideLength = 2, maxOnes = 1
# Output: 4
# Explanation:
# In a 3*3 matrix, no 2*2 sub-matrix can have more than 1 one.
# The best solution that has 4 ones is:
# [1,0,1]
# [0,0,0]
# [1,0,1]
# 
# 
# Example 2:
# 
# 
# Input: width = 3, height = 3, sideLength = 2, maxOnes = 2
# Output: 6
# Explanation:
# [1,0,1]
# [1,0,1]
# [1,0,1]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= width, height <= 100
# 1 <= sideLength <= width, height
# 0 <= maxOnes <= sideLength * sideLength
# 
# 
#

# @lc code=start
class Solution:
    def maximumNumberOfOnes(self, width: int, height: int, sideLength: int, maxOnes: int) -> int:
        res = []
        for i in range(sideLength):
            for j in range(sideLength):
                res += [((width - i - 1) // sideLength + 1) * ((height - j - 1) // sideLength + 1)]

        res.sort(reverse=True)
        return sum(res[:maxOnes])
        
# @lc code=end

