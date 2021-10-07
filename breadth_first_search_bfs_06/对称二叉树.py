# coding:utf-8


"""

判断一棵树是否是对称二叉树，深度优先搜索和广度优先搜索都可以实现，下面将用两种方式实现。


广度优先搜索思路解析：

Q: 思考如何对比对称位置上的两个节点比较方便呢？
A: 借助队列结构,令需要被比较的两个节点相邻，每次从队列中取出相邻的两个节点进行对比。如果相同，则继续；否则，立即返回结果FALSE。

变量定义
root: 二叉树的根节点
queue： 队列结构
root1: 队列中取出的第一个节点
root2: 队列中取出的第二个节点
其中root1和root2是对称位置上的两个节点。



"""


def symmetric(root):

    if not root:
        return True

    queue = []
    queue.append(root.left)
    queue.append(root.right)

    while queue:
        root1 = queue.pop()
        root2 = queue.pop()
        if not root1 and not root2:
            continue
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False

        if root1.left or root2.left or root1.right or root2.right:
            # 因为是对称节点，因此左子树的左节点对应着右子树的右节点， 左子树的右节点对应着右子树的左节点
            queue.append(root1.left)
            queue.append(root2.right)
            queue.append(root1.right)
            queue.append(root2.left)
        return True



"""

深度优先搜索思路解析



"""




def symmetric(root):

    if root:
        return dfs(root.left, root.right)
    return True

def dfs(root1, root2):
    if not root1 and not root2:
        return True

    if not root1 or root2:
        return False

    return root1.val == root2.val and dfs(root1.left, root2.right) and dfs(root1.right, root2.left)






