# coding: utf-8


"""

给定一颗二叉树，保证为非空二叉树，返回最大路径和。此处的路径可以是从树中任意节点出发到任意节点的路径，路径中至少包含一个节点即可。


因为可以从任意节点到任意节点，因此每一颗子树都需要判断当前路径是不是最大路径。

访问每个节点时，分别计算其左右子树的最大值路径，只有当左右子树的最大路径大于0时，才是能增大路径之和，因此当左右子树最大路径小于0时，直接置0.
那么每一次返回上层上层的值，是该节点与其左子树最大路径之和或者该节点与其右子树最大路径之和，因为路径不能折回， 这样才能保证递归返回当前节点的最大路径。


"""

class MaxValue(object):

    def max_path(self, root):
        self.res = float("-inf")
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if not root:
            return 0
        left = max(0, self.dfs(root.left))
        right = max(0, self.dfs(root.right))
        self.res = max(self.res, left + root.val, right + root.val)
        return root.val + max(left, right)









