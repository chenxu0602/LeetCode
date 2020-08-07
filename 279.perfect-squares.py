#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#
# https://leetcode.com/problems/perfect-squares/description/
#
# algorithms
# Medium (44.43%)
# Likes:    2160
# Dislikes: 168
# Total Accepted:    246.5K
# Total Submissions: 552.9K
# Testcase Example:  '12'
#
# Given a positive integer n, find the least number of perfect square numbers
# (for example, 1, 4, 9, 16, ...) which sum to n.
# 
# Example 1:
# 
# 
# Input: n = 12
# Output: 3 
# Explanation: 12 = 4 + 4 + 4.
# 
# Example 2:
# 
# 
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.
#

# @lc code=start
import math

class Solution:
    def numSquares(self, n: int) -> int:
        # Time  complexity: O(n x sqrt(n))
        # Space complexity: O(n)
        # square_nums = [i**2 for i in range(0, int(math.sqrt(n)) + 1)]

        # dp = [float("inf")] * (n + 1)
        # dp[0] = 0

        # for i in range(n + 1):
        #     for square in square_nums:
        #         if i < square:
        #             break
        #         dp[i] = min(dp[i], dp[i-square] + 1)

        # return dp[-1]


        # dp = [0] * (n + 1)
        # dp[1] = 1

        # for i in range(2, n + 1):
        #     dp[i] = 1 + min(dp[i-j*j] for j in range(1, int(math.sqrt(i)) + 1))

        # return dp[-1]



        # Greedy Enumeration
        # Time  complexity: O((power(n, 1/(h+1)) - 1) / (sqrt(n) - 1)) = O(h/2), here h is the maximal number of recursion that could happen. 
        # Space complexity: O(sqrt(n))
        # def is_divided_by(n, count):
        #     if count == 1:
        #         return n in square_nums

        #     for k in square_nums:
        #         if is_divided_by(n - k, count - 1):
        #             return True
        #     return False

        # square_nums = set([i**2 for i in range(1, int(n**0.5) + 1)])

        # for count in range(1, n + 1):
        #     if is_divided_by(n, count):
        #         return count


        # Greedy + BFS (Breadth-First Search)
        # Time  complexity: O((power(n, 1/(h+1)) - 1) / (sqrt(n) - 1)) = O(h/2), here h is the maximal number of recursion that could happen. 
        # Space complexity: O(power(n, 1/h)), which is also the maximal number of nodes that can appear at the level h
        square_nums = [i**2 for i in range(1, int(n**0.5) + 1)]

        level, queue = 0, {n}
        while queue:
            level += 1
            next_queue = set()
            for remainder in queue:
                for square_num in square_nums:
                    if remainder == square_num:
                        return level
                    elif remainder < square_num:
                        break
                    else:
                        next_queue.add(remainder - square_num)
            queue = next_queue

        return level


        # In 1770, Joseph Louis Lagrange proved a theorem, called Lagrange's four-square theorem, also known as Bachet's conjecture, which states that every natural number can be represented as the sum of four integer squares.
        # Later, in 1797, Adrien-Marie Legendre completed the four-square theorem with his three-square theorem, by proving a particular condition that a positive integer can be expressed as the sum of three squares.
        # n != 4^k x (8m + 7)
        # Time  complexity: O(sqrt(n))
        # Space complexity: O(1)
        # def isSquare(n: int) -> bool:
        #     sq = int(math.sqrt(n))
        #     return sq*sq == n

        # # four-square and three-square theorems
        # while n & 3 == 0:
        #     n >>= 2 # reducing the 4^k factor from number
        # if n & 7 == 7: # mod 8
        #     return 4

        # if isSquare(n):
        #     return 1

        # for i in range(1, int(n**0.5) + 1):
        #     if isSquare(n - i*i):
        #         return 2

        # return 3


        
# @lc code=end

