# coding: utf-8

"""
问题描述：在nlogn的时间复杂度和常数空间复杂度下，对链表进行排序。

对时间复杂度有要求：首先是快速排序和归并排序，但是快速排序需要双指针，在链表中不适合，因此锁定归并排序。

基本流程：
1、找到链表的中间节点，可以采用快慢双指针，即两个指针都从头开始，快指针每次前进两步，满指针每次前进一次，这样当快指针到尾部时，慢指针到达中点。
2.找到节点的中点节点，得到了两个子链表的头指针


"""

class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


def get_middle(head):
    """获取链表的中间节点"""

    slow = fast = head

    while fast.next and fast.next.next:
        slow = slow.next         # 慢指针走一步
        fast = fast.next.next    # 快指针走两步
    return slow


def merge(l, r):
    a = ListNode(0)
    q = a
    while l and r:
        if l.val > r.val:
            q.next = r
            r = r.next
        else:
            q.next = l
            l = l.next
        q = q.next

    if l:           # 将剩余子链表链接在q的后面
        q.next = l
    if r:
        q.next = r

    return a.next

def sort_list(head):
    if head is None or head.next is None:
        return head

    mid = get_middle(head)
    l = head
    r = mid.next
    mid.next = None
    return merge(sort_list(l), sort_list(r))
