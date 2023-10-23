#
# @lc app=leetcode id=2785 lang=python3
#
# [2785] Sort Vowels in a String
#

# @lc code=start
from collections import deque 

class Solution:
    def sortVowels(self, s: str) -> str:

        vowels, ans = "AEIOUaeiou", ""

        sVowels = deque(sorted(filter(lambda x: x in vowels, s)))

        for c in s:
            if c in vowels:
                ans += sVowels.popleft()
            else:
                ans += c

        return ans 

        
# @lc code=end

