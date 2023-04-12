#
# @lc app=leetcode id=2607 lang=python3
#
# [2607] Make K-Subarray Sums Equal
#

# @lc code=start
import math
from collections import defaultdict

class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:

        n = len(arr)
        n_buckets = math.gcd(k, n)
        buckets = defaultdict(list)

        for i, num in enumerate(arr):
            buckets[i % n_buckets].append(num)

        res = 0
        for bucket_id, bucket in buckets.items():
            bucket.sort()
            median = bucket[len(bucket) // 2] # could be improved by using quick select

            for num in bucket:
                res += abs(median - num)

        return res
        
# @lc code=end

