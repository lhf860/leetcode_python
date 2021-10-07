# coding:utf-8


"""

问题描述
给定一颗二叉树，返回从根节点到叶子结点的所有路径

"""

def all_path(root):

    res = []
    str_ = ""
    dfs(root, res, str_)
    return res

def dfs(root, res, str_):
    if not root:
        return
    else:
        str_ = str_ + str(root.val)
        dfs(root.left, res, str_ + "-")
        dfs(root.right, res, str_ + "-")
    if not root.left and not root.right:
        res.append(str_)










