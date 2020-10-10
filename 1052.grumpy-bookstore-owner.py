#
# @lc app=leetcode id=1052 lang=python3
#
# [1052] Grumpy Bookstore Owner
#
# https://leetcode.com/problems/grumpy-bookstore-owner/description/
#
# algorithms
# Medium (52.75%)
# Likes:    140
# Dislikes: 14
# Total Accepted:    9.8K
# Total Submissions: 18.5K
# Testcase Example:  '[1,0,1,2,1,1,7,5]\n[0,1,0,1,0,1,0,1]\n3'
#
# Today, the bookstore owner has a store open for customers.length minutes.
# Every minute, some number of customers (customers[i]) enter the store, and
# all those customers leave after the end of that minute.
# 
# On some minutes, the bookstore owner is grumpy.  If the bookstore owner is
# grumpy on the i-th minute, grumpy[i] = 1, otherwise grumpy[i] = 0.  When the
# bookstore owner is grumpy, the customers of that minute are not satisfied,
# otherwise they are satisfied.
# 
# The bookstore owner knows a secret technique to keep themselves not grumpy
# for X minutes straight, but can only use it once.
# 
# Return the maximum number of customers that can be satisfied throughout the
# day.
# 
# 
# 
# Example 1:
# 
# 
# Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
# Output: 16
# Explanation: The bookstore owner keeps themselves not grumpy for the last 3
# minutes. 
# The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5
# = 16.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= X <= customers.length == grumpy.length <= 20000
# 0 <= customers[i] <= 1000
# 0 <= grumpy[i] <= 1
# 
#
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        # customers1 = [customers[i] if grumpy[i] == 0 else 0 for i in range(len(customers))]
        
        # i = 0
        # diff = sum(customers[i:i+X]) - sum(customers1[i:i+X])
        # max_diff = diff
        # non_grump_ind = 0

        # for i in range(1, len(customers) - X + 1):
        #     diff += customers[i+X-1] - customers1[i+X-1] - customers[i-1] + customers1[i-1]
        #     if diff > max_diff:
        #         max_diff = diff
        #         non_grump_ind = i
        # return sum(customers1[:non_grump_ind]) + sum(customers[non_grump_ind:non_grump_ind+X]) + sum(customers1[non_grump_ind+X:])


        m = s = tmp = 0

        for i in range(len(customers)):
            if not grumpy[i]:
                s += customers[i]
                customers[i] = 0
            else:
                tmp += customers[i]

            if i >= X:
                tmp -= customers[i - X]

            m = max(m, tmp)

        return s + m

        

