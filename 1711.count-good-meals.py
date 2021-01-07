#
# @lc app=leetcode id=1711 lang=python3
#
# [1711] Count Good Meals
#
# https://leetcode.com/problems/count-good-meals/description/
#
# algorithms
# Medium (25.21%)
# Likes:    112
# Dislikes: 106
# Total Accepted:    7.3K
# Total Submissions: 29K
# Testcase Example:  '[1,3,5,7,9]'
#
# A good meal is a meal that contains exactly two different food items with a
# sum of deliciousness equal to a power of two.
# 
# You can pick any two different foods to make a good meal.
# 
# Given an array of integers deliciousness where deliciousness[i] is the
# deliciousness of the i^​​​​​​th​​​​​​​​ item of food, return the number of
# different good meals you can make from this list modulo 10^9 + 7.
# 
# Note that items with different indices are considered different even if they
# have the same deliciousness value.
# 
# 
# Example 1:
# 
# 
# Input: deliciousness = [1,3,5,7,9]
# Output: 4
# Explanation: The good meals are (1,3), (1,7), (3,5) and, (7,9).
# Their respective sums are 4, 8, 8, and 16, all of which are powers of 2.
# 
# 
# Example 2:
# 
# 
# Input: deliciousness = [1,1,1,3,3,3,7]
# Output: 15
# Explanation: The good meals are (1,1) with 3 ways, (1,3) with 9 ways, and
# (1,7) with 3 ways.
# 
# 
# Constraints:
# 
# 
# 1 <= deliciousness.length <= 10^5
# 0 <= deliciousness[i] <= 2^20
# 
# 
#

# @lc code=start
from collections import Counter
import math

class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        count = Counter(deliciousness)
        ans = 0
        for k in sorted(count):
            for p in range(22):
                x = 2**p
                if x % 2 == 0 and k == x // 2: # take care of case k == 0, p == 0, x == 1
                    ans += count[k] * (count[k] - 1) // 2
                elif k < x - k:
                    r = count[k] * count[x - k]
                    ans += r

        return ans % (10**9 + 7)


        # count = Counter()
        # res = 0
        # for d in deliciousness:
        #     for i in range(22):
        #         res += count[2**i - d]
        #     count[d] += 1
        # return res % (10**9 + 7)


        
# @lc code=end

