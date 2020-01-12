#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#
# https://leetcode.com/problems/count-primes/description/
#
# algorithms
# Easy (29.61%)
# Likes:    1333
# Dislikes: 454
# Total Accepted:    277K
# Total Submissions: 923.4K
# Testcase Example:  '10'
#
# Count the number of prime numbers less than a non-negative number, n.
# 
# Example:
# 
# 
# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
# 
# 
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        res = [True] * n
        res[0] = res[1] = False

        for i in range(2, int(n**0.5)+1):
            if res[i]:
                """
                for j in range(2, (n-1)//i+1):
                    res[i*j] = False
                """
                res[i*i:n:i] = [0] * ((n-1-i*i)//i + 1)

        return sum(res)
        
# @lc code=end

