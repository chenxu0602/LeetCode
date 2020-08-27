#
# @lc app=leetcode id=649 lang=python3
#
# [649] Dota2 Senate
#
# https://leetcode.com/problems/dota2-senate/description/
#
# algorithms
# Medium (37.84%)
# Likes:    211
# Dislikes: 163
# Total Accepted:    9.2K
# Total Submissions: 24.3K
# Testcase Example:  '"RD"'
#
# In the world of Dota2, there are two parties: the Radiant and the Dire.
# 
# The Dota2 senate consists of senators coming from two parties. Now the senate
# wants to make a decision about a change in the Dota2 game. The voting for
# this change is a round-based procedure. In each round, each senator can
# exercise one of the two rights:
# 
# 
# Ban one senator's right:
# A senator can make another senator lose all his rights in this and all the
# following rounds.
# Announce the victory:
# If this senator found the senators who still have rights to vote are all from
# the same party, he can announce the victory and make the decision about the
# change in the game.
# 
# 
# 
# 
# Given a string representing each senator's party belonging. The character 'R'
# and 'D' represent the Radiant party and the Dire party respectively. Then if
# there are n senators, the size of the given string will be n.
# 
# The round-based procedure starts from the first senator to the last senator
# in the given order. This procedure will last until the end of voting. All the
# senators who have lost their rights will be skipped during the procedure.
# 
# Suppose every senator is smart enough and will play the best strategy for his
# own party, you need to predict which party will finally announce the victory
# and make the change in the Dota2 game. The output should be Radiant or Dire.
# 
# Example 1:
# 
# 
# Input: "RD"
# Output: "Radiant"
# Explanation: The first senator comes from Radiant and he can just ban the
# next senator's right in the round 1. 
# And the second senator can't exercise any rights any more since his right has
# been banned. 
# And in the round 2, the first senator can just announce the victory since he
# is the only guy in the senate who can vote.
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: "RDD"
# Output: "Dire"
# Explanation: 
# The first senator comes from Radiant and he can just ban the next senator's
# right in the round 1. 
# And the second senator can't exercise any rights anymore since his right has
# been banned. 
# And the third senator comes from Dire and he can ban the first senator's
# right in the round 1. 
# And in the round 2, the third senator can just announce the victory since he
# is the only guy in the senate who can vote.
# 
# 
# 
# 
# Note:
# 
# 
# The length of the given string will in the range [1, 10,000].
# 
# 
# 
# 
#
from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # Time  complexity: O(N)
        # Space complexity: O(N)
        queue = deque()
        people, bans = [0, 0], [0, 0]

        for person in senate:
            x = person == 'R'
            people[x] += 1
            queue.append(x)

        while all(people):
            x = queue.popleft()
            if bans[x]:
                bans[x] -= 1
                people[x] -= 1
            else:
                bans[x ^ 1] += 1
                queue.append(x)

        return 'Radiant' if people[1] else 'Dire'


        # l = len(senate)
        # R = [i for i in range(l) if senate[i] == 'R']
        # D = [i for i in range(l) if senate[i] == 'D']

        # while len(D) and len(R):
        #     if D[0] > R[0]:
        #         R.append(R[0] + l)
        #     else:
        #         D.append(D[0] + l)

        #     del D[0]
        #     del R[0]

        # return 'Dire' if len(D) != 0 else 'Radiant'


        # s = list(senate)
        # i = j = 0
        # while True:
        #     while i < len(s) and s[i] != 'R':
        #         i += 1
        #     if i == len(s):
        #         return 'Dire'

        #     while j < len(s) and s[j] != 'D':
        #         j += 1
        #     if j == len(s):
        #         return 'Radiant'

        #     if i < j:
        #         s[j] = ['X']
        #         s.append('R')
        #     else:
        #         s[i] = 'X'
        #         s.append('D')

        #     i += 1
        #     j += 1
            
            

        

