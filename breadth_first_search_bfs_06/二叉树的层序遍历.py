# coding:utf-8

"""

二叉树的层序遍历

"""

from collections import deque


def visit_tree(root):

    if not root:
        return

    queue = deque([root])

    while queue:
        node = queue.popleft()
        print(node.val)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)




























