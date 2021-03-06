#
# @lc app=leetcode id=526 lang=python3
#
# [526] Beautiful Arrangement
#
# https://leetcode.com/problems/beautiful-arrangement/description/
#
# algorithms
# Medium (57.74%)
# Likes:    694
# Dislikes: 151
# Total Accepted:    51.9K
# Total Submissions: 89.6K
# Testcase Example:  '2'
#
# Suppose you have N integers from 1 to N. We define a beautiful arrangement as
# an array that is constructed by these N numbers successfully if one of the
# following is true for the ith position (1 <= i <= N) in this array:
# 
# 
# The number at the ith position is divisible by i.
# i is divisible by the number at the ith position.
# 
# 
# 
# 
# Now given N, how many beautiful arrangements can you construct?
# 
# Example 1:
# 
# 
# Input: 2
# Output: 2
# Explanation: 
# 
# The first beautiful arrangement is [1, 2]:
# 
# Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).
# 
# Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).
# 
# The second beautiful arrangement is [2, 1]:
# 
# Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).
# 
# Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.
# 
# 
# 
# 
# Note:
# 
# 
# N is a positive integer and will not exceed 15.
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def countArrangement(self, N: int) -> int:
        def calculate(N, pos, visited):
            if pos > N: self.count += 1

            for i in range(1, N + 1):
                if not visited[i] and (pos % i == 0 or i % pos == 0):
                    visited[i] = True
                    calculate(N, pos + 1, visited)
                    visited[i] = False

        self.count = 0
        visited = [False] * (N + 1)
        calculate(N, 1, visited)
        return self.count


        # def count(i, X):
        #     if i == 1: return 1
        #     return sum(count(i-1, X-{x}) for x in X if x % i == 0 or i % x == 0)
        # return count(N, set(range(1, N+1)))
        
# @lc code=end

