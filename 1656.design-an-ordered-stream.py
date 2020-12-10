#
# @lc app=leetcode id=1656 lang=python3
#
# [1656] Design an Ordered Stream
#
# https://leetcode.com/problems/design-an-ordered-stream/description/
#
# algorithms
# Easy (80.87%)
# Likes:    43
# Dislikes: 227
# Total Accepted:    8.3K
# Total Submissions: 10.2K
# Testcase Example:  '["OrderedStream","insert","insert","insert","insert","insert"]\n' + '[[5],[3,"ccccc"],[1,"aaaaa"],[2,"bbbbb"],[5,"eeeee"],[4,"ddddd"]]'
#
# There is a stream of n (id, value) pairs arriving in an arbitrary order,
# where id is an integer between 1 and n and value is a string. No two pairs
# have the same id.
# 
# Design a stream that returns the values in increasing order of their IDs by
# returning a chunk (list) of values after each insertion. The concatenation of
# all the chunks should result in a list of the sorted values.
# 
# Implement the OrderedStream class:
# 
# 
# OrderedStream(int n) Constructs the stream to take n values.
# String[] insert(int id, String value) Inserts the pair (id, value) into the
# stream, then returns the largest possible chunk of currently inserted values
# that appear next in the order.
# 
# 
# 
# Example:
# 
# 
# 
# 
# Input
# ["OrderedStream", "insert", "insert", "insert", "insert", "insert"]
# [[5], [3, "ccccc"], [1, "aaaaa"], [2, "bbbbb"], [5, "eeeee"], [4, "ddddd"]]
# Output
# [null, [], ["aaaaa"], ["bbbbb", "ccccc"], [], ["ddddd", "eeeee"]]
# 
# Explanation
# // Note that the values ordered by ID is ["aaaaa", "bbbbb", "ccccc", "ddddd",
# "eeeee"].
# OrderedStream os = new OrderedStream(5);
# os.insert(3, "ccccc"); // Inserts (3, "ccccc"), returns [].
# os.insert(1, "aaaaa"); // Inserts (1, "aaaaa"), returns ["aaaaa"].
# os.insert(2, "bbbbb"); // Inserts (2, "bbbbb"), returns ["bbbbb", "ccccc"].
# os.insert(5, "eeeee"); // Inserts (5, "eeeee"), returns [].
# os.insert(4, "ddddd"); // Inserts (4, "ddddd"), returns ["ddddd", "eeeee"].
# // Concatentating all the chunks returned:
# // [] + ["aaaaa"] + ["bbbbb", "ccccc"] + [] + ["ddddd", "eeeee"] = ["aaaaa",
# "bbbbb", "ccccc", "ddddd", "eeeee"]
# // The resulting order is the same as the order above.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 1000
# 1 <= id <= n
# value.length == 5
# value consists only of lowercase letters.
# Each call to insert will have a unique id.
# Exactly n calls will be made to insert.
# 
# 
#

# @lc code=start
class OrderedStream:

    def __init__(self, n: int):
      self.data = [None] * n   
      self.ptr = 0
        
    def insert(self, id: int, value: str) -> List[str]:
        id -= 1    
        self.data[id] = value
        if id > self.ptr:
            return []

        while self.ptr < len(self.data) and self.data[self.ptr]:
            self.ptr += 1

        return self.data[id:self.ptr]
        
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)
# @lc code=end

