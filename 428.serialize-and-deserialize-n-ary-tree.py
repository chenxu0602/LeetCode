
from collections import deque

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """

        serial = []

        def preorder(node):
            if not node: return
            serial.append(str(node.val))
            for child in node.children:
                preorder(child)
            serial.append('#')

        preorder(root)
        return ' '.join(serial)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """

        if not data: return None

        tokens = deque(data.split())
        root = Node(int(tokens.popleft()), [])

        def helper(node):
            if not tokens: return

            while tokens[0] != '#':
                value = tokens.popleft()
                child = Node(int(value), [])
                node.children.append(child)
                helper(child)

            tokens.popleft()

        helper(root)
        return root
