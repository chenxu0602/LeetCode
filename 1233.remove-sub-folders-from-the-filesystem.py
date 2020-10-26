#
# @lc app=leetcode id=1233 lang=python3
#
# [1233] Remove Sub-Folders from the Filesystem
#
# https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/description/
#
# algorithms
# Medium (59.12%)
# Likes:    256
# Dislikes: 47
# Total Accepted:    21.4K
# Total Submissions: 35.3K
# Testcase Example:  '["/a","/a/b","/c/d","/c/d/e","/c/f"]'
#
# Given a list of folders, remove all sub-folders in those folders and return
# in any order the folders after removing.
# 
# If a folder[i] is located within another folder[j], it is called a sub-folder
# of it.
# 
# The format of a path is one or more concatenated strings of the form: /
# followed by one or more lowercase English letters. For example, /leetcode and
# /leetcode/problems are valid paths while an empty string and / are not.
# 
# 
# Example 1:
# 
# 
# Input: folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
# Output: ["/a","/c/d","/c/f"]
# Explanation: Folders "/a/b/" is a subfolder of "/a" and "/c/d/e" is inside of
# folder "/c/d" in our filesystem.
# 
# 
# Example 2:
# 
# 
# Input: folder = ["/a","/a/b/c","/a/b/d"]
# Output: ["/a"]
# Explanation: Folders "/a/b/c" and "/a/b/d/" will be removed because they are
# subfolders of "/a".
# 
# 
# Example 3:
# 
# 
# Input: folder = ["/a/b/c","/a/b/ca","/a/b/d"]
# Output: ["/a/b/c","/a/b/ca","/a/b/d"]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= folder.length <= 4 * 10^4
# 2 <= folder[i].length <= 100
# folder[i] contains only lowercase letters and '/'
# folder[i] always starts with character '/'
# Each folder name is unique.
# 
# 
#

# @lc code=start
from collections import defaultdict

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        cache = defaultdict(list)

        for f in folder:
            fl = f.split('/')
            if fl:
                fl = fl[1:]
                for i in range(1, len(fl)):
                    cache['/' + '/'.join(fl[:i])].append(f)

        to_remove = set()
        for f in folder:
            if f in cache:
                for item in cache[f]:
                    to_remove.add(item)

        return list(set(folder) - to_remove)
        
# @lc code=end

