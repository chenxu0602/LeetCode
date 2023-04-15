#
# @lc app=leetcode id=2614 lang=python3
#
# [2614] Prime In Diagonal
#

# @lc code=start
class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:

        def is_prime(num):
            if num <= 1:
                return False
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True

        largest_prime = 0
        n = len(nums)
        for i in range(n):
            if is_prime(nums[i][i]):
                largest_prime = max(largest_prime, nums[i][i])
            if is_prime(nums[i][n - i - 1]):
                largest_prime = max(largest_prime, nums[i][n - i - 1])

        return largest_prime
        
# @lc code=end

