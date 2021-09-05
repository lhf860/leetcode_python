# coding:utf-8

"""需要实现二叉树"""


"""自定节点"""

class Node(object):

    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right




class Tree(object):

    def __init__(self, node=None):
        self.root = node

    def add(self, item=None):

        node = Node(val=item)

        if not self.root or self.root.val is None:
            self.root = node

        else:
            queue = []
            queue.append(self.root)

            while True:
                current_node = queue.pop(0)
                if current_node.val is None:
                    continue
                if not current_node.left:
                    current_node.left = node
                    return
                elif not current_node.right:
                    current_node.right = node
                    return
                else:
                    queue.append(current_node.left)
                    queue.append(current_node.right)






tree = Tree()

for i in range(10):
    if i == 3:
        i = None
    tree.add(i)
























