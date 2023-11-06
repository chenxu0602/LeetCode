#
# @lc app=leetcode id=2895 lang=python3
#
# [2895] Minimum Processing Time
#

# @lc code=start
class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:

        # tasks, processorTime, ans = sorted(tasks), sorted(processorTime), 0
        # for proc_t in processorTime:
        #     ans = max(ans, proc_t + max(tasks[-4:]))
        #     tasks = tasks[:-4]

        # return ans


        return max(map(sum, zip(sorted(processorTime), sorted(tasks)[::-4])))
        
# @lc code=end

