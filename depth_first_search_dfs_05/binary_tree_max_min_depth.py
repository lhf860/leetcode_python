# coding: utf-8

"""

二叉树最大\最小深度

问题：给定一颗二叉树，求其最大深度与最小深度。
最大深度是指二叉树的根节点与最远的叶子节点之间的高度
最小深度是指根节点与最近的叶子节点之间的高度。

"""

# 最大深度

def max_depth(root):
    if root:
        return 0

    else:
        return max(max_depth(root.left), max_depth(root.right)) + 1



"""二叉树最小深度"""

"""

上述的代码不能直接换成：return min(maxDepth(root.left), maxDepth(root.right)) + 1
需要考虑二叉树只有左子树和右子树的情况

当一棵树只有左子树，右侧的空子树就不应该返回上层，应该只将左子树的深度+1返回给上层即可；只有右子树同理；
若左右子树都有，那么可以采用最大深度时的方式。
"""


def min_depth(root):
    if not root:
        return 0
    if not root.left:
        return min_depth(root.right) + 1
    elif not root.right:
        return min_depth(root.left) + 1
    else:
        return min(min_depth(root.left), min_depth(root.right)) + 1














