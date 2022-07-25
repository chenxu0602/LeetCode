#
# @lc app=leetcode id=2325 lang=python3
#
# [2325] Decode the Message
#

# @lc code=start
import string

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mapping = {' ': ' '}
        res = ""
        i = 0

        for c in key:
            if c not in mapping:
                mapping[c] = string.ascii_lowercase[i]
                i += 1

        for c in message:
            res += mapping[c]

        return res
        
# @lc code=end

