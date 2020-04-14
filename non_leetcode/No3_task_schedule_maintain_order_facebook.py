#!/usr/bin/python
# coding=utf-8
################################################################################
'''
// Given a list of task execution order: [1, 1, 2, 1],
same number indicates same type of task;

// Executing any type of task takes only one time slot,
while there should be at least a cooldown time cd between executing same type of task
// Write a function processTasks(int[] order_list, int cooldown) that returns
the interval of executing all tasks

// For example: order_list = [1, 1, 2, 1], cd = 2, then executing situation would be:
// [1 _ _ 1 2 _ 1], the interval is 7, si processTasks() should return 7

// Complexity: assume M types of tasks, and N tasks to execute；
// Time: O(NM), Space: O(M)
'''
################################################################################
'''
public int processTasks(int[] orderList, int cooldown) {
// key is the task Id, value is the recently time it should be put
   Map<Integer, Integer> map = new HashMap<>();
   int time = 0;
   for (int id : orderList) {
     if (map.containsKey(id)) {
       time = Math.max(map.get(id) + cooldown + 1, time);
     }
     map.put(id, time++);
   }
   return time;
}

'''

class Solution(object):
    def processTasks(self, orderList, cooldown):

        count = {}
        res = 0
        for ID in orderList:
            res += 1
            if ID in count:
                prev_time = count[ID]
                time_interval = res - prev_time - 1
                if time_interval < cooldown:
                    res += cooldown - time_interval
            count[ID] = res
        return res




a = Solution()
print a.processTasks([1,1,2,1], 2)
print a.processTasks([1,2,2,1], 4)




