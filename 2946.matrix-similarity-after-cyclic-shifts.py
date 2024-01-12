#
# @lc app=leetcode id=2946 lang=python3
#
# [2946] Matrix Similarity After Cyclic Shifts
#

# @lc code=start
class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:

        for l in mat:
            n = len(l)
            for i in range(n):
                if l[i] != l[(i + k) % n]:
                    return False
                
        return True
    
    
        
# @lc code=end

