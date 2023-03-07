# 给定一个链表 判断其中是否有环
# 为了表示给定链表中的环，我们用pos表示链表尾部链接到链表中的位置，如果pos=-1 那就是没有环
from typing import List
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self,head:ListNode)->bool:
        if head is None:
            return False
        # 将node保存到哈希表中 作为key
        node_set = {}
        while head.next:
            node_set[head] = True
            if head.next in node_set:
                return True
            head = head.next
        return False
    # 双指针法 更节约空间
    def hasCycle_twopointers(self,head:ListNode)->bool:
        # 如果快慢指针在初始化之后仍然相遇 代表有环
        if head == None or head.next == None:
            return False
        pslow = pfast = head
        # 有环必会相遇 无环必会结束
        while pfast != None and pfast.next!=None:
            pslow = pslow.next
            pfast = pfast.next.next
            if pfast == pslow:
                break
        # 到达终点
        if pfast == None or pfast.next == None:
            return False
        elif pfast == pslow:
            return True

        return False


