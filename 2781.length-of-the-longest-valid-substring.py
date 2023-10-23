#
# @lc app=leetcode id=2781 lang=python3
#
# [2781] Length of the Longest Valid Substring
#

# @lc code=start
class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:

        forbidden_set = set(forbidden)
        res = 0
        n = len(word)
        right = n - 1
        for left in range(n - 1, -1, -1):
            for k in range(left, min(left + 10, right + 1)):
                if word[left:k + 1] in forbidden_set:
                    right = k - 1
                    break

            res = max(res, right - left + 1)

        return res
        
# @lc code=end

