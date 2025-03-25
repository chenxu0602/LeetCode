#
# @lc app=leetcode id=3271 lang=python3
#
# [3271] Hash Divided String
#

# @lc code=start
from string import ascii_lowercase

class Solution:
    def stringHash(self, s: str, k: int) -> str:

        arr =  [ord(c) - 97 for c in s]
        return ''.join([ascii_lowercase[sum(arr[i:i + k]) % 26] for i in range(0, len(arr), k)])
        
# @lc code=end

