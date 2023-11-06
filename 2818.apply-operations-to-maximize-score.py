#
# @lc app=leetcode id=2818 lang=python3
#
# [2818] Apply Operations to Maximize Score
#

# @lc code=start
MOD = 1_000_000_007
primes, scores = [True] * 100001, [0] * 100001
for i in range(2, 100001):
    if primes[i]:
        for j in range(i, 100001, i):
            primes[j]  = False
            scores[j] += 1

primes[0] = primes[1] = False
scores[0] = scores[1] = 0


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:

        n = len(nums)
        s = [scores[num] for num in nums]

        left, right = [-1] * n, [n] * n
        for i in range(1, n):
            j = i - 1
            while j >= 0 and s[j] < s[i]:
                j = left[j]
            left[i] = j
        
        for i in range(n - 2, -1, -1):
            j = i + 1
            while j < n and s[j] <= s[i]:
                j = right[j]
            right[i] = j

        ranges = [(i - left[i]) * (right[i] - i) for i in range(n)]

        candidates = sorted([(nums[i], ranges[i]) for i in range(n)], reverse=True)

        score = 1
        i = 0
        while k > 0:
            power = min(candidates[i][1], k)
            score *= pow(candidates[i][0], power, MOD)
            k -= power
            i += 1

        return score % MOD
        
# @lc code=end

