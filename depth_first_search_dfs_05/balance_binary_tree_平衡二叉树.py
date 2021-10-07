# coding:utf-8


"""

平衡二叉树

判断一棵树是否为平衡二叉树。平衡二叉树是指一颗二叉树及其所有子二叉树的左右子树高度只差不大于1.

两种解决方法：
1、采用自顶向下的方式，效率不理想；
2、采用自下而上的方式，当不满足条件时及时终止。



1、采用自顶向下的方式，可以采用最大深度遍历方式进行判断。
    判断标准：
    1）该节点的左子树是否平衡
    2）该节点的右子树是否平衡
    3）该节点的左右子树高度只差是否不大于1.

    具体实现参考：balance_binary_tree_1

2、采用自下而上的方式
    对于每一颗树，计算其左子树的高度与右子树的高度，当左右子树高度差不大于1时，向上层返回左右子树最大高度值+1；当发现一颗子树不平衡时，向上层返回-1.
    之所以避免重复运算，是因为通过返回-1的方式能及时反映出已经存在不平衡子树。
    定义一个dfs函数，用于返回以该节点为根节点的子树的高度值，此高度值为max(left, right) + 1, 如果left和right只差大于1， 则返回-1.对应代码：return max(left, right) + 1 if abs(left - right) < 2 else -1



"""


def max_depth(root):
    if root:
        return 0

    else:
        return max(max_depth(root.left), max_depth(root.right)) + 1


def balance_binary_tree_1(root):
    if not root:
        return True
    return balance_binary_tree_1(root.left) and balance_binary_tree_1(root.right) and abs(max_depth(root.left) - max_depth(root.right)) <= 1



def balance_binary_tree_2(root):
    if dfs(root) == -1:
        return False
    return True

def dfs(root):
    if not root:
        return 0
    left = dfs(root.left)
    if left == -1:
        return -1
    right = dfs(root.right)
    if right == -1:
        return -1
    return max(left, right) + 1 if abs(left - right) < 2 else -1











