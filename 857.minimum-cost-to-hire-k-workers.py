#
# @lc app=leetcode id=857 lang=python3
#
# [857] Minimum Cost to Hire K Workers
#
# https://leetcode.com/problems/minimum-cost-to-hire-k-workers/description/
#
# algorithms
# Hard (49.52%)
# Likes:    941
# Dislikes: 96
# Total Accepted:    31.2K
# Total Submissions: 62.8K
# Testcase Example:  '[10,20,5]\n[70,50,30]\n2'
#
# There are N workers.  The i-th worker has a quality[i] and a minimum wage
# expectation wage[i].
# 
# Now we want to hire exactly K workers to form a paid group.  When hiring a
# group of K workers, we must pay them according to the following rules:
# 
# 
# Every worker in the paid group should be paid in the ratio of their quality
# compared to other workers in the paid group.
# Every worker in the paid group must be paid at least their minimum wage
# expectation.
# 
# 
# Return the least amount of money needed to form a paid group satisfying the
# above conditions.
# 
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: quality = [10,20,5], wage = [70,50,30], K = 2
# Output: 105.00000
# Explanation: We pay 70 to 0-th worker and 35 to 2-th worker.
# 
# 
# 
# Example 2:
# 
# 
# Input: quality = [3,1,10,10,1], wage = [4,8,2,2,7], K = 3
# Output: 30.66667
# Explanation: We pay 4 to 0-th worker, 13.33333 to 2-th and 3-th workers
# seperately. 
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= K <= N <= 10000, where N = quality.length = wage.length
# 1 <= quality[i] <= 10000
# 1 <= wage[i] <= 10000
# Answers within 10^-5 of the correct answer will be considered correct.
# 
# 
# 
# 
#

# @lc code=start
from fractions import Fraction
import heapq

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        # Greedy
        # Time  complexity: O(N^2 x logN), where N is the number of workers.
        # Space complexity: O(N)
        # ans, N = float("inf"), len(quality)
        # for captain in range(N):
        #     # Must pay at least wage[captain] / quality[captain] per qual
        #     factor = Fraction(wage[captain], quality[captain])
        #     prices = []
        #     for worker in range(N):
        #         price = factor * quality[worker]
        #         if price < wage[worker]: continue
        #         prices.append(price)

        #     if len(prices) < K: continue
        #     prices.sort()
        #     ans = min(ans, sum(prices[:K]))

        # return float(ans)


        # Heap
        # The key insight is to iterate over the ratio. Let's say we hire workers with a ratio R or lower. 
        # Then, we would want to know the K workers with the lowest quality, and the sum of that quality. 
        # Time  complexity: O(NlogN)
        # Space complexity: O(N)
        workers = sorted((Fraction(w, q), q, w) for q, w in zip(quality, wage))
        ans, pool, sumq = float("inf"), [], 0

        # Loop over from the lowest ratio to highest ratio
        for ratio, q, w in workers:
            heapq.heappush(pool, -q)
            sumq += q

            if len(pool) > K:
                sumq += heapq.heappop(pool)

            if len(pool) == K:
                ans = min(ans, ratio * sumq)

        return float(ans)
        
# @lc code=end

