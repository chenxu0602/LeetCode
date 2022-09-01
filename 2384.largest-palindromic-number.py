#
# @lc app=leetcode id=2384 lang=python3
#
# [2384] Largest Palindromic Number
#

# @lc code=start
from collections import Counter

class Solution:
    def largestPalindromic(self, num: str) -> str:
        count = Counter(num)
        res = ''.join(count[i] // 2 * i for i in "9876543210").lstrip('0')
        mid = max(count[i] % 2 * i for i in count)
        return res + mid + res[::-1] or '0'
        
# @lc code=end

