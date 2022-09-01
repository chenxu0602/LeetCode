#
# @lc app=leetcode id=2385 lang=python3
#
# [2385] Amount of Time for Binary Tree to Be Infected
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:

        """
        graph = defaultdict(list)

        def build_graph(parent, node):
            if not node: return

            if parent:
                graph[parent.val].append(node)
                graph[node.val].append(parent)

            build_graph(node, node.left)
            build_graph(node, node.right)

        build_graph(None, root)

        visited = set()
        max_infection = 0
        queue = deque([(start, 0)])
        visited.add(start)

        while queue:
            node_val, time = queue.popleft()
            max_infection = max(max_infection, time)

            for nei in graph[node_val]:
                if nei.val not in visited:
                    visited.add(nei.val)
                    queue.append((nei.val, time + 1))

        return max_infection
        """

        graph = defaultdict(list)

        stack = [(root, None)]
        while stack:
            n, p = stack.pop()
            if p:
                graph[p.val].append(n.val)
                graph[n.val].append(p.val)

            if n.left: stack.append((n.left, n))
            if n.right: stack.append((n.right, n))

        ans = -1
        seen = {start}
        queue = deque([start])

        while queue:
            for _ in range(len(queue)):
                u = queue.popleft()
                for v in graph[u]:
                    if v not in seen:
                        seen.add(v)
                        queue.append(v)

            ans += 1

        return ans
        
# @lc code=end

