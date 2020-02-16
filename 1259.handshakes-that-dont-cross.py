#
# @lc app=leetcode id=1259 lang=python3
#
# [1259] Handshakes That Don't Cross
#
# https://leetcode.com/problems/handshakes-that-dont-cross/description/
#
# algorithms
# Hard (52.56%)
# Likes:    43
# Dislikes: 2
# Total Accepted:    1.9K
# Total Submissions: 3.7K
# Testcase Example:  '2'
#
# You are given an even number of people num_people that stand around a circle
# and each person shakes hands with someone else, so that there are num_people
# / 2 handshakes total.
# 
# Return the number of ways these handshakes could occur such that none of the
# handshakes cross.
# 
# Since this number could be very big, return the answer mod 10^9 + 7
# 
# 
# Example 1:
# 
# 
# Input: num_people = 2
# Output: 1
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: num_people = 4
# Output: 2
# Explanation: There are two ways to do it, the first way is [(1,2),(3,4)] and
# the second one is [(2,3),(4,1)].
# 
# 
# Example 3:
# 
# 
# 
# 
# Input: num_people = 6
# Output: 5
# 
# 
# Example 4:
# 
# 
# Input: num_people = 8
# Output: 14
# 
# 
# 
# Constraints:
# 
# 
# 2 <= num_people <= 1000
# num_people % 2 == 0
# 
# 
#

# @lc code=start
# from functools import lru_cache

# class Solution:
#     @lru_cache(None)
#     def numberOfWays(self, num_people: int) -> int:
#         return (sum(self.numberOfWays(i) * self.numberOfWays(num_people - 2 - i) for i in range(0, num_people, 2)) % (10**9 + 7)) if num_people else 1
        
class Solution:
    def numberOfWays(self, num_people: int) -> int:
        d = {0: 1, 2: 1, 4: 2}
        for i in range(6, num_people + 1, 2):
            s = 0
            for j in range(i // 2):
                left = j * 2
                right = i - left - 2
                s += d[left] * d[right]
            d[i] = s
        return d[num_people] % (10**9 + 7)

        
# @lc code=end

