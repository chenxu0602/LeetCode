#
# @lc app=leetcode id=2545 lang=python3
#
# [2545] Sort the Students by Their Kth Score
#

# @lc code=start
class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:

        return sorted(score, key=lambda x: -x[k])
        
# @lc code=end

