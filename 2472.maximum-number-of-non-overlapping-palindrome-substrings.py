#
# @lc app=leetcode id=2472 lang=python3
#
# [2472] Maximum Number of Non-overlapping Palindrome Substrings
#

# @lc code=start
class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:


        
        # O(nk)
        # First find all palindromic substrings with length >= k in O(n*k) and store their start and end in an intervals list
        # Then find minumum number of intervals you need to remove to make the intervals array non overlapping in O(n) (intervals is already added in sorted order.)

        n = len(s)
        intervals = []
        last = float("-inf")
        ans = 0

        for center in range(2 * n - 1):
            left = center // 2
            right = left + center % 2
            while left >= 0 and right < n and s[left] == s[right]:
                if right + 1 - left >= k:
                    intervals.append((left, right + 1))
                    break
                left -= 1
                right += 1

        for x, y in intervals:
            if x >= last:
                last = y
                ans += 1
            else:
                if y < last:
                    last = y

        return ans
        
# @lc code=end

