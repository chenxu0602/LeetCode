#
# @lc app=leetcode id=2231 lang=python3
#
# [2231] Largest Number After Digit Swaps by Parity
#

# @lc code=start
import heapq

class Solution:
    def largestInteger(self, num: int) -> int:
        odd, even = [], []

        nums = list(str(num))
        n = len(nums)

        for i in range(n):
            d = ord(nums[i]) - ord('0')
            if d % 2:
                heapq.heappush(odd, -d)
            else:
                heapq.heappush(even, -d)

        ans = 0
        for i in range(n):
            ans *= 10
            if int(nums[i]) % 2:
                ans -= heapq.heappop(odd)
            else:
                ans -= heapq.heappop(even)

        return ans
        
# @lc code=end

