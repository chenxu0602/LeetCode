#
# @lc app=leetcode id=1349 lang=python3
#
# [1349] Maximum Students Taking Exam
#
# https://leetcode.com/problems/maximum-students-taking-exam/description/
#
# algorithms
# Hard (43.08%)
# Likes:    343
# Dislikes: 9
# Total Accepted:    6.5K
# Total Submissions: 15.1K
# Testcase Example:  '[["#",".","#","#",".","#"],[".","#","#","#","#","."],["#",".","#","#",".","#"]]'
#
# Given a m * n matrix seats  that represent seats distributions in a
# classroom. If a seat is broken, it is denoted by '#' character otherwise it
# is denoted by a '.' character.
# 
# Students can see the answers of those sitting next to the left, right, upper
# left and upper right, but he cannot see the answers of the student sitting
# directly in front or behind him. Return the maximum number of students that
# can take the exam together without any cheating being possible..
# 
# Students must be placed in seats in good condition.
# 
# 
# Example 1:
# 
# 
# Input: seats = [["#",".","#","#",".","#"],
# [".","#","#","#","#","."],
# ["#",".","#","#",".","#"]]
# Output: 4
# Explanation: Teacher can place 4 students in available seats so they don't
# cheat on the exam. 
# 
# 
# Example 2:
# 
# 
# Input: seats = [[".","#"],
# ["#","#"],
# ["#","."],
# ["#","#"],
# [".","#"]]
# Output: 3
# Explanation: Place all students in available seats. 
# 
# 
# 
# Example 3:
# 
# 
# Input: seats = [["#",".",".",".","#"],
# [".","#",".","#","."],
# [".",".","#",".","."],
# [".","#",".","#","."],
# ["#",".",".",".","#"]]
# Output: 10
# Explanation: Place students in available seats in column 1, 3 and 5.
# 
# 
# 
# Constraints:
# 
# 
# seats contains only characters '.' and'#'.
# m == seats.length
# n == seats[i].length
# 1 <= m <= 8
# 1 <= n <= 8
# 
# 
#

# @lc code=start
from functools import lru_cache

class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        m, n = map(len, (seats, seats[0]))
        dp = [{} for _ in range(n + 1)]

        def count_bits(c):
            res = 0
            while c:
                res += c & 1
                c >>= 1
            return res

        for j in range(n):
            comb = [0]
            for i in range(m):
                if seats[i][j] == '.':
                    comb += [c | 1 << i for c in comb]

            for c in comb:
                nbits = count_bits(c)
                for prev in range(1 << m):
                    if prev & c == 0 and (prev >> 1) & c == 0 and (prev << 1) & c == 0:
                        dp[j + 1][c] = max(dp[j + 1].get(c, 0), nbits + dp[j].get(prev, 0))

        return max(dp[-1].values())

        

        
        
# @lc code=end

