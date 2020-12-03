#
# @lc app=leetcode id=1601 lang=python3
#
# [1601] Maximum Number of Achievable Transfer Requests
#
# https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/description/
#
# algorithms
# Hard (46.91%)
# Likes:    146
# Dislikes: 19
# Total Accepted:    4.9K
# Total Submissions: 10.5K
# Testcase Example:  '5\n[[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]'
#
# We have n buildings numbered from 0 to n - 1. Each building has a number of
# employees. It's transfer season, and some employees want to change the
# building they reside in.
# 
# You are given an array requests where requests[i] = [fromi, toi] represents
# an employee's request to transfer from building fromi to building toi.
# 
# All buildings are full, so a list of requests is achievable only if for each
# building, the net change in employee transfers is zero. This means the number
# of employees leaving is equal to the number of employees moving in. For
# example if n = 3 and two employees are leaving building 0, one is leaving
# building 1, and one is leaving building 2, there should be two employees
# moving to building 0, one employee moving to building 1, and one employee
# moving to building 2.
# 
# Return the maximum number of achievable requests.
# 
# 
# Example 1:
# 
# 
# Input: n = 5, requests = [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]
# Output: 5
# Explantion: Let's see the requests:
# From building 0 we have employees x and y and both want to move to building
# 1.
# From building 1 we have employees a and b and they want to move to buildings
# 2 and 0 respectively.
# From building 2 we have employee z and they want to move to building 0.
# From building 3 we have employee c and they want to move to building 4.
# From building 4 we don't have any requests.
# We can achieve the requests of users x and b by swapping their places.
# We can achieve the requests of users y, a and z by swapping the places in the
# 3 buildings.
# 
# 
# Example 2:
# 
# 
# Input: n = 3, requests = [[0,0],[1,2],[2,1]]
# Output: 3
# Explantion: Let's see the requests:
# From building 0 we have employee x and they want to stay in the same building
# 0.
# From building 1 we have employee y and they want to move to building 2.
# From building 2 we have employee z and they want to move to building 1.
# We can achieve all the requests. 
# 
# Example 3:
# 
# 
# Input: n = 4, requests = [[0,3],[3,1],[1,2],[2,0]]
# Output: 4
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 20
# 1 <= requests.length <= 16
# requests[i].length == 2
# 0 <= fromi, toi < n
# 
# 
#

# @lc code=start
import itertools 

class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        # For each combination, use a mask to present the picks.
        # The kth bits means we need to satisfy the kth request.
        # If for all buildings, in degrees == out degrees, it's achievable.
        # Time  complexity: O((N + R) x 2^R)
        # Space complexity: O(N)

        # m = len(requests) 
        # if m == 0: return 0

        # for k in range(m, 0, -1):
        #     for c in itertools.combinations(range(m), k):
        #         degree = [0] * n
        #         for i in c:
        #             degree[requests[i][0]] -= 1
        #             degree[requests[i][1]] += 1

        #         if not any(degree):
        #             return k

        # return 0


        # m = len(requests)
        # res = 0

        # def test(mask):
        #     outd, ind = [0] * n, [0] * n
        #     for k in range(m):
        #         if 1 << k & mask:
        #             outd[requests[k][0]] += 1
        #             ind[requests[k][1]] += 1
        #     return sum(outd) if outd == ind else 0

        # for i in range(1 << m):
        #     res = max(res, test(i))

        # return res


        # maximize sum(x_i)
        # subject to sum(x_j) - sum(x_i) = 0
        from scipy.optimize import linprog
        m = len(requests)
        cost = [-1] * m
        A = [[0] * m for _ in range(n)]
        b = [0] * n

        for i, (u, v) in enumerate(requests):
            A[u][i] -= 1
            A[v][i] += 1

        res = linprog(cost, A_eq=A, b_eq=b, bounds=(0, 1))
        return round(-res.fun)
        
# @lc code=end

