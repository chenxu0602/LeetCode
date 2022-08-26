#
# @lc app=leetcode id=2359 lang=python3
#
# [2359] Find Closest Node to Given Two Nodes
#

# @lc code=start
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:

        def dfs(node, arr, counter=0):
            while arr[node] == -1 and node != -1:
                arr[node] = counter
                next_node = edges[node]

                dfs(edges[node], arr, counter + 1)

            return arr

        res = float("inf")
        n1 = [-1] * len(edges)
        dfs(node1, n1)

        n2 = [-1] * len(edges)
        dfs(node2, n2)

        answer = -1
        for i in range(len(edges)):
            if n1[i] != -1 and n2[i] != -1:
                max_dist = max(n1[i], n2[i])

                if max_dist < res:
                    res = max_dist
                    answer = i

        return answer
        
# @lc code=end

