#
# @lc app=leetcode id=2033 lang=python3
#
# [2033] Minimum Operations to Make a Uni-Value Grid
#

# @lc code=start
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:

        def get_num_operations_to_target(grid, cand, x):
            ans = 0
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if abs(grid[i][j] - cand) % x:
                        return -1
                    else:
                        ans += abs(grid[i][j] - cand) // x

            return ans

        m, n = map(len, (grid, grid[0]))
        if m == 1 and n == 1: return 0

        arr = []
        for i in range(m):
            arr += grid[i]

        arr.sort()
        cand1 = arr[len(arr) // 2]
        cand2 = arr[len(arr) // 2 - 1]

        return min(get_num_operations_to_target(grid, cand1, x), get_num_operations_to_target(grid, cand2, x))
        
# @lc code=end

