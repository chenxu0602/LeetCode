#
# @lc app=leetcode id=2451 lang=python3
#
# [2451] Odd String Difference
#

# @lc code=start
class Solution:
    def oddString(self, words: List[str]) -> str:

        diff = lambda x: [ord(x[j]) - ord(x[j - 1]) for j in range(1, len(x))]
        words.sort(key=diff)
        return words[0] if diff(words[0]) != diff(words[1]) else words[-1]

        
# @lc code=end

