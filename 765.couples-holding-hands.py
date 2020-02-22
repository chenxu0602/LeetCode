#
# @lc app=leetcode id=765 lang=python3
#
# [765] Couples Holding Hands
#
# https://leetcode.com/problems/couples-holding-hands/description/
#
# algorithms
# Hard (53.49%)
# Likes:    509
# Dislikes: 53
# Total Accepted:    20.8K
# Total Submissions: 38.8K
# Testcase Example:  '[0,2,1,3]'
#
# 
# N couples sit in 2N seats arranged in a row and want to hold hands.  We want
# to know the minimum number of swaps so that every couple is sitting side by
# side.  A swap consists of choosing any two people, then they stand up and
# switch seats. 
# 
# The people and seats are represented by an integer from 0 to 2N-1, the
# couples are numbered in order, the first couple being (0, 1), the second
# couple being (2, 3), and so on with the last couple being (2N-2, 2N-1).
# 
# The couples' initial seating is given by row[i] being the value of the person
# who is initially sitting in the i-th seat.
# 
# Example 1:
# Input: row = [0, 2, 1, 3]
# Output: 1
# Explanation: We only need to swap the second (row[1]) and third (row[2])
# person.
# 
# 
# Example 2:
# Input: row = [3, 2, 0, 1]
# Output: 0
# Explanation: All couples are already seated side by side.
# 
# 
# 
# Note:
# ⁠
# ⁠len(row) is even and in the range of [4, 60].
# ⁠row is guaranteed to be a permutation of 0...len(row)-1.
# 
#

# @lc code=start
class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:

        # ans = 0
        # for i in range(0, len(row), 2):
        #     x = row[i]
        #     if row[i+1] == x ^ 1:
        #         continue
        #     ans += 1
        #     for j in range(i+1, len(row)):
        #         if row[j] == x ^ 1:
        #             row[i+1], row[j] = row[j], row[i+1]
        #             break
        # return ans

        # pairs = {}
        # for i in range(0, len(row), 2):
        #     pairs[row[i]] = row[i+1]
        #     pairs[row[i+1]] = row[i]

        # res = 0
        # for pos in range(0, len(row), 2):
        #     if pairs[pos] != pos + 1:
        #         right = pairs[pos]
        #         left = pairs[pos+1]
        #         pairs[left], pairs[right] = right, left
        #         res += 1
        # return res

        N = len(row)
        d = [0] * N

        def find(a):
            if d[a] != a:
                d[a] = find(d[a])
            return d[a]

        def union(a, b):
            d[find(a)] = d[find(b)]

        for i in range(0, N, 2):
            d[i] = d[i+1] = i

        for i in range(0, N, 2):
            union(row[i], row[i+1])

        return (N // 2) - sum([1 for i in range(0, N, 2) if i == d[i] == d[i+1]])
        
# @lc code=end

