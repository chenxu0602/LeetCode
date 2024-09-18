#
# @lc app=leetcode id=3234 lang=python3
#
# [3234] Count the Number of Substrings With Dominant Ones
#

# @lc code=start
from collections import deque

class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        # Time  complexity: O(n x sqrt(n))
        # Space complexity: O(n)

        n, res = len(s), 0

        for k in range(1, int(n ** 0.5) + 1):
            zeros, last_zero, ones = deque(), -1, 0
            
            for right in range(n):
                if s[right] == '0':
                    zeros.append(right)
                    while len(zeros) > k:
                        ones -= (zeros[0] - last_zero - 1)
                        last_zero = zeros.popleft()
                else:
                    ones += 1

                if len(zeros) == k and ones >= k ** 2:
                    res += min(zeros[0] - last_zero, ones - k ** 2 + 1)

        
        # All 1s case
        i = 0
        while i < n:
            if s[i] == '0':
                i += 1
                continue

            sz = 0
            while i < n and s[i] == '1':
                sz += 1
                i += 1

            res += sz * (sz + 1) // 2

        return res
        
# @lc code=end

