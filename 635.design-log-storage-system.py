#
# @lc app=leetcode id=635 lang=python3
#
# [635] Design Log Storage System
#
# https://leetcode.com/problems/design-log-storage-system/description/
#
# algorithms
# Medium (54.86%)
# Likes:    180
# Dislikes: 87
# Total Accepted:    11.3K
# Total Submissions: 20.4K
# Testcase Example:  '["LogSystem","put","put","put","retrieve","retrieve"]\n' +
#
# You are given several logs that each log contains a unique id and timestamp.
# Timestamp is a string that has the following format:
# Year:Month:Day:Hour:Minute:Second, for example, 2017:01:01:23:59:59. All
# domains are zero-padded decimal numbers. 
# 
# Design a log storage system to implement the following functions:
# 
# void Put(int id, string timestamp): Given a log's unique id and timestamp,
# store the log in your storage system.
# 
# int[] Retrieve(String start, String end, String granularity): Return the id
# of logs whose timestamps are within the range from start to end. Start and
# end all have the same format as timestamp. However, granularity means the
# time level for consideration. For example, start = "2017:01:01:23:59:59", end
# = "2017:01:02:23:59:59", granularity = "Day", it means that we need to find
# the logs within the range from Jan. 1st 2017 to Jan. 2nd 2017.
# 
# Example 1:
# 
# put(1, "2017:01:01:23:59:59");
# put(2, "2017:01:01:22:59:59");
# put(3, "2016:01:01:00:00:00");
# retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Year"); // return
# [1,2,3], because you need to return all logs within 2016 and 2017.
# retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Hour"); // return
# [1,2], because you need to return all logs start from 2016:01:01:01 to
# 2017:01:01:23, where log 3 is left outside the range.
# 
# 
# 
# Note:
# 
# There will be at most 300 operations of Put or Retrieve.
# Year ranges from [2000,2017]. Hour ranges from [00,23].
# Output for Retrieve has no order required.
# 
# 
#
class LogSystem:

    def __init__(self):
        self.log = {}

    def put(self, id: int, timestamp: str) -> None:
        self.log[id] = timestamp.split(':')

    def retrieve(self, s: str, e: str, gra: str) -> List[int]:
        output = []
        start_string = s.split(':')
        end_string = e.split(':')

        granualrity = {
            "Year":   0,
            "Month":  1,
            "Day":    2,
            "Hour":   3,
            "Minute": 4,
            "Second": 5
        }

        start_time = int("".join(start_string[:granualrity[gra]+1]))
        end_time = int("".join(end_string[:granualrity[gra]+1]))

        for k, v in self.log.items():
            if start_time <= int("".join(v[:granualrity[gra]+1])) <= end_time:
                output.append(k)

        return output
        


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(s,e,gra)

