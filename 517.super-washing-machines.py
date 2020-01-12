#
# @lc app=leetcode id=517 lang=python3
#
# [517] Super Washing Machines
#
# https://leetcode.com/problems/super-washing-machines/description/
#
# algorithms
# Hard (37.06%)
# Likes:    203
# Dislikes: 113
# Total Accepted:    12.9K
# Total Submissions: 34.8K
# Testcase Example:  '[1,0,5]'
#
# You have n super washing machines on a line. Initially, each washing machine
# has some dresses or is empty. 
# 
# 
# For each move, you could choose any m (1 ≤ m ≤ n) washing machines, and pass
# one dress of each washing machine to one of its adjacent washing machines  at
# the same time .  
# 
# Given an integer array representing the number of dresses in each washing
# machine from left to right on the line, you should find the minimum number of
# moves to make all the washing machines have the same number of dresses. If it
# is not possible to do it, return -1.
# 
# Example1
# 
# Input: [1,0,5]
# 
# Output: 3
# 
# Explanation: 
# 1st move:    1     0     1     1     4
# 2nd move:    1     2     1     3    
# 3rd move:    2     1     2     2     2   
# 
# 
# Example2
# 
# Input: [0,3,0]
# 
# Output: 2
# 
# Explanation: 
# 1st move:    0     1     2     0    
# 2nd move:    1     2 --> 0    =>    1     1     1     
# 
# 
# Example3
# 
# Input: [0,2,0]
# 
# Output: -1
# 
# Explanation: 
# It's impossible to make all the three washing machines have the same number
# of dresses. 
# 
# 
# 
# 
# Note:
# 
# The range of n is [1, 10000].
# The range of dresses number in a super washing machine is [0, 1e5].
# 
# 
#
class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        """
        n = len(machines)
        dress_total = sum(machines)
        if dress_total % n != 0:
            return -1

        dress_per_machine = dress_total // n

        for i in range(n):
            machines[i] -= dress_per_machine

        curr_sum = max_sum = res = 0
        for m in machines:
            curr_sum += m
            max_sum = max(max_sum, abs(curr_sum))
            res = max(res, max_sum, m)

        return res
        """

        total, n = sum(machines), len(machines)
        if total % n: return -1
        target, res, toRight = total // n, 0, 0
        for m in machines:
            toRight = m + toRight - target
            res = max(res, abs(toRight), m - target)
        return res
        

