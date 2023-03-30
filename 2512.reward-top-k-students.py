#
# @lc app=leetcode id=2512 lang=python3
#
# [2512] Reward Top K Students
#

# @lc code=start
import heapq

class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:

        d = [0] * len(student_id)

        pSet, nSet = set(positive_feedback), set(negative_feedback)

        for i, v in enumerate(report):
            for w in v.split():
                d[i] += 3 * (w in pSet) - (w in nSet)

        return [id for _i, id in
                heapq.nsmallest(k, enumerate(student_id),
                key=lambda x: (-d[x[0]], x[1]))]

        
# @lc code=end

