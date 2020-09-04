#
# @lc app=leetcode id=721 lang=python3
#
# [721] Accounts Merge
#
# https://leetcode.com/problems/accounts-merge/description/
#
# algorithms
# Medium (48.44%)
# Likes:    1575
# Dislikes: 312
# Total Accepted:    90.7K
# Total Submissions: 184.9K
# Testcase Example:  '[["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]'
#
# Given a list accounts, each element accounts[i] is a list of strings, where
# the first element accounts[i][0] is a name, and the rest of the elements are
# emails representing emails of the account.
# 
# Now, we would like to merge these accounts.  Two accounts definitely belong
# to the same person if there is some email that is common to both accounts.
# Note that even if two accounts have the same name, they may belong to
# different people as people could have the same name.  A person can have any
# number of accounts initially, but all of their accounts definitely have the
# same name.
# 
# After merging the accounts, return the accounts in the following format: the
# first element of each account is the name, and the rest of the elements are
# emails in sorted order.  The accounts themselves can be returned in any
# order.
# 
# Example 1:
# 
# Input: 
# accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John",
# "johnnybravo@mail.com"], ["John", "johnsmith@mail.com",
# "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
# Output: [["John", 'john00@mail.com', 'john_newyork@mail.com',
# 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary",
# "mary@mail.com"]]
# Explanation: 
# The first and third John's are the same person as they have the common email
# "johnsmith@mail.com".
# The second John and Mary are different people as none of their email
# addresses are used by other accounts.
# We could return these lists in any order, for example the answer [['Mary',
# 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
# ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']]
# would still be accepted.
# 
# 
# 
# Note:
# The length of accounts will be in the range [1, 1000].
# The length of accounts[i] will be in the range [1, 10].
# The length of accounts[i][j] will be in the range [1, 30].
# 
#

# @lc code=start
from collections import defaultdict

class DSU:
    def __init__(self, N=10001):
        self.par = list(range(N))
        self.rnk = [0] * N

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = map(self.find, (x, y))
        if xr == yr: 
            return False
        elif self.rnk[xr] < self.rnk[yr]:
            self.par[xr] = yr
        elif self.rnk[xr] > self.rnk[yr]:
            self.par[yr] = xr
        else:
            self.par[yr] = xr
            self.rnk[xr] += 1

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # Depth-First Search
        # Time  complexity: O(sum(a_i x log(a_i))), where a_i is the length of accounts[i].
        # Without the log factor, this is the complexity to build the graph and search for reach component.
        # The log factor is for sorting each component at the end.
        # Space complexity: O(sum(a_i)), the space used by our graph and our search.
        # em_to_name = {}
        # graph = defaultdict(set)
        # for acc in accounts:
        #     name = acc[0]
        #     for email in acc[1:]:
        #         graph[acc[1]].add(email)
        #         graph[email].add(acc[1])
        #         em_to_name[email] = name

        # seen, ans = set(), []
        # for email in graph:
        #     if email not in seen:
        #         seen.add(email)
        #         stack, component = [email], []
        #         while stack:
        #             node = stack.pop()
        #             component.append(node)
        #             for nei in graph[node]:
        #                 if nei not in seen:
        #                     seen.add(nei)
        #                     stack.append(nei)

        #         ans.append([em_to_name[email]] + sorted(component))
        # return ans


        # Union-Find
        # Time  complexity: O(AlogA), where A = sum(a_i) and a_i is the length of accounts[i].
        # If we use union-by-rank, this complexity improves to O(A x a(A)) = O(A), 
        # where a is the Inverse-Ackermann function.
        # Space complexity: O(A), the space used by our DSU structure.
        dsu = DSU()
        em_to_name, em_to_id = {}, {}
        
        i = 0
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                em_to_name[email] = name
                if email not in em_to_id:
                    em_to_id[email] = i
                    i += 1
                dsu.union(em_to_id[acc[1]], em_to_id[email])

        ans = defaultdict(list)
        for email in em_to_name:
            ans[dsu.find(em_to_id[email])].append(email)

        return [[em_to_name[v[0]]] + sorted(v) for v in ans.values()]

        
# @lc code=end

