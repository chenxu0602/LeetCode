#
# @lc app=leetcode id=3044 lang=python3
#
# [3044] Most Frequent Prime
#

# @lc code=start
from collections import Counter
from math import isqrt

class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:

        m, n = map(len, (mat, mat[0]))
        directions = (-1, 0, 1)

        def isPrime(num):
            if num < 10 or num % 2 == 0: return False
            for i in range(3, isqrt(num) + 1, 2):
                if num % i == 0: return False
            return True

        nums = []
        for i in range(m):
            for j in range(n):
                for di in directions:
                    for dj in directions:
                        if di == 0 == dj: continue
                        ni, nj = i + di, j + dj
                        num = mat[i][j]
                        while 0 <= ni < m and 0 <= nj < n:
                            nums.append(num := num * 10 + mat[ni][nj])
                            ni += di
                            nj += dj

        return max(filter(isPrime, ctr := Counter(nums)), key=lambda x: (ctr[x], x), default=-1)
                        
        
# @lc code=end

