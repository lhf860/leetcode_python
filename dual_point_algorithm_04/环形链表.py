# coding: utf-8


"""

比较经典题目： 环形链表

即：判断链表中是否存在环， 解决方法：快慢双指针

"""

class ListNode(object):

    def __init__(self, x):
        self.value = x
        self.next = None

def cycle(head):

    if head == None:
        return False

    fast = head
    slow = head
    while fast:
        if fast.next == None:
            return fast
        fast = fast.next.next
        slow = fast.next
        if fast == slow:
            return True
    return False








