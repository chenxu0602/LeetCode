#
# @lc app=leetcode id=967 lang=python3
#
# [967] Numbers With Same Consecutive Differences
#
# https://leetcode.com/problems/numbers-with-same-consecutive-differences/description/
#
# algorithms
# Medium (39.34%)
# Likes:    514
# Dislikes: 108
# Total Accepted:    38.3K
# Total Submissions: 87.7K
# Testcase Example:  '3\n7'
#
# Return all non-negative integers of length n such that the absolute
# difference between every two consecutive digits is k.
# 
# Note that every number in the answer must not have leading zeros except for
# the number 0 itself. For example, 01 has one leading zero and is invalid, but
# 0 is valid.
# 
# You may return the answer in any order.
# 
# 
# Example 1:
# 
# 
# Input: n = 3, k = 7
# Output: [181,292,707,818,929]
# Explanation: Note that 070 is not a valid number, because it has leading
# zeroes.
# 
# 
# Example 2:
# 
# 
# Input: n = 2, k = 1
# Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
# 
# 
# Example 3:
# 
# 
# Input: n = 2, k = 0
# Output: [11,22,33,44,55,66,77,88,99]
# 
# 
# Example 4:
# 
# 
# Input: n = 2, k = 1
# Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
# 
# 
# Example 5:
# 
# 
# Input: n = 2, k = 2
# Output: [13,20,24,31,35,42,46,53,57,64,68,75,79,86,97]
# 
# 
# 
# Constraints:
# 
# 
# 2 <= n <= 9
# 0 <= k <= 9
# 
# 
#

# @lc code=start
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        # DFS (Depth-First Search)
        # Time  complexity: O(N x 2^N) = O(N x 9 x 2^(N-1))
        # Space compleixty: O(2^N) = O(9 x 2^(N-1)) + O(N)
        # if n == 1:
        #     return [i for i in range(10)]

        # ans = []
        # def dfs(n, num):
        #     # base case
        #     if n == 0:
        #         return ans.append(num)

        #     tail_digit = num % 10
        #     # using set() to avoid duplicates when K == 0
        #     next_digits = set([tail_digit + k, tail_digit - k])

        #     for next_digit in next_digits:
        #         if 0 <= next_digit < 10:
        #             new_num = num * 10 + next_digit
        #             dfs(n - 1, new_num)

        # for num in range(1, 10):
        #     dfs(n - 1, num)

        # return list(ans)


        # BFS (Breadth-First Search)
        # Time  complexity: O(N x 2^N)
        # Space complexity: O(2^N)
        # if n == 1:
        #     return [i for i in range(10)]

        # # initialize the queue with candidates for the first level
        # queue = [digit for digit in range(1, 10)]

        # for level in range(n - 1):
        #     next_queue = []
        #     for num in queue:
        #         tail_digit = num % 10
        #         # using set() to avoid duplicates when K == 0
        #         next_digits = set([tail_digit + k, tail_digit - k])

        #         for next_digit in next_digits:
        #             if 0 <= next_digit < 10:
        #                 new_num = num * 10 + next_digit
        #                 next_queue.append(new_num)

        #     # start the next level
        #     queue = next_queue

        # return queue


        cur = range(10)
        for i in range(n - 1):
            cur = {x * 10 + y for x in cur for y in [x % 10 + k, x % 10 - k] if x and 0 <= y < 10}
        return list(cur)
        
# @lc code=end

