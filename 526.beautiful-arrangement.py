#
# @lc app=leetcode id=526 lang=python3
#
# [526] Beautiful Arrangement
#
# https://leetcode.com/problems/beautiful-arrangement/description/
#
# algorithms
# Medium (54.92%)
# Likes:    456
# Dislikes: 115
# Total Accepted:    38.9K
# Total Submissions: 70.7K
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
class Solution:
    def countArrangement(self, N: int) -> int:
        self.count = 0
        visited = [False] * (N+1)
        self.calculate(N, 1, visited)
        return self.count

    def calculate(self, N, pos, visited):
        if pos > N:
            self.count += 1

        for i in range(1, N+1):
            if not visited[i] and (pos % i == 0 or i % pos == 0):
                visited[i] = True
                self.calculate(N, pos + 1, visited)
                visited[i] = False
        

