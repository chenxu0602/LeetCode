#
# @lc app=leetcode id=2176 lang=python3
#
# [2176] Count Equal and Divisible Pairs in an Array
#

# @lc code=start
from collections import defaultdict

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        counter = defaultdict(list)
        for i in range(len(nums)):
            counter[nums[i]].append(i)

        ans = 0
        for key, v in counter.items():
            l = len(v)
            for i in range(l - 1):
                for j in range(i + 1, l):
                    if v[i] * v[j] % k == 0:
                        ans += 1

        return ans
        
# @lc code=end

