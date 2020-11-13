#
# @lc app=leetcode id=1406 lang=python3
#
# [1406] Stone Game III
#
# https://leetcode.com/problems/stone-game-iii/description/
#
# algorithms
# Hard (56.62%)
# Likes:    400
# Dislikes: 4
# Total Accepted:    12.4K
# Total Submissions: 21.9K
# Testcase Example:  '[1,2,3,7]'
#
# Alice and Bob continue their games with piles of stones. There are several
# stones arranged in a row, and each stone has an associated value which is an
# integer given in the array stoneValue.
# 
# Alice and Bob take turns, with Alice starting first. On each player's turn,
# that player can take 1, 2 or 3 stones from the first remaining stones in the
# row.
# 
# The score of each player is the sum of values of the stones taken. The score
# of each player is 0 initially.
# 
# The objective of the game is to end with the highest score, and the winner is
# the player with the highest score and there could be a tie. The game
# continues until all the stones have been taken.
# 
# Assume Alice and Bob play optimally.
# 
# Return "Alice" if Alice will win, "Bob" if Bob will win or "Tie" if they end
# the game with the same score.
# 
# 
# Example 1:
# 
# 
# Input: values = [1,2,3,7]
# Output: "Bob"
# Explanation: Alice will always lose. Her best move will be to take three
# piles and the score become 6. Now the score of Bob is 7 and Bob wins.
# 
# 
# Example 2:
# 
# 
# Input: values = [1,2,3,-9]
# Output: "Alice"
# Explanation: Alice must choose all the three piles at the first move to win
# and leave Bob with negative score.
# If Alice chooses one pile her score will be 1 and the next move Bob's score
# becomes 5. The next move Alice will take the pile with value = -9 and lose.
# If Alice chooses two piles her score will be 3 and the next move Bob's score
# becomes 3. The next move Alice will take the pile with value = -9 and also
# lose.
# Remember that both play optimally so here Alice will choose the scenario that
# makes her win.
# 
# 
# Example 3:
# 
# 
# Input: values = [1,2,3,6]
# Output: "Tie"
# Explanation: Alice cannot win this game. She can end the game in a draw if
# she decided to choose all the first three piles, otherwise she will lose.
# 
# 
# Example 4:
# 
# 
# Input: values = [1,2,3,-1,-2,-3,7]
# Output: "Alice"
# 
# 
# Example 5:
# 
# 
# Input: values = [-1,-2,-3]
# Output: "Tie"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= values.length <= 50000
# -1000 <= values[i] <= 1000
# 
#

# @lc code=start
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        # dp[i] means, if we ignore before A[i], what's the highest score that Alex can win over the Bob？
        # There are three option for Alice to choose.
        # Take A[i], win take - dp[i+1]
        # Take A[i] + A[i+1], win take - dp[i+2]
        # Take A[i] + A[i+1] + A[i+2], win take - dp[i+3]
        # dp[i] equals the best outcome of these three solutions.
        # n = len(stoneValue)
        # dp = [float("-inf")] * n
        # for i in range(n - 1, -1, -1):
        #     k = take = 0
        #     while k < 3 and i + k < n:
        #         take += stoneValue[i + k]
        #         dp[i] = max(dp[i], take - dp[i + k + 1] if i + k + 1 < n else take)
        #         k += 1

        # return "Alice" if dp[0] > 0 else "Bob" if dp[0] < 0 else "Tie"


        def cmp(a, b): return (a > b) - (a < b)
        dp = [0] * 3
        for i in range(len(stoneValue) - 1, -1, -1):
            dp[i % 3] = max(sum(stoneValue[i:i + k]) - dp[(i + k) % 3] for k in (1, 2, 3))
        return ["Tie", "Alice", "Bob"][cmp(dp[0], 0)]




        
        
# @lc code=end

