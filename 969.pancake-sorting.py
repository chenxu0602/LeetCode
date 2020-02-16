#
# @lc app=leetcode id=969 lang=python3
#
# [969] Pancake Sorting
#
# https://leetcode.com/problems/pancake-sorting/description/
#
# algorithms
# Medium (64.64%)
# Likes:    275
# Dislikes: 345
# Total Accepted:    21.2K
# Total Submissions: 32.8K
# Testcase Example:  '[3,2,4,1]'
#
# Given an array A, we can perform a pancake flip: We choose some positive
# integer k <= A.length, then reverse the order of the first k elements of A.
# We want to perform zero or more pancake flips (doing them one after another
# in succession) to sort the array A.
# 
# Return the k-values corresponding to a sequence of pancake flips that sort
# A.  Any valid answer that sorts the array within 10 * A.length flips will be
# judged as correct.
# 
# 
# 
# Example 1:
# 
# 
# Input: [3,2,4,1]
# Output: [4,2,4,3]
# Explanation: 
# We perform 4 pancake flips, with k values 4, 2, 4, and 3.
# Starting state: A = [3, 2, 4, 1]
# After 1st flip (k=4): A = [1, 4, 2, 3]
# After 2nd flip (k=2): A = [4, 1, 2, 3]
# After 3rd flip (k=4): A = [3, 2, 1, 4]
# After 4th flip (k=3): A = [1, 2, 3, 4], which is sorted. 
# 
# 
# 
# Example 2:
# 
# 
# Input: [1,2,3]
# Output: []
# Explanation: The input is already sorted, so there is no need to flip
# anything.
# Note that other answers, such as [3, 3], would also be accepted.
# 
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 100
# A[i] is a permutation of [1, 2, ..., A.length]
# 
# 
#

# @lc code=start
class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:

        n = len(A)
        res = []
        for i in range(n):
            cur_max = max(A[0:n-i])
            j = 0
            while A[j] != cur_max:
                j += 1
            A[:j+1] = reversed(A[:j+1])
            res.append(j+1)
            A[:n-i] = reversed(A[:n-i])
            res.append(n-i)
        return res
        
# @lc code=end

