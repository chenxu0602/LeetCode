#
# @lc app=leetcode id=838 lang=python3
#
# [838] Push Dominoes
#
# https://leetcode.com/problems/push-dominoes/description/
#
# algorithms
# Medium (44.63%)
# Likes:    342
# Dislikes: 39
# Total Accepted:    13.8K
# Total Submissions: 30.7K
# Testcase Example:  '".L.R...LR..L.."'
#
# There are N dominoes in a line, and we place each domino vertically upright.
# 
# In the beginning, we simultaneously push some of the dominoes either to the
# left or to the right.
# 
# 
# 
# After each second, each domino that is falling to the left pushes the
# adjacent domino on the left.
# 
# Similarly, the dominoes falling to the right push their adjacent dominoes
# standing on the right.
# 
# When a vertical domino has dominoes falling on it from both sides, it stays
# still due to the balance of the forces.
# 
# For the purposes of this question, we will consider that a falling domino
# expends no additional force to a falling or already fallen domino.
# 
# Given a string "S" representing the initial state. S[i] = 'L', if the i-th
# domino has been pushed to the left; S[i] = 'R', if the i-th domino has been
# pushed to the right; S[i] = '.', if the i-th domino has not been pushed.
# 
# Return a string representing the final state. 
# 
# Example 1:
# 
# 
# Input: ".L.R...LR..L.."
# Output: "LL.RR.LLRRLL.."
# 
# 
# Example 2:
# 
# 
# Input: "RR.L"
# Output: "RR.L"
# Explanation: The first domino expends no additional force on the second
# domino.
# 
# 
# Note:
# 
# 
# 0 <= N <= 10^5
# String dominoes contains only 'L', 'R' and '.'
# 
# 
#
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        # Adjacent Symbols
        # O(N)
        def cmp(a, b):
            return (a > b) - (a < b)
        
        symbols = [(i, x) for i, x in enumerate(dominoes) if x != '.']
        symbols = [(-1, 'L')] + symbols + [(len(dominoes), 'R')]

        ans = list(dominoes)
        for (i, x), (j, y) in zip(symbols, symbols[1:]):
            if x == y:
                for k in range(i + 1, j):
                    ans[k] = x
            elif x > y: # RL
                for k in range(i + 1, j):
                    ans[k] = '.LR'[cmp(k - i, j - k)]

        return ''.join(ans)


        # Calculate Force
        # O(N)
        # N = len(dominoes)
        # force = [0] * N

        # # Populate forces going from left to right
        # f = 0
        # for i in range(N):
        #     if dominoes[i] == 'R':
        #         f = N
        #     elif dominoes[i] == 'L':
        #         f = 0
        #     else:
        #         f = max(f - 1, 0)
        #     force[i] += f

        # # Populate forces going from right to left
        # for i in range(N - 1, -1, -1):
        #     if dominoes[i] == 'L':
        #         f = N
        #     elif dominoes[i] == 'R':
        #         f = 0
        #     else:
        #         f = max(f - 1, 0)
        #     force[i] -= f

        # return ''.join('.' if f == 0 else 'R' if f > 0 else 'L' for f in force)


        

