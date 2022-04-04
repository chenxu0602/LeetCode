#
# @lc app=leetcode id=2131 lang=python3
#
# [2131] Longest Palindrome by Concatenating Two Letter Words
#

# @lc code=start
from collections import defaultdict

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:

        """
        m = defaultdict(int)
        unpaired = ans = 0

        for w in words:
            if w[0] == w[1]:
                if m[w] > 0:
                    unpaired -= 1
                    m[w] -= 1
                    ans += 4
                else:
                    m[w] += 1
                    unpaired += 1

            else:
                if m[w[::-1]] > 0:
                    ans += 4
                    m[w[::-1]] -= 1
                else:
                    m[w] += 1

        if unpaired > 0:
            ans += 2

        return ans 
        """

        counter, ans = [[0] * 26 for _ in range(26)], 0
        for w in words:
            a, b = ord(w[0]) - ord('a'), ord(w[1]) - ord('a')
            if counter[b][a]:
                ans += 4
                counter[b][a] -= 1
            else:
                counter[a][b] += 1

        for i in range(26):
            if counter[i][i]:
                ans += 2
                break 

        return ans 


# @lc code=end

