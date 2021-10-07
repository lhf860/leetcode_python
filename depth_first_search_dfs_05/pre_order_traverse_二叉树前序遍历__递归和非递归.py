# coding: utf-8

"""

实现二叉树的前序遍历（前序遍历即在访问过程中，对于该二叉树及其所有子树，均先访问根节点，再访问左子树，最后访问右子树）


实现二叉树的前序遍历，两种方式：
1、递归方式
2、非递归方式

"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 递归遍历二叉树（前序）
def visit_tree(root):
    if not root:
        return ""
    print(root.val)
    visit_tree(root.left)
    visit_tree(root.right)

"""
非递归方式遍历
实现前序遍历二叉树需要借助一种常用的数据结构--栈，栈的特性：后进先出
在Python中，可以使用list实现栈即可，list的pop实现了移除列表中最后一个元素，相当于栈顶元素出栈；append实现了向列表尾部添加一个元素，相当于入栈，位于栈顶。

变量定义：
1、root： 输入变量，表示二叉树的根节点
2、stack： 表示栈结构，list类型
3、top： 表示栈顶树节点，TreeNode类型。

"""

def visit_tree_stack(root: TreeNode):
    stack = []
    stack.append(root)

    while len(stack) != 0:
        top = stack.pop()
        print(top.val)
        if top.right:
            stack.append(top.right)
        if top.left:
            stack.append(top.left)













