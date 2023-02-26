# 请判断一个链表是否为回文链表
# 链表与数组的不同在于链表不支持随机访问 因此如果不考虑空间复杂度，可以直接将链表遍历存储到数组中 如此会导致空间复杂度O(n)
# 如果要以空间复杂度O(1)解决 因为单链表只有next 所以需要将链表从中间反转 然后分别走next也就完成了前后向
from typing import List
class ListNode():
    def __init__(self, val):
        if isinstance(val, int):
            self.val = val
            self.next = None

        elif isinstance(val, list):
            self.val = val[0]
            self.next = None
            cur = self
            for i in val[1:]:
                cur.next = ListNode(i)
                cur = cur.next

    def gatherAttrs(self):
        return ", ".join("{}: {}".format(k, getattr(self, k)) for k in self.__dict__.keys())

    def __str__(self):
        return self.__class__.__name__ + " {" + "{}".format(self.gatherAttrs()) + "}"

class Solution:
    def isPalindrome(self, head:ListNode) -> bool:
        pre = None
        slow = fast = head
        # 一边反转前半部分 一边当fast走到终点时，slow处于中点
        # 如果是奇数个 fast最后会停在列表尾的前一位 因为fast.next会是Null 这个时候slow在正中
        # 如果是偶数个 fast最后会停在列表的终末哨兵节点 这个时候slow处于 n//2 + 1的位置
        while fast and fast.next:
            fast = fast.next.next
            # 反转链接
            # slow.next, pre, slow = pre, slow, slow.next
            next = slow.next
            slow.next = pre
            pre = slow
            slow = next
        # 如果是奇数节点 不能让slow在正中心 需要往后移动一位
        if fast:
            slow = slow.next
        # 从中点开始往前后遍历
        while slow:
            if slow.val != pre.val:
                return False
            pre = pre.next
            slow = slow.next
        return True
