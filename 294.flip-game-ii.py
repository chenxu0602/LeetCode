#
# @lc app=leetcode id=294 lang=python3
#
# [294] Flip Game II
#
# https://leetcode.com/problems/flip-game-ii/description/
#
# algorithms
# Medium (48.34%)
# Likes:    281
# Dislikes: 23
# Total Accepted:    43.9K
# Total Submissions: 90.7K
# Testcase Example:  '"++++"'
#
# You are playing the following Flip Game with your friend: Given a string that
# contains only these two characters: + and -, you and your friend take turns
# to flip two consecutive "++" into "--". The game ends when a person can no
# longer make a move and therefore the other person will be the winner.
# 
# Write a function to determine if the starting player can guarantee a win.
# 
# Example:
# 
# 
# Input: s = "++++"
# Output: true 
# Explanation: The starting player can guarantee a win by flipping the middle
# "++" to become "+--+".
# 
# 
# Follow up:
# Derive your algorithm's runtime complexity.
#
class Solution:
    _memo = {}
    def canWin(self, s: str) -> bool:

        """
        return any(s[i:i+2] == '++' and not self.canWin(s[:i] + '--' + s[i+2:]) for i in range(len(s)))
        """

        memo = self._memo
        if s not in memo:
            return any(s[i:i+2] == '++' and not self.canWin(s[:i] + '--' + s[i+2:]) for i in range(len(s)))
        return memo[s]

        

