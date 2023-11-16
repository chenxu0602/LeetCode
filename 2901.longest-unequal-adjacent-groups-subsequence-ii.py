#
# @lc app=leetcode id=2901 lang=python3
#
# [2901] Longest Unequal Adjacent Groups Subsequence II
#

# @lc code=start
class Solution:
    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:

        # dp and pv, to keep track of the maximum subsequence length and the previous word index 
        # in the longest subsequence, respectively.
        n = len(groups)
        dp, pv = [1] * n, [-1] * n

        for i in range(1, n):
            for j in range(i):
                if groups[i] == groups[j]:
                    continue

                if len(words[i]) != len(words[j]):
                    continue

                diff = sum(1 for k in range(len(words[i])) if words[i][k] != words[j][k])

                if diff != 1: continue

                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    pv[i] = j


        wi = dp.index(max(dp))
        ans = []

        while wi != -1:
            ans += words[wi],
            wi = pv[wi]

        return reversed(ans)

        
# @lc code=end

