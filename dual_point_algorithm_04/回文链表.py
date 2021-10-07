# coding: utf-8


"""
回文链表：判断一个链表是否是回文链表，采用快慢双指针找链表中点。

问题描述： 判断一个链表是否为回文链表，回文链表即正向链表和逆向链表完全相同


example:
1->2:  false
1->2->2->1: true


思路：
1、首先找到链表的中点
2、翻转后半部分链表做反转
3、比较前半部分和后半部分是否相同


遍历定义：
1、head：表示链表的头结点
2、fast变量：移动速度较快的指针
3、slow变量：移动速度慢的指针

"""


def is_plalindrome(head):

    if head == None or head.next == None:
        return True

    # 找到链表的中点
    fast = slow = head
    while fast.next != None and fast.next.next!=None:
        slow = slow.next
        fast = fast.next.next

    def reverse_link(head):
        current = None
        pre = None
        while head != None:
            current = head.next
            head.next = pre
            pre = head
            head = current
        return pre

    start = reverse_link(slow.next)
    while start != None:
        if head.val != start.val:
            return False
        head = head.next
        start = start.next
    return True












