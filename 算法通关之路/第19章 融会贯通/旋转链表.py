# 链表的旋转与数组不同 由于不支持随机访问 所以之前的三次旋转是没有意义的
# 但是这对我们却更简单 我们只需要找到关键的断点即可
# 例如 1 2 3 4 5 k=2 变成 4 5 1 2 3
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self,head:ListNode,k:int)->ListNode:
        if head == None or head.next == None:
            return head
        p1 = head
        res = None
        n = 1
        # 寻找末尾
        while p1 and p1.next:
            p1 = p1.next
            n += 1
        cur = 1
        p2 = head
        # 寻找中断点
        while cur < n - k % n:
            p2 = p2.next
            cur += 1
        # 尾连首
        p1.next = head
        # 断连尾
        res = p2.next
        p2.next = None

        # res成为了新的head
        return res
