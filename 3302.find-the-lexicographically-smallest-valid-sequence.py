#
# @lc app=leetcode id=3302 lang=python3
#
# [3302] Find the Lexicographically Smallest Valid Sequence
#

# @lc code=start
class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:

        m, n = map(len, (word1, word2))
        last = [-1] * n
        j = n - 1
        for i in range(m - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                last[j] = i
                j -= 1

        res = []
        skip = j = 0
        for i, c in enumerate(word1):
            if j == n: break
            if word1[i] == word2[j] or skip == 0 and (j == n - 1 or i < last[j + 1]):
                skip += word1[i] != word2[j]
                res += i,
                j += 1

        return res if j == n else []
        
# @lc code=end

