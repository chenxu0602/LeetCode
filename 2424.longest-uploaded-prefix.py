#
# @lc app=leetcode id=2424 lang=python3
#
# [2424] Longest Uploaded Prefix
#

# @lc code=start
class LUPrefix:

    def __init__(self, n: int):
       self._longest = 0
       self._nums = set() 

    def upload(self, video: int) -> None:
       self._nums.add(video) 
       while self._longest + 1 in self._nums:
          self._longest += 1

    def longest(self) -> int:
        return self._longest 


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()
# @lc code=end

