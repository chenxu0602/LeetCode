#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#
# https://leetcode.com/problems/happy-number/description/
#
# algorithms
# Easy (46.12%)
# Likes:    1088
# Dislikes: 282
# Total Accepted:    278.8K
# Total Submissions: 592.9K
# Testcase Example:  '19'
#
# Write an algorithm to determine if a number is "happy".
# 
# A happy number is a number defined by the following process: Starting with
# any positive integer, replace the number by the sum of the squares of its
# digits, and repeat the process until the number equals 1 (where it will
# stay), or it loops endlessly in a cycle which does not include 1. Those
# numbers for which this process ends in 1 are happy numbers.
# 
# Example: 
# 
# 
# Input: 19
# Output: true
# Explanation: 
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
# 
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:

        # Detect Cycles with a HashSet
        # Time  complexity: O(logn)
        # Space complexity: O(logn)
        # def get_next(n):
        #     total_sum = 0
        #     while n > 0:
        #         n, digit = divmod(n, 10)
        #         total_sum += digit ** 2
        #     return total_sum

        # seen = set()
        # while n != 1 and n not in seen:
        #     seen.add(n)
        #     n = get_next(n)

        # return n == 1


        # Floyd's Cycle-Finding Algorithm
        # Instead of keeping track of just one value in the chain, we keep track of 2, called the slow runner and the fast runner. 
        # Time  complexity: O(logn)
        # Space complexity: O(1)
        def get_next(n):
            total_num = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_num += digit ** 2
            return total_num

        slow_runner, fast_runner = n, get_next(n)
        while fast_runner != 1 and slow_runner != fast_runner:
            slow_runner, fast_runner = get_next(slow_runner), get_next(get_next(fast_runner))
        return fast_runner == 1


        
# @lc code=end

