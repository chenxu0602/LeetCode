#
# @lc app=leetcode id=2925 lang=python3
#
# [2925] Maximum Score After Applying Operations on a Tree
#

# @lc code=start
from collections import defaultdict

class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:

        # Post-order traversal: for some node, return the lowest deductible value up to this position; i.e. if a node's value exceeds the sum of the lowest deductibles from its children, deduct the sum mins from children. otherwise if this node has a lower value, deduct this node from the sum.

        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        def get_min(node, par):
            rec = [get_min(c, node) for c in tree[node] if c != par]
            if not len(rec): return values[node]
            return min(sum(rec), values[node])

        return sum(values) - get_min(0, -1)

        
# @lc code=end

