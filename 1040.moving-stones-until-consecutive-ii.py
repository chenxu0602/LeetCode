#
# @lc app=leetcode id=1040 lang=python3
#
# [1040] Moving Stones Until Consecutive II
#
# https://leetcode.com/problems/moving-stones-until-consecutive-ii/description/
#
# algorithms
# Medium (48.94%)
# Likes:    83
# Dislikes: 115
# Total Accepted:    2.7K
# Total Submissions: 5.4K
# Testcase Example:  '[7,4,9]'
#
# On an infinite number line, the position of the i-th stone is given by
# stones[i].  Call a stone an endpoint stone if it has the smallest or largest
# position.
# 
# Each turn, you pick up an endpoint stone and move it to an unoccupied
# position so that it is no longer an endpoint stone.
# 
# In particular, if the stones are at say, stones = [1,2,5], you cannot move
# the endpoint stone at position 5, since moving it to any position (such as 0,
# or 3) will still keep that stone as an endpoint stone.
# 
# The game ends when you cannot make any more moves, ie. the stones are in
# consecutive positions.
# 
# When the game ends, what is the minimum and maximum number of moves that you
# could have made?  Return the answer as an length 2 array: answer =
# [minimum_moves, maximum_moves]
# 
# 
# 
# Example 1:
# 
# 
# Input: [7,4,9]
# Output: [1,2]
# Explanation: 
# We can move 4 -> 8 for one move to finish the game.
# Or, we can move 9 -> 5, 4 -> 6 for two moves to finish the game.
# 
# 
# 
# Example 2:
# 
# 
# Input: [6,5,4,3,10]
# Output: [2,3]
# We can move 3 -> 8 then 10 -> 7 to finish the game.
# Or, we can move 3 -> 7, 4 -> 8, 5 -> 9 to finish the game.
# Notice we cannot move 10 -> 2 to finish the game, because that would be an
# illegal move.
# 
# 
# 
# Example 3:
# 
# 
# Input: [100,101,104,102,103]
# Output: [0,0]
# 
# 
# 
# 
# 
# Note:
# 
# 
# 3 <= stones.length <= 10^4
# 1 <= stones[i] <= 10^9
# stones[i] have distinct values.
# 
# 
# 
# 
# 
# 
# 
#
class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        stones.sort()
        i, n, low = 0, len(stones), len(stones)
        high = max(stones[-1] - n + 2 - stones[1], stones[-2] - stones[0] - n + 2)
        
        for j in range(n):
            while stones[j] - stones[i] >= n:
                i += 1

            if j - i + 1 == n - 1 and stones[j] - stones[i] == n - 2:
                low = min(low, 2)
            else:
                low = min(low, n - (j - i + 1))
        return [low, high]
            
        

