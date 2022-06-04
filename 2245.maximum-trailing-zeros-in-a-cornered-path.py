#
# @lc app=leetcode id=2245 lang=python3
#
# [2245] Maximum Trailing Zeros in a Cornered Path
#

# @lc code=start
class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        m, n = map(len, (grid, grid[0]))
        left = [[(0, 0) for _ in range(n)] for _ in range(m)]
        top = [[(0, 0) for _ in range(n)] for _ in range(m)]

        def helper(num):
            a, b = 0, 0
            while num % 2 == 0:
                num //= 2
                a += 1

            while num % 5 == 0:
                num //= 5
                b += 1
            
            return (a, b)

        for i in range(m):
            for j in range(n):
                if j == 0:
                    left[i][j] = helper(grid[i][j])
                else:
                    a, b = helper(grid[i][j])
                    left[i][j] = (left[i][j - 1][0] + a, left[i][j - 1][1] + b)

        for j in range(n):
            for i in range(m):
                if i == 0:
                    top[i][j] = helper(grid[i][j])
                else:
                    a, b = helper(grid[i][j])
                    top[i][j] = (top[i - 1][j][0] + a, top[i - 1][j][1] + b)

        ans = 0
        for i in range(m):
            for j in range(n):
                a, b = top[m - 1][j]
                d, e = left[i][n - 1]

                x, y = helper(grid[i][j])
                a1, b1 = top[i][j]
                a2, b2 = left[i][j]

                tmp = [a1 + a2 - x, b1 + b2 - y]
                ans = max(ans, min(tmp))

                tmp = [d - a2 + a1, e - b2 + b1]
                ans = max(ans, min(tmp))

                tmp = [a - a1 + a2, b - b1 + b2]
                ans = max(ans, min(tmp))

                tmp = [a + d - a1 - a2 + x, b + e - b1 - b2 + y]
                ans = max(ans, min(tmp))

        return ans

        
# @lc code=end

