#
# @lc app=leetcode id=6916 lang=python3
#
# [6916] Prime Pairs With Target Sum
#

# @lc code=start
class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:

        prime = [False, False] + [True] * (n - 1)
        for i in range(2, n + 1):
            if prime[i]:
                for j in range(i * i, n + 1, i):
                    prime[j] = False

        return [[i, n - i] for i in range(2, n // 2 + 1) if prime[i] and prime[n - i]]
        
# @lc code=end

