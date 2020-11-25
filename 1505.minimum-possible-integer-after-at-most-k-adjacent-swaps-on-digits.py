#
# @lc app=leetcode id=1505 lang=python3
#
# [1505] Minimum Possible Integer After at Most K Adjacent Swaps On Digits
#
# https://leetcode.com/problems/minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/description/
#
# algorithms
# Hard (36.10%)
# Likes:    177
# Dislikes: 12
# Total Accepted:    4.7K
# Total Submissions: 13K
# Testcase Example:  '"4321"\n4'
#
# Given a string num representing the digits of a very large integer and an
# integer k.
# 
# You are allowed to swap any two adjacent digits of the integer at most k
# times.
# 
# Return the minimum integer you can obtain also as a string.
# 
# 
# Example 1:
# 
# 
# Input: num = "4321", k = 4
# Output: "1342"
# Explanation: The steps to obtain the minimum integer from 4321 with 4
# adjacent swaps are shown.
# 
# 
# Example 2:
# 
# 
# Input: num = "100", k = 1
# Output: "010"
# Explanation: It's ok for the output to have leading zeros, but the input is
# guaranteed not to have any leading zeros.
# 
# 
# Example 3:
# 
# 
# Input: num = "36789", k = 1000
# Output: "36789"
# Explanation: We can keep the number without any swaps.
# 
# 
# Example 4:
# 
# 
# Input: num = "22", k = 22
# Output: "22"
# 
# 
# Example 5:
# 
# 
# Input: num = "9438957234785635408", k = 23
# Output: "0345989723478563548"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= num.length <= 30000
# num contains digits only and doesn't have leading zeros.
# 1 <= k <= 10^9
# 
# 
#

# @lc code=start
from collections import defaultdict, deque
from sortedcontainers import SortedList
from string import digits

class Solution:
    def minInteger(self, num: str, k: int) -> str:
        # num = [*map(int, num)]
        # if k >= (len(num) ** 2) // 2:
        #     return "".join(map(str, sorted(num)))

        # res = []
        # q = [(v, i) for i, v in enumerate(num)]
        # while k and q:
        #     idx, (v, i) = min(enumerate(q[:k + 1]), key=lambda p: p[1])
        #     k -= idx
        #     del q[idx]
        #     res += v,

        # res += [v for v, _ in q]
        # return "".join(map(str, res))


        # O(nlogn)
        d = defaultdict(deque)
        for i, a in enumerate(num):
            d[a].append(i)

        ans, seen = "", SortedList()
        for _ in range(len(num)):
            for a in digits:
                if d[a]:
                    i = d[a][0]
                    dis = i - seen.bisect(i)
                    if dis <= k:
                        k -= dis
                        d[a].popleft()
                        ans += a
                        seen.add(i)
                        break

        return ans
        
# @lc code=end

