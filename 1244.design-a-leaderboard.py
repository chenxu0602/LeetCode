#
# @lc app=leetcode id=1244 lang=python3
#
# [1244] Design A Leaderboard
#
# https://leetcode.com/problems/design-a-leaderboard/description/
#
# algorithms
# Medium (55.33%)
# Likes:    54
# Dislikes: 39
# Total Accepted:    3.4K
# Total Submissions: 6.2K
# Testcase Example:  '["Leaderboard","addScore","addScore","addScore","addScore","addScore","top","reset","reset","addScore","top"]\n' + '[[],[1,73],[2,56],[3,39],[4,51],[5,4],[1],[1],[2],[2,51],[3]]'
#
# Design a Leaderboard class, which has 3 functions:
# 
# 
# addScore(playerId, score): Update the leaderboard by adding score to the
# given player's score. If there is no player with such id in the leaderboard,
# add him to the leaderboard with the given score.
# top(K): Return the score sum of the top K players.
# reset(playerId): Reset the score of the player with the given id to 0. It is
# guaranteed that the player was added to the leaderboard before calling this
# function.
# 
# 
# Initially, the leaderboard is empty.
# 
# 
# Example 1:
# 
# 
# Input: 
# 
# ["Leaderboard","addScore","addScore","addScore","addScore","addScore","top","reset","reset","addScore","top"]
# [[],[1,73],[2,56],[3,39],[4,51],[5,4],[1],[1],[2],[2,51],[3]]
# Output: 
# [null,null,null,null,null,null,73,null,null,null,141]
# 
# Explanation: 
# Leaderboard leaderboard = new Leaderboard ();
# leaderboard.addScore(1,73);   // leaderboard = [[1,73]];
# leaderboard.addScore(2,56);   // leaderboard = [[1,73],[2,56]];
# leaderboard.addScore(3,39);   // leaderboard = [[1,73],[2,56],[3,39]];
# leaderboard.addScore(4,51);   // leaderboard = [[1,73],[2,56],[3,39],[4,51]];
# leaderboard.addScore(5,4);    // leaderboard =
# [[1,73],[2,56],[3,39],[4,51],[5,4]];
# leaderboard.top(1);           // returns 73;
# leaderboard.reset(1);         // leaderboard = [[2,56],[3,39],[4,51],[5,4]];
# leaderboard.reset(2);         // leaderboard = [[3,39],[4,51],[5,4]];
# leaderboard.addScore(2,51);   // leaderboard = [[2,51],[3,39],[4,51],[5,4]];
# leaderboard.top(3);           // returns 141 = 51 + 51 + 39;
# 
# 
# 
# Constraints:
# 
# 
# 1 <= playerId, K <= 10000
# It's guaranteed that K is less than or equal to the current number of
# players.
# 1 <= score <= 100
# There will be at most 1000 function calls.
# 
# 
#

# @lc code=start
from collections import defaultdict

class Leaderboard:

    def __init__(self):
        self.scores = defaultdict(int)
        

    def addScore(self, playerId: int, score: int) -> None:
        self.scores[playerId] += score
        
    def top(self, K: int) -> int:
        return sum(sorted(self.scores.values(), reverse=True)[:K])
        

    def reset(self, playerId: int) -> None:
        self.scores[playerId] = 0
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
# @lc code=end

