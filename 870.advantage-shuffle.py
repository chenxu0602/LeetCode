#
# @lc app=leetcode id=870 lang=python3
#
# [870] Advantage Shuffle
#
# https://leetcode.com/problems/advantage-shuffle/description/
#
# algorithms
# Medium (45.40%)
# Likes:    563
# Dislikes: 33
# Total Accepted:    21.6K
# Total Submissions: 47.3K
# Testcase Example:  '[2,7,11,15]\n[1,10,4,11]'
#
# Given two arrays A and B of equal size, the advantage of A with respect to B
# is the number of indices i for which A[i] > B[i].
# 
# Return any permutation of A that maximizes its advantage with respect to
# B.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: A = [2,7,11,15], B = [1,10,4,11]
# Output: [2,11,7,15]
# 
# 
# 
# Example 2:
# 
# 
# Input: A = [12,24,8,32], B = [13,25,32,11]
# Output: [24,32,8,12]
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length = B.length <= 10000
# 0 <= A[i] <= 10^9
# 0 <= B[i] <= 10^9
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        # Greedy
        # Time  complexity: O(NlogN), where N is the length of A and B.
        # Space complexity: O(N)
        sortedA, sortedB = sorted(A), sorted(B)

        # assigned[b] = list of a that are assigned to beat b
        # remaining = list of a that are not assigned to any b
        assigned = {b: [] for b in B}
        remaining = []

        j = 0
        for a in sorted(A):
            if a > sortedB[j]:
                assigned[sortedB[j]].append(a)
                j += 1
            else:
                remaining.append(a)

        return [assigned[b].pop() if assigned[b] else remaining.pop() for b in B] 
        
# @lc code=end

