#
# @lc app=leetcode id=1429 lang=python3
#
# [1429] First Unique Number
#
# https://leetcode.com/problems/first-unique-number/description/
#
# algorithms
# Medium (48.38%)
# Likes:    155
# Dislikes: 5
# Total Accepted:    46.8K
# Total Submissions: 96.7K
# Testcase Example:  '["FirstUnique","showFirstUnique","add","showFirstUnique","add","showFirstUnique","add","showFirstUnique"]\r' + '\n[[[2,3,5]],[],[5],[],[2],[],[3],[]]\r'
#
# You have a queue of integers, you need to retrieve the first unique integer
# in the queue.
# 
# Implement the FirstUnique class:
# 
# 
# FirstUnique(int[] nums) Initializes the object with the numbers in the
# queue.
# int showFirstUnique() returns the value of the first unique integer of the
# queue, and returns -1 if there is no such integer.
# void add(int value) insert value to the queue.
# 
# 
# 
# Example 1:
# 
# 
# Input: 
# 
# ["FirstUnique","showFirstUnique","add","showFirstUnique","add","showFirstUnique","add","showFirstUnique"]
# [[[2,3,5]],[],[5],[],[2],[],[3],[]]
# Output: 
# [null,2,null,2,null,3,null,-1]
# Explanation: 
# FirstUnique firstUnique = new FirstUnique([2,3,5]);
# firstUnique.showFirstUnique(); // return 2
# firstUnique.add(5);            // the queue is now [2,3,5,5]
# firstUnique.showFirstUnique(); // return 2
# firstUnique.add(2);            // the queue is now [2,3,5,5,2]
# firstUnique.showFirstUnique(); // return 3
# firstUnique.add(3);            // the queue is now [2,3,5,5,2,3]
# firstUnique.showFirstUnique(); // return -1
# 
# 
# Example 2:
# 
# 
# Input: 
# 
# ["FirstUnique","showFirstUnique","add","add","add","add","add","showFirstUnique"]
# [[[7,7,7,7,7,7]],[],[7],[3],[3],[7],[17],[]]
# Output: 
# [null,-1,null,null,null,null,null,17]
# Explanation: 
# FirstUnique firstUnique = new FirstUnique([7,7,7,7,7,7]);
# firstUnique.showFirstUnique(); // return -1
# firstUnique.add(7);            // the queue is now [7,7,7,7,7,7,7]
# firstUnique.add(3);            // the queue is now [7,7,7,7,7,7,7,3]
# firstUnique.add(3);            // the queue is now [7,7,7,7,7,7,7,3,3]
# firstUnique.add(7);            // the queue is now [7,7,7,7,7,7,7,3,3,7]
# firstUnique.add(17);           // the queue is now [7,7,7,7,7,7,7,3,3,7,17]
# firstUnique.showFirstUnique(); // return 17
# 
# 
# Example 3:
# 
# 
# Input: 
# ["FirstUnique","showFirstUnique","add","showFirstUnique"]
# [[[809]],[],[809],[]]
# Output: 
# [null,809,null,-1]
# Explanation: 
# FirstUnique firstUnique = new FirstUnique([809]);
# firstUnique.showFirstUnique(); // return 809
# firstUnique.add(809);          // the queue is now [809,809]
# firstUnique.showFirstUnique(); // return -1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^8
# 1 <= value <= 10^8
# At most 50000 calls will be made to showFirstUnique and add.
# 
# 
#

# @lc code=start
from collections import deque, OrderedDict

class FirstUnique:

    def __init__(self, nums: List[int]):
      # self._queue = deque(nums)    
      # self._is_unique = {}
      # for num in nums:
      #     self.add(num)

      self._queue = OrderedDict()
      self._is_unique = {}
      for num in nums:
          self.add(num)

    def showFirstUnique(self) -> int:
      # while self._queue and not self._is_unique[self._queue[0]]:
      #       self._queue.popleft()

      # if self._queue:
      #     return self._queue[0]  

      # return -1


      if self._queue:
          return next(iter(self._queue))

      return -1

    def add(self, value: int) -> None:
        # if value not in self._is_unique:
        #     self._is_unique[value] = True
        #     self._queue.append(value)
        # else:
        #     self._is_unique[value] = False


        if value not in self._is_unique:
            self._is_unique[value] = True
            self._queue[value] = None
        elif self._is_unique[value]:
            self._is_unique[value] = False
            self._queue.pop(value)
        
# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
# @lc code=end

