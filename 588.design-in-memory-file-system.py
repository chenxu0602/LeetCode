#
# @lc app=leetcode id=588 lang=python3
#
# [588] Design In-Memory File System
#
# https://leetcode.com/problems/design-in-memory-file-system/description/
#
# algorithms
# Hard (40.47%)
# Likes:    141
# Dislikes: 20
# Total Accepted:    6.7K
# Total Submissions: 16.5K
# Testcase Example:  '["FileSystem","ls","mkdir","addContentToFile","ls","readContentFromFile"]\n' +
#
# Design an in-memory file system to simulate the following functions:
# 
# ls: Given a path in string format. If it is a file path, return a list that
# only contains this file's name. If it is a directory path, return the list of
# file and directory names in this directory. Your output (file and directory
# names together) should in lexicographic order.
# 
# mkdir: Given a directory path that does not exist, you should make a new
# directory according to the path. If the middle directories in the path don't
# exist either, you should create them as well. This function has void return
# type.
# 
# addContentToFile: Given a file path and file content in string format. If the
# file doesn't exist, you need to create that file containing given content. If
# the file already exists, you need to append given content to original
# content. This function has void return type.
# 
# readContentFromFile: Given a file path, return its content in string
# format.
# 
# 
# 
# Example:
# 
# 
# Input: 
# ["FileSystem","ls","mkdir","addContentToFile","ls","readContentFromFile"]
# [[],["/"],["/a/b/c"],["/a/b/c/d","hello"],["/"],["/a/b/c/d"]]
# 
# Output:
# [null,[],null,null,["a"],"hello"]
# 
# Explanation:
# 
# 
# 
# 
# 
# Note:
# 
# 
# You can assume all file or directory paths are absolute paths which begin
# with / and do not end with / except that the path is just "/".
# You can assume that all operations will be passed valid parameters and users
# will not attempt to retrieve file content or list a directory or file that
# does not exist.
# You can assume that all directory names and file names only contain
# lower-case letters, and same names won't exist in the same directory.
# 
# 
#

from collections import defaultdict

class Node(object):
    def __init__(self):
        self.children = {}
    
    def setdefault(self, token):
        return self.children.setdefault(token, Node())

    def get(self, token):
        return self.children.get(token, None)


class FileSystem:

    def __init__(self):
        self.root = Node()
        self.fileinfo = defaultdict(str)
        
    def ls(self, path: str) -> List[str]:
        if path in self.fileinfo:
            return path.split('/')[-1:]

        cur = self.root
        for token in path.split('/'):
            if cur and token:
                cur = cur.get(token)

        return sorted(cur.children.keys()) if cur else []
        

    def mkdir(self, path: str) -> None:
        cur = self.root
        for token in path.split('/'):
            if token:
                cur = cur.setdefault(token)
        

    def addContentToFile(self, filePath: str, content: str) -> None:
        self.mkdir(filePath)
        self.fileinfo[filePath] += content
        

    def readContentFromFile(self, filePath: str) -> str:
        return self.fileinfo[filePath]


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)

