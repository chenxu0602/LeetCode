#
# @lc app=leetcode id=1361 lang=python3
#
# [1361] Validate Binary Tree Nodes
#
# https://leetcode.com/problems/validate-binary-tree-nodes/description/
#
# algorithms
# Medium (45.28%)
# Likes:    260
# Dislikes: 94
# Total Accepted:    15.5K
# Total Submissions: 34.4K
# Testcase Example:  '4\n[1,-1,3,-1]\n[2,-1,-1,-1]'
#
# You have n binary tree nodes numbered from 0 to n - 1 where node i has two
# children leftChild[i] and rightChild[i], return true if and only if all the
# given nodes form exactly one valid binary tree.
# 
# If node i has no left child then leftChild[i] will equal -1, similarly for
# the right child.
# 
# Note that the nodes have no values and that we only use the node numbers in
# this problem.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
# Output: true
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
# Output: false
# 
# 
# Example 3:
# 
# 
# 
# 
# Input: n = 2, leftChild = [1,0], rightChild = [-1,-1]
# Output: false
# 
# 
# Example 4:
# 
# 
# 
# 
# Input: n = 6, leftChild = [1,-1,-1,4,-1,-1], rightChild = [2,-1,-1,5,-1,-1]
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 10^4
# leftChild.length == rightChild.length == n
# -1 <= leftChild[i], rightChild[i] <= n - 1
# 
# 
#

# @lc code=start
class DSU:
    def __init__(self, N):
        self.par = list(range(N))
        self.rnk = [0] * N

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = map(self.find, (x, y))
        if xr == yr: return False
        if self.rnk[xr] < self.rnk[yr]:
            xr, yr = yr, xr
        if self.rnk[xr] == self.rnk[yr]:
            self.rnk[xr] += 1
        self.par[yr] = xr
        return True

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # O(n)
        dsu = DSU(n)
        for i in range(n):
            left, right = leftChild[i], rightChild[i]
            if left >= 0:
                if not dsu.union(i, left):
                    return False
            if right >= 0:
                if not dsu.union(i, right):
                    return False
                
        roots = [dsu.find(i) for i in range(n)]
        return len(set(roots)) == 1
        
# @lc code=end

