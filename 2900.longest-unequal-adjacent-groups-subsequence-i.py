#
# @lc app=leetcode id=2900 lang=python3
#
# [2900] Longest Unequal Adjacent Groups Subsequence I
#

# @lc code=start
class Solution:
    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:

        ans = []
        t = groups[0]
        ans += words[0],

        for i in range(1, n):
            if groups[i] != t:
                t = groups[i]
                ans += words[i],

        return ans
        
# @lc code=end

