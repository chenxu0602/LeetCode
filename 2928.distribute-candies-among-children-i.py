#
# @lc app=leetcode id=2928 lang=python3
#
# [2928] Distribute Candies Among Children I
#

# @lc code=start
from math import comb

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:

        # count = 0
        # for i in range(min(n, limit) + 1):
        #     for j in range(min(n - i, limit) + 1):
        #         k = n - i - j
        #         if 0 <= k <= limit:
        #             count += 1

        # return count


        def count_ways(candies):
            # Using the stars and bars method: 
            # - Stars (*) represent candies
            # - Bars (|) represent dividers between children
            # For example, to distribute 5 candies among 3 children, a configuration 
            # might look like '**|*|**', meaning 2 candies for the first child, 
            # 1 for the second, and 2 for the third.
            # In total, we have 'candies' stars and 2 bars (for 3 children). 
            # The number of ways to arrange these is comb(candies + 2, 2).
            if candies < 0: return 0
            return comb(candies + 2, 2)

        total_ways = count_ways(n)

        # Apply inclusion-exclusion principle
        # Subtract cases where one or more children exceed the limit
        over_limit = limit + 1
        total_ways -= 3 * count_ways(n - over_limit)

        # Add back cases where two or more children exceed the limit
        total_ways += 3 * count_ways(n - 2 * over_limit)

        # Subtract cases where all three children exceed the limit
        total_ways -= count_ways(n - 3 * over_limit)

        return total_ways

        
# @lc code=end

