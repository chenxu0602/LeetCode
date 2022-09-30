#
# @lc app=leetcode id=2412 lang=python3
#
# [2412] Minimum Money Required Before Transactions
#

# @lc code=start
class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        L, E = [a for a in transactions if a[0] > a[1]], [a for a in transactions if a[0] <= a[1]]
        L.sort(key=lambda x: x[1])

        budget, curr = 0, 0

        for a, b in L:
            curr -= a
            budget = min(budget, curr)
            curr += b

        if E:
            curr -= max(e[0] for e in E)
            budget = min(budget, curr)

        return -budget

        # res = v = 0
        # for i, j in transactions:
        #     res += max(0, i - j)
        #     v = max(v, min(i, j))
        # return res + v

        # return sum(max(0, i - j) for i, j in transactions) + max(map(min, transactions))
        
# @lc code=end

