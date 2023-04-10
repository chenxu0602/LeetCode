#
# @lc app=leetcode id=2584 lang=python3
#
# [2584] Split the Array to Make Coprime Products
#

# @lc code=start
import math
from collections import defaultdict

mx = 10 ** 6
spf = [i for i in range(mx + 1)]
for i in range(2, int(math.sqrt(mx)) + 1):
    if spf[i] == i:
        for j in range(i * i, mx + 1, i):
            spf[j] = min(spf[j], i)

def getPrimeFactors(x):
    while x != 1:
        yield spf[x]
        x //= spf[x]
        
class Solution:
    def findValidSplit(self, nums: List[int]) -> int:

        # We record the right-most index of each prime factor into a dictionary. Then start from arr[0], we keep updating the right-most index scanned so far. If the current right-most index is "i" itself, then that means "i" is the smallest splitting point.
        fac_idx = defaultdict(int)
        for i, v in enumerate(nums):
            for fac in getPrimeFactors(v):
                fac_idx[fac] = i

        right_most = 0
        for i in range(len(nums) - 1):
            for fac in getPrimeFactors(nums[i]):
                right_most = max(right_most, fac_idx[fac])

            if right_most == i:
                return i

        return -1
# @lc code=end

