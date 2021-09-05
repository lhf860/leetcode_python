# coding: utf-8


class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None



def insert_sort_list(head: ListNode):
    """
    head: 有序子链表的头指针
    p: 待排序的链表的头指针

    :param head: 有序子链表的头指针
    :return:
    """

    if head is None or head.next is None:
        return None

    p = head.next  # 将两部分两两分开
    while (p is not None):
        p_head = p.next
        current = head
        if p.val <= head.val:  # 待插入的位置在头指针的前面
            p.next = head
            head = p
        else:  # 如果插入位置不在head之前，就要进行搜寻
            while(current.next and current and current.next.val <= p.val):
                current = current.next

            p.next = current.next
            current.next = p
        p = p_head
    return head
















