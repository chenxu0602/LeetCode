
class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """

        self.stack = []
        self.iter = iter(nestedList)


    def next(self):
        """
        :rtype: int
        """
        return self.nextInteger


    def hasNext(self):
        """
        :rtype: bool
        """

        while self.iter:
            try:
                r = self.iter.next()
            except StopIteration:
                self.iter = self.stack.pop() if self.stack else None
                continue

            if r.isInteger():
                self.nextInteger = r.getInteger()
                return True

            self.stack.append(self.iter)
            self.iter = iter(r.getList())

        return False
