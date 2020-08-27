#
# @lc app=leetcode id=544 lang=python3
#
# [544] Output Contest Matches
#
# https://leetcode.com/problems/output-contest-matches/description/
#
# algorithms
# Medium (75.11%)
# Likes:    273
# Dislikes: 93
# Total Accepted:    20.9K
# Total Submissions: 27.8K
# Testcase Example:  '4'
#
# 
# During the NBA playoffs, we always arrange the rather strong team to play
# with the rather weak team, like make the rank 1 team play with the rank nth
# team, which is a good strategy to make the contest more interesting. Now,
# you're given n teams, you need to output their final contest matches in the
# form of a string.
# 
# 
# The n teams are given in the form of positive integers from 1 to n, which
# represents their initial rank. (Rank 1 is the strongest team and Rank n is
# the weakest team.) We'll use parentheses('(', ')') and commas(',') to
# represent the contest team pairing - parentheses('(' , ')') for pairing and
# commas(',') for partition. During the pairing process in each round, you
# always need to follow the strategy of making the rather strong one pair with
# the rather weak one. 
# 
# Example 1:
# 
# Input: 2
# Output: (1,2)
# Explanation: 
# Initially, we have the team 1 and the team 2, placed like: 1,2.
# Then we pair the team (1,2) together with '(', ')' and ',', which is the
# final answer.
# 
# 
# 
# Example 2:
# 
# Input: 4
# Output: ((1,4),(2,3))
# Explanation: 
# In the first round, we pair the team 1 and 4, the team 2 and 3 together, as
# we need to make the strong team and weak team together.
# And we got (1,4),(2,3).
# In the second round, the winners of (1,4) and (2,3) need to play again to
# generate the final winner, so you need to add the paratheses outside them.
# And we got the final answer ((1,4),(2,3)).
# 
# 
# 
# Example 3:
# 
# Input: 8
# Output: (((1,8),(4,5)),((2,7),(3,6)))
# Explanation: 
# First round: (1,8),(2,7),(3,6),(4,5)
# Second round: ((1,8),(4,5)),((2,7),(3,6))
# Third round: (((1,8),(4,5)),((2,7),(3,6)))
# Since the third round will generate the final winner, you need to output the
# answer (((1,8),(4,5)),((2,7),(3,6))).
# 
# 
# 
# Note:
# 
# The n is in range [2, 2^12].
# We ensure that the input n can be converted into the form 2^k, where k is a
# positive integer.
# 
# 
#

# @lc code=start
import math

class Solution:
    def findContestMatch(self, n: int) -> str:
        # Time  complexity: O(NlogN)
        # Space complexity: O(NlogN)
        # team = list(map(str, range(1, n + 1)))
        # while n > 1:
        #     for i in range(n // 2):
        #         team[i] = "({},{})".format(team[i], team.pop())
        #     n //= 2
        # return team[0]


        # Time  complexity: O(N)
        # Space complexity: O(N)
        team, ans = [], []
        def write(r):
            if r == 0:
                i = len(team)
                w = i & -i
                team.append(n // w + 1 - team[i - w] if w else 1)
                ans.append(str(team[-1]))
            else:
                ans.append('(')
                write(r - 1)
                ans.append(',')
                write(r - 1)
                ans.append(')')

        write(int(math.log(n, 2)))
        return "".join(ans)
        
# @lc code=end

