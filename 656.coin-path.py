#
# @lc app=leetcode id=656 lang=python3
#
# [656] Coin Path
#
# https://leetcode.com/problems/coin-path/description/
#
# algorithms
# Hard (28.87%)
# Likes:    163
# Dislikes: 82
# Total Accepted:    9.3K
# Total Submissions: 32.1K
# Testcase Example:  '[1,2,4,-1,2]\n2'
#
# Given an array A (index starts at 1) consisting of N integers: A1, A2, ...,
# AN and an integer B. The integer B denotes that from any place (suppose the
# index is i) in the array A, you can jump to any one of the place in the array
# A indexed i+1, i+2, …, i+B if this place can be jumped to. Also, if you step
# on the index i, you have to pay Ai coins. If Ai is -1, it means you can’t
# jump to the place indexed i in the array.
# 
# Now, you start from the place indexed 1 in the array A, and your aim is to
# reach the place indexed N using the minimum coins. You need to return the
# path of indexes (starting from 1 to N) in the array you should take to get to
# the place indexed N using minimum coins.
# 
# If there are multiple paths with the same cost, return the lexicographically
# smallest such path.
# 
# If it's not possible to reach the place indexed N then you need to return an
# empty array.
# 
# Example 1:
# 
# 
# Input: [1,2,4,-1,2], 2
# Output: [1,3,5]
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: [1,2,4,-1,2], 1
# Output: []
# 
# 
# 
# 
# Note:
# 
# 
# Path Pa1, Pa2, ..., Pan is lexicographically smaller than Pb1, Pb2, ..., Pbm,
# if and only if at the first i where Pai and Pbi differ, Pai < Pbi; when no
# such i exists, then n < m.
# A1 >= 0. A2, ..., AN (if exist) will in the range of [-1, 100].
# Length of A is in the range of [1, 1000].
# B is in the range of [1, 100].
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def cheapestJump(self, A: List[int], B: int) -> List[int]:
        # Time  complexity: O(nB)
        # Space compleixty: O(n)
        nxt = [-1] * len(A)
        dp = [0] * len(A)
        res = []

        for i in range(len(A) - 2, -1, -1):
            min_cost = float("inf")
            for j in range(i + 1, min(i + B + 1, len(A))):
                if A[j] >= 0:
                    cost = A[i] + dp[j]
                    if cost < min_cost:
                        min_cost = cost
                        nxt[i] = j
            dp[i] = min_cost

        i = 0
        while i < len(A) - 1 and nxt[i] > 0:
            res.append(i + 1)
            i = nxt[i]

        if i == len(A) - 1 and A[i] >= 0:
            res.append(len(A))
        else:
            return []

        return res
        
# @lc code=end

