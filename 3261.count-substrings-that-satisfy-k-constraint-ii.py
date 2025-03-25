#
# @lc app=leetcode id=3261 lang=python3
#
# [3261] Count Substrings That Satisfy K-Constraint II
#

# @lc code=start
from collections import Counter
from itertools import accumulate

class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[List[int]]) -> List[int]:

        # Use sliding window to find maximum windows for right index and left index seperately. Use that to calculate the results. 

        n = len(s)
        left_to_right = [0] * n
        right_to_left = [0] * n

        left = 0
        counts = Counter()
        for right in range(n):
            counts[s[right]] += 1
            while counts['0'] > k and counts['1'] > k:
                counts[s[left]] -= 1
                left += 1
            right_to_left[right] = left

        right = n - 1
        counts = Counter()
        for left in reversed(range(n)):
            counts[s[left]] += 1
            while counts['0'] > k and counts['1'] > k:
                counts[s[right]] -= 1
                right -= 1
            left_to_right[left] = right

        pref_sum = [0] + list(accumulate([(right - left + 1) for right, left in enumerate(right_to_left)]))        
        result = []
        for left_bound, right_bound in queries:
            mid = min(right_bound, left_to_right[left_bound])
            length = mid - left_bound + 1
            curr = length * (length + 1) // 2
            curr += pref_sum[right_bound + 1] - pref_sum[mid + 1]
            result += curr,

        return result


        
# @lc code=end

